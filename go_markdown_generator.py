import datetime
from pathlib import Path
import tree_sitter
from tree_sitter import Language, Parser
from typing import Dict, List
import os

class MarkdownGenerator:
    def __init__(self):
        self.parser, self.language = self.setup_parser()
        self.query = self.language.query("""
            (function_declaration
                name: (identifier) @function.name
                body: (block) @function.body) @function.declaration

            (method_declaration
                name: (field_identifier) @method.name
                body: (block) @method.body) @method.declaration

            (comment) @doc
        """)
        self.function_calls = {}  # Dictionary to store function call relationships
        self.function_info = {}   # Dictionary to store function information



    def setup_parser(self):
        LANGUAGE_PATH = os.path.expanduser('~/.tree-sitter/tree-sitter-go.so')
        language = Language(LANGUAGE_PATH, 'go')
        parser = Parser()
        parser.set_language(language)
        return parser, language

    def generate_markdown(self, project_path: str) -> str:
        project_files = list(Path(project_path).rglob("*.go"))

        # Generate markdown content
        md_content = [
            "# Go Project Analysis Report\n",
            f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
            "![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=flat&logo=go&logoColor=white)\n",
            "## Contents",
            "1. [Overview](#overview)",
            "2. [Function Relationships](#function-relationships)",
            "3. [Code Analysis](#code-analysis)\n",
            f"## Overview\nTotal files analyzed: {len(project_files)}\n",
            "## Function Relationships\n"
        ]

        # Analyze each file
        for file_path in project_files:
            file_content = self._analyze_file(file_path)
            if file_content:
                md_content.append(f"### File: `{file_path.relative_to(project_path)}`\n")
                md_content.append(file_content)

        # Generate call stack visualizations
        md_content.append("## Call Stack Visualization\n")
        md_content.append("```mermaid\nflowchart TD\n")
        for caller, callees in self.function_calls.items():
            for callee in callees:
                md_content.append(f"    {caller} --> {callee}\n")
        md_content.append("```\n")

        return "\n".join(md_content)

    def _analyze_file(self, file_path: Path) -> str:
        with open(file_path, 'rb') as f:
            content = f.read()

        tree = self.parser.parse(content)
        root = tree.root_node

        md_content = []

        # Find all function declarations
        for node in self._traverse_tree(root):
            if node.type == 'function_declaration':
                func_info = self._extract_function_info(node, file_path)
                if func_info:
                    md_content.append(self._format_function_info(func_info))

        return "\n".join(md_content)

    def _extract_function_info(self, node, file_path) -> Dict:
        name_node = next((c for c in node.children if c.type == 'identifier'), None)
        if not name_node:
            return None

        func_name = name_node.text.decode('utf-8')

        # Get clean signature using the new method
        signature = self.get_function_signature(node)

        # Get function documentation
        doc_comment = self._get_doc_comment(node)

        # Analyze dependencies
        dependencies = self._analyze_dependencies(node)
        # Add operations analysis here
        operations = self.analyze_operations(node)
        return {
            'name': func_name,
            'signature': signature,
            'doc': doc_comment,
            'operations': operations,
            'dependencies': dependencies,
            'file_path': file_path
        }



    def _format_function_info(self, func_info: Dict) -> str:
        md = [
            f"#### Function: `{func_info['name']}`",
            f"**Signature:** `{func_info['signature']}`\n",
            "**Documentation:**",
            f"```go\n{func_info['doc']}\n```\n",
            "**Operations:**",
            f"```go\n{func_info['operations']}\n```\n",
            "<details>",
            "<summary>Dependencies</summary>\n"
        ]

        if func_info['dependencies']['calls']:
            for call in func_info['dependencies']['calls']:
                md.append(f"- `{call}`")
        else:
            md.append("- No outgoing calls")

        md.append("\n#### Called By:")
        if func_info['dependencies']['called_by']:
            for caller in func_info['dependencies']['called_by']:
                md.append(f"- `{caller}`")
        else:
            md.append("- No incoming calls")

        md.append("</details>\n")
        return "\n".join(md)

    def _analyze_dependencies(self, node) -> Dict:
        calls = set()
        for child in self._traverse_tree(node):
            if child.type == 'call_expression':
                func_name = child.children[0].text.decode('utf-8')
                calls.add(func_name)

        return {
            'calls': list(calls),
            'called_by': []  # Will be populated later
        }

    def _get_doc_comment(self, node) -> str:
        prev_sibling = node.prev_sibling
        if prev_sibling and prev_sibling.type == 'comment':
            return prev_sibling.text.decode('utf-8')
        return "No documentation available"

    def _traverse_tree(self, node):
        yield node
        for child in node.children:
            yield from self._traverse_tree(child)

    def get_function_signature(self, node):
        # Get the function name and parameters
        name_node = next(c for c in node.children if c.type == 'identifier')
        param_list = next(c for c in node.children if c.type == 'parameter_list')
        result = next((c for c in node.children if c.type == 'result'), None)

        # Build the signature
        func_name = name_node.text.decode('utf-8')
        params = param_list.text.decode('utf-8')
        return_type = result.text.decode('utf-8') if result else ""

        # Format as: func name(params) return_type
        signature = f"func {func_name}{params}"
        if return_type:
            signature += f" {return_type}"

        return signature

    def analyze_operations(self, node):
        operation_patterns = {
            'test': {'pattern': '(call_expression function: (identifier) @test)',
                    'description': 'Performs unit testing'},
            'http': {'pattern': '(selector_expression field: (field_identifier) @http)',
                    'description': 'Makes HTTP requests'},
            'json': {'pattern': '(call_expression function: (identifier) @json)',
                    'description': 'Handles JSON data'},
            'goroutine': {'pattern': '(go_statement)',
                         'description': 'Uses concurrent execution'},
            'file': {'pattern': '(call_expression function: (identifier) @file)',
                    'description': 'Performs file operations'}
        }

        detected_ops = []
        for op_type, op_info in operation_patterns.items():
            try:
                query = self.language.query(op_info['pattern'])
                captures = query.captures(node)
                if captures:
                    detected_ops.append(op_info['description'])
            except:
                continue

        return " and ".join(detected_ops) if detected_ops else "Basic function operations"

