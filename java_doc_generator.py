from document_generator import DocumentationGenerator
from java_analyzer import JavaAnalyzer
import os
import argparse
import git
from urllib.parse import urlparse

def clone_github_repo(github_url, target_dir):
    repo_name = urlparse(github_url).path.split('/')[-1]
    local_path = os.path.join(target_dir, repo_name)
    if not os.path.exists(local_path):
        git.Repo.clone_from(github_url, local_path)
    return local_path

def generate_java_documentation(project_dir):
    # Initialize analyzers
    java_analyzer = JavaAnalyzer()
    doc_generator = DocumentationGenerator()

    # Use analyze_project to get all results
    results = java_analyzer.analyze_project(project_dir)
    call_stacks = {}

    # Build call stacks for each method
    for result in results:
        for method in result['functions']:
            call_stacks[method['name']] = java_analyzer.analyze_call_stack(method['name'], results)

    # Generate documentation with both results and call stacks
    doc_generator.generate_docs(results, call_stacks)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate Java documentation')
    parser.add_argument('--project-dir', type=str, help='Directory containing Java files')
    parser.add_argument('--github-url', type=str, help='GitHub repository URL')
    args = parser.parse_args()

    if args.github_url:
        project_dir = clone_github_repo(args.github_url, 'repos')
    else:
        project_dir = args.project_dir if args.project_dir else 'test_files'

    generate_java_documentation(project_dir)
