from tree_sitter import Language, Parser
import os

class GoAnalyzer:
    def __init__(self):
        self.query_config = {
            'function_query': """
                (function_declaration) @function
            """,
            'parameter_query': """
                (parameter_list
                    (parameter_declaration
                        name: (identifier)
                        type: (_))) @param
            """
        }
        self.parser, self.language = self.setup_parser()

    def setup_parser(self):
        language = Language(os.path.expanduser('~/.tree-sitter/tree-sitter-go.so'), 'go')
        parser = Parser()
        parser.set_language(language)
        return parser, language

    def analyze_function_signature(self, node):
        params = []
        return_type = 'void'

        # Handle parameters
        param_list = node.child_by_field_name('parameters')
        if param_list:
            for param in param_list.children:
                if param.type == 'parameter_declaration':
                    param_name = param.child_by_field_name('name').text.decode('utf8')
                    param_type = param.child_by_field_name('type').text.decode('utf8')
                    params.append(f"{param_name} {param_type}")

        # Handle return type
        result = node.child_by_field_name('result')
        if result:
            if result.type == 'type_identifier':
                return_type = result.text.decode('utf8')
            elif result.type == 'parameter_list':
                type_node = result.child_by_field_name('type')
                if type_node:
                    return_type = type_node.text.decode('utf8')

        return {
            'parameters': params,
            'return_type': return_type
        }

    def analyze_file(self, file_path):
        with open(file_path, 'rb') as file:
            content = file.read()

        tree = self.parser.parse(content)
        functions = []

        query = self.language.query(self.query_config['function_query'])
        captures = query.captures(tree.root_node)

        for node, _ in captures:
            name_node = node.child_by_field_name('name')
            if name_node:
                function_name = name_node.text.decode('utf8')
                print(f"Found function: {function_name}")
                signature = self.analyze_function_signature(node)
                functions.append({
                    'name': function_name,
                    'signature': signature,
                    'operations': self.analyze_operations(node)
                })

        return {
            'file': file_path,
            'functions': functions
        }

    def analyze_operations(self, node):
        operations = []
        if self.has_channel_operations(node):
            operations.append("Uses channels")
        if self.has_goroutines(node):
            operations.append("Launches goroutines")
        if self.has_defer_statements(node):
            operations.append("Uses defer")

        return " and ".join(operations) if operations else "Basic Go operations"

    def has_channel_operations(self, node):
        channel_query = self.language.query("""
            (channel_type) @channel
        """)
        return len(channel_query.captures(node)) > 0

    def has_goroutines(self, node):
        goroutine_query = self.language.query("""
            (go_statement) @goroutine
        """)
        return len(goroutine_query.captures(node)) > 0

    def has_defer_statements(self, node):
        defer_query = self.language.query("""
            (defer_statement) @defer
        """)
        return len(defer_query.captures(node)) > 0

# Test code
def test_go():
    analyzer = GoAnalyzer()
    test_file = 'test_files/test.go'
    result = analyzer.analyze_file(test_file)

    print("\nGo Analysis Results:")
    print("===================")
    for function in result['functions']:
        print(f"\nFunction: {function['name']}")
        print(f"Signature: {function['signature']}")
        print(f"Operations: {function['operations']}")

if __name__ == "__main__":
    test_go()
