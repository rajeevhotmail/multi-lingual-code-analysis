from tree_sitter import Language, Parser
import os

class JavaAnalyzer:
    def __init__(self):
        self.query_config = {
            'function_query': """
                (method_declaration) @method
            """,
            'parameter_query': """
                (formal_parameters
                    (formal_parameter
                        name: (identifier)
                        type: (_))) @param
            """,
            'call_query': """
                (method_invocation
                    name: (identifier) @method_name)
            """
        }
        self.parser, self.language = self.setup_parser()

    def setup_parser(self):
        language = Language(os.path.expanduser('~/.tree-sitter/tree-sitter-java.so'), 'java')
        parser = Parser()
        parser.set_language(language)
        return parser, language
    def build_call_hierarchy(self, results):
        # Build complete call graph
        call_graph = {}
        for file_result in results:
            for method in file_result['functions']:
                method_name = method['name']
                if method_name not in call_graph:
                    call_graph[method_name] = {
                        'direct_calls': set(method['calls']),
                        'called_by': set(),
                        'file': file_result['file']
                    }

        # Build reverse relationships
        for caller, info in call_graph.items():
            for called in info['direct_calls']:
                if called in call_graph:
                    call_graph[called]['called_by'].add(caller)

        return call_graph

    def analyze_file(self, file_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        tree = self.parser.parse(content)
        methods = []
        all_calls = {}  # Track all method calls

        # First pass: collect all method calls
        query = self.language.query(self.query_config['function_query'])
        captures = query.captures(tree.root_node)

        for node, _ in captures:
            name_node = node.child_by_field_name('name')
            if name_node:
                method_name = name_node.text.decode('utf8')
                calls = self.find_method_calls(node)
                all_calls[method_name] = calls

        # Second pass: build complete method info with relationships
        for node, _ in captures:
            name_node = node.child_by_field_name('name')
            if name_node:
                method_name = name_node.text.decode('utf8')
                print(f"Found method: {method_name}")

                # Build relationships
                calls = all_calls[method_name]
                called_by = {caller for caller, called_methods in all_calls.items()
                           if method_name in called_methods}

                methods.append({
                    'name': method_name,
                    'signature': self.analyze_method_signature(node),
                    'operations': self.analyze_operations(node),
                    'calls': calls,
                    'relationships': {
                        'calls': list(calls),
                        'called_by': list(called_by)
                    },
                    'description': self.generate_description(node)  # Add this line
                })

        # Build complete call hierarchy
        call_graph = self.build_call_hierarchy([{
            'file': file_path,
            'functions': methods
        }])

        return {
            'file': file_path,
            'functions': methods,
            'call_graph': call_graph,
            'description': f"Java source file containing {len(methods)} methods"  # Add file description
        }
    def get_modifiers(self, node):
        modifiers = []
        modifier_query = self.language.query("""
            (method_declaration
                (modifiers) @modifier)
        """)
        modifier_captures = modifier_query.captures(node)
        for n, _ in modifier_captures:
            modifiers.append(n.text.decode('utf8'))
        return modifiers

    def analyze_method_calls(self, node):
        calls = {}
        call_query = self.language.query("""
            (method_invocation
                name: (identifier) @method_name
                arguments: (argument_list) @args)
        """)

        captures = call_query.captures(node)
        for n, capture_name in captures:
            if capture_name == 'method_name':
                method_name = n.text.decode('utf8')
                calls[method_name] = {
                    'name': method_name,
                    'return_type': self.find_method_return_type(method_name),
                    'args': []
                }

        return calls
    def find_method_return_type(self, method_name):
        query = self.language.query("""
            (method_declaration
                name: (identifier) @name
                type: (_) @return_type)
        """)

        return_types = {}
        for file_result in self.results:
            tree = self.parser.parse(bytes(file_result['content'], 'utf8'))
            captures = query.captures(tree.root_node)
            for node, capture_name in captures:
                if capture_name == 'name' and node.text.decode('utf8') == method_name:
                    return_types[method_name] = node.parent.child_by_field_name('type').text.decode('utf8')

        return return_types.get(method_name, 'unknown')
    def analyze_parameter_types(self, param_node):
        param_info = {}

        # Get parameter type details
        type_query = self.language.query("""
            (formal_parameter
                type: (_) @type
                name: (identifier) @name
                dimensions: (dimensions)? @array)
        """)

        captures = type_query.captures(param_node)
        for node, capture_name in captures:
            if capture_name == 'type':
                param_info['type'] = node.text.decode('utf8')
            elif capture_name == 'name':
                param_info['name'] = node.text.decode('utf8')
            elif capture_name == 'array':
                param_info['is_array'] = True

        return param_info


    def analyze_method_signature(self, node):
        params = []
        modifiers = []

        # Get return type and basic signature
        type_node = node.child_by_field_name('type')
        return_type = type_node.text.decode('utf8') if type_node else 'void'

        params_node = node.child_by_field_name('parameters')
        if params_node:
            for param in params_node.children:
                if param.type == 'formal_parameter':
                    param_type = param.child_by_field_name('type').text.decode('utf8')
                    param_name = param.child_by_field_name('name').text.decode('utf8')
                    params.append(f"{param_type} {param_name}")

        # Clean up modifiers to exclude annotations
        modifier_query = self.language.query("""
            (method_declaration
                (modifiers) @modifier)
        """)
        modifier_captures = modifier_query.captures(node)
        for n, _ in modifier_captures:
            mod_text = n.text.decode('utf8')
            if not mod_text.startswith('@'):
                modifiers.append(mod_text)

        return {
            'parameters': params,
            'return_type': return_type,
            'modifiers': modifiers
        }


    def generate_description(self, node):
        """Generate human-readable description of methods"""
        desc = []

        # Get method info
        modifiers = self.get_modifiers(node)
        return_type = node.child_by_field_name('type').text.decode('utf8') if node.child_by_field_name('type') else 'void'
        name = node.child_by_field_name('name').text.decode('utf8')

        # Build description
        desc.append(f"This {' '.join(modifiers)} method '{name}' returns {return_type}")

        # Add parameter description
        params = self.get_parameters_description(node)
        if params:
            desc.append(f"It takes parameters: {params}")

        # Add behavior description
        if self.has_field_access(node):
            desc.append("It accesses class fields")
        if self.find_method_calls(node):
            desc.append(f"It calls other methods: {', '.join(self.find_method_calls(node))}")

        return " and ".join(desc)

    def find_java_files(self, project_dir):
        java_files = []
        for root, dirs, files in os.walk(project_dir):
            for file in files:
                if file.endswith('.java'):
                    java_files.append(os.path.join(root, file))
        return java_files

    def analyze_project(self, project_dir):
        java_files = self.find_java_files(project_dir)
        print(f"Found {len(java_files)} Java files")
        results = []
        for file_path in java_files:
            print(f"Processing: {file_path}")
            result = self.analyze_file(file_path)
            results.append(result)
        return results
    def get_parameters_description(self, node):
        params = []
        params_node = node.child_by_field_name('parameters')
        if params_node:
            for param in params_node.children:
                if param.type == 'formal_parameter':
                    param_type = param.child_by_field_name('type').text.decode('utf8')
                    param_name = param.child_by_field_name('name').text.decode('utf8')
                    params.append(f"{param_type} {param_name}")
        return ", ".join(params) if params else ""

    def find_method_calls(self, node):
        calls = set()
        query = self.language.query(self.query_config['call_query'])
        captures = query.captures(node)
        for n, _ in captures:
            calls.add(n.text.decode('utf8'))
        return calls

    def analyze_call_stack(self, entry_point, results):
        call_stack = []
        visited = set()

        def build_call_chain(method_name, depth=0):
            if method_name in visited:
                return
            visited.add(method_name)

            for file_result in results:
                for method in file_result['functions']:
                    if method['name'] == method_name:
                        call_stack.append({
                            'name': method_name,
                            'depth': depth,
                            'file': file_result['file'],
                            'calls': method['calls']
                        })
                        for called_method in method['calls']:
                            build_call_chain(called_method, depth + 1)

        build_call_chain(entry_point)
        return call_stack

    def analyze_operations(self, node):
        operations = []

        # Detect common Java operations
        if self.has_loops(node):
            operations.append("Contains loops")
        if self.has_try_catch(node):
            operations.append("Handles exceptions")
        if self.has_field_access(node):
            operations.append("Accesses class fields")
        if self.has_new_instance(node):
            operations.append("Creates new objects")
        if self.has_annotations(node):
            operations.append("Uses annotations")

        return " and ".join(operations) if operations else "Basic Java operations"

    def has_annotations(self, node):
        annotation_query = self.language.query("""
            (marker_annotation) @annotation
        """)
        return len(annotation_query.captures(node)) > 0

    def has_interface_implementation(self, node):
        interface_query = self.language.query("""
            (implements_clause) @interface
        """)
        return len(interface_query.captures(node)) > 0

    def has_inheritance(self, node):
        extends_query = self.language.query("""
            (superclass) @extends
        """)
        return len(extends_query.captures(node)) > 0

    def has_loops(self, node):
        loop_query = self.language.query("""
            [(for_statement) (while_statement) (do_statement)] @loop
        """)
        return len(loop_query.captures(node)) > 0

    def has_try_catch(self, node):
        try_query = self.language.query("""
            (try_statement) @try
        """)
        return len(try_query.captures(node)) > 0

    def has_field_access(self, node):
        field_query = self.language.query("""
            (field_access) @field
        """)
        return len(field_query.captures(node)) > 0

    def has_new_instance(self, node):
        new_query = self.language.query("""
            (object_creation_expression) @new
        """)
        return len(new_query.captures(node)) > 0

def test_java_analyzer():
    analyzer = JavaAnalyzer()
    test_file = 'test_files/Test.java'
    result = analyzer.analyze_file(test_file)

    print("\nJava Analysis Results:")
    print("=====================")
    for method in result['functions']:
        print(f"\nMethod: {method['name']}")
        print(f"Signature: {method['signature']}")
        print(f"Operations: {method['operations']}")
        print(f"Calls: {method['calls']}")

if __name__ == "__main__":
    test_java_analyzer()
