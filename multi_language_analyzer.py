import argparse
from tree_sitter import Language, Parser
import os
import glob

class BaseCodeAnalyzer:
    def __init__(self, language_name, language_path, query_config):
        self.language_name = language_name
        self.language_path = language_path
        self.query_config = query_config
        self.parser, self.language = self.setup_parser()
        self.function_query = query_config['function_query']

    def setup_parser(self):
        language = Language(self.language_path, self.language_name)
        parser = Parser()
        parser.set_language(language)
        return parser, language

    def extract_docstring(self, node, default_description):
        body_node = None
        for child in node.children:
            if child.type == 'block':
                body_node = child
                break

        if body_node and body_node.children:
            first_stmt = body_node.children[0]
            if first_stmt.type == 'expression_statement':
                string_node = first_stmt.children[0]
                if string_node.type == 'string':
                    return string_node.text.decode('utf8').strip('"""').strip("'''").strip()
        return default_description

    def analyze_file(self, file_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        tree = self.parser.parse(content)
        functions = []

        query = self.language.query(self.function_query)
        captures = query.captures(tree.root_node)

        for node, _ in captures:
            name_node = node.child_by_field_name('name')
            if name_node:
                function_name = name_node.text.decode('utf8')
                print(f"Found function: {function_name}")
                signature = self.analyze_function_signature(node)
                operations = self.analyze_operations(node.parent)
                operations_desc = self.generate_accurate_description(function_name, operations)

                functions.append({
                    'name': function_name,
                    'signature': signature,
                    'operations': operations_desc,
                    'calls': self.find_function_calls(node)
                })

        return {
            'file': file_path,
            'functions': functions
        }

    def analyze_operations(self, node):
        operation_patterns = {
            'test': {'pattern': self.query_config.get('test_query', '(call function: (identifier) @test)'),
                    'description': 'Performs unit testing'},
            'assert': {'pattern': self.query_config.get('assert_query', '(assert_statement) @assert'),
                      'description': 'Validates expected behavior'},
            'api_call': {'pattern': self.query_config.get('api_query', '(call function: (attribute object: (identifier)) @api)'),
                        'description': 'Makes API requests'},
        }

        detected_ops = []
        for op_type, op_info in operation_patterns.items():
            query = self.language.query(op_info['pattern'])
            if query.captures(node):
                detected_ops.append(op_info['description'])

        return " and ".join(detected_ops) if detected_ops else "Basic function operations"

    def analyze_function_signature(self, node):
        params = []
        returns = None

        parameters = node.child_by_field_name('parameters')
        if parameters:
            for param in parameters.children:
                if param.type == 'identifier':
                    param_text = param.text.decode('utf8')
                    params.append(param_text)
                elif param.type == 'typed_parameter':
                    param_name = param.child_by_field_name('name').text.decode('utf8')
                    param_type = param.child_by_field_name('type').text.decode('utf8')
                    params.append(f"{param_name}: {param_type}")

        return_annotation = node.child_by_field_name('return_type')
        if return_annotation:
            returns = return_annotation.text.decode('utf8')

        return {
            'parameters': params,
            'return_type': returns
        }

    def find_function_calls(self, node):
        query = self.language.query(self.query_config['call_query'])
        calls = set()
        for n, _ in query.captures(node):
            calls.add(n.text.decode('utf8'))
        return calls

    def generate_accurate_description(self, function_name, operations_desc):
        return f"Function {function_name} {operations_desc}"

class JavaAnalyzer(BaseCodeAnalyzer):
    def __init__(self):
        query_config = {
            'function_query': """
                (method_declaration
                    name: (identifier)
                    parameters: (formal_parameters)
                    type: (_)?) @method
            """,
            'call_query': """
                (method_invocation 
                    name: (identifier) @call)
            """,
            'parameter_query': """
                (formal_parameter
                    type: (_)
                    name: (identifier)) @param
            """
        }
        super().__init__('java', os.path.expanduser('~/.tree-sitter/tree-sitter-java.so'), query_config)

    def analyze_function_signature(self, node):
        params = []
        returns = None

        # Get return type
        type_node = node.child_by_field_name('type')
        if type_node:
            returns = type_node.text.decode('utf8')

        # Get parameters
        parameters = node.child_by_field_name('parameters')
        if parameters:
            param_query = self.language.query(self.query_config['parameter_query'])
            for param, _ in param_query.captures(parameters):
                param_type = param.child_by_field_name('type').text.decode('utf8')
                param_name = param.child_by_field_name('name').text.decode('utf8')
                params.append(f"{param_type} {param_name}")

        return {
            'parameters': params,
            'return_type': returns if returns else 'void'
        }


    def analyze_operations(self, node):
        operation_patterns = {
            'method_call': {'pattern': """
                (method_invocation) @method_call
            """, 'description': 'Makes method calls'},
            'field_access': {'pattern': """
                (field_access) @field
            """, 'description': 'Accesses class fields'},
            'variable_declaration': {'pattern': """
                (local_variable_declaration) @var
            """, 'description': 'Declares variables'}
        }

        detected_ops = []
        for op_type, op_info in operation_patterns.items():
            query = self.language.query(op_info['pattern'])
            if query.captures(node):
                detected_ops.append(op_info['description'])

        return " and ".join(detected_ops) if detected_ops else "Basic method operations"

class GoAnalyzer(BaseCodeAnalyzer):
    def __init__(self):
        query_config = {
            'function_query': """
                (function_declaration
                name: (identifier)) @function
            """,
            'call_query': """
                (call_expression
                function: (identifier) @call)
            """,
            'test_query': """
                (function_declaration
                name: (_) @test
                (#match? @test "^Test"))
            """
        }
        super().__init__('go', os.path.expanduser('~/.tree-sitter/tree-sitter-go.so'), query_config)

class PythonAnalyzer(BaseCodeAnalyzer):
    def __init__(self):
        query_config = {
            'function_query': """
                (function_definition
                name: (identifier)) @function
            """,
            'call_query': """
                (call function: (identifier) @call)
            """,
            'test_query': """
                (function_definition
                name: (_) @test
                (#match? @test "^test_"))
            """
        }
        super().__init__('python', os.path.expanduser('~/.tree-sitter/tree-sitter-python.so'), query_config)

class CodeReader:
    def read_from_directory(self, directory):
        supported_extensions = ('.py', '.java', '.go')
        files = []
        for ext in supported_extensions:
            files.extend(glob.glob(f"{directory}/**/*{ext}", recursive=True))
        return files

class MultiLanguageAnalyzer:
    def __init__(self):
        self.analyzers = {
            'python': PythonAnalyzer(),
            'java': JavaAnalyzer(),
            'go': GoAnalyzer()
        }

    def analyze_file(self, file_path):
        extension = file_path.split('.')[-1]
        language_map = {
            'py': 'python',
            'java': 'java',
            'go': 'go'
        }

        if extension in language_map:
            analyzer = self.analyzers[language_map[extension]]
            return analyzer.analyze_file(file_path)
        return None

def main():
    parser = argparse.ArgumentParser(description='Multi-language Code Analyzer')
    parser.add_argument('--project-dir', required=True, help='Path to the project directory')
    args = parser.parse_args()

    reader = CodeReader()
    files = reader.read_from_directory(args.project_dir)

    analyzer = MultiLanguageAnalyzer()
    results = []

    for file in files:
        result = analyzer.analyze_file(file)
        if result:
            results.append(result)
            print(f"\nAnalyzed {file}:")
            for function in result['functions']:
                print(f"  Function: {function['name']}")
                print(f"  Signature: {function['signature']}")
                print(f"  Operations: {function['operations']}")
                print(f"  Calls: {function['calls']}\n")

if __name__ == "__main__":
    main()
