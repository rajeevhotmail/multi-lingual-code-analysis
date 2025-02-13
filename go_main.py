import argparse
from go_markdown_generator import MarkdownGenerator
from code_reader import CodeReader

def main():
    parser = argparse.ArgumentParser(description='Generate Go code documentation')
    parser.add_argument('--project-dir', help='Path to the project directory')
    parser.add_argument('--github-url', help='GitHub repository URL')
    args = parser.parse_args()

    reader = CodeReader()

    if args.github_url:
        project_path = reader.clone_repository(args.github_url)
    else:
        project_path = args.project_dir

    generator = MarkdownGenerator()
    markdown = generator.generate_markdown(project_path)

    with open('go_project_analysis.md', 'w') as f:
        f.write(markdown)

    print("Documentation generated successfully in project_analysis.md")

if __name__ == "__main__":
    main()
