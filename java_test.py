from multi_language_analyzer import MultiLanguageAnalyzer
import sys

def test_java():
    analyzer = MultiLanguageAnalyzer()
    file_path = 'test_files/Test.java'

    print(f"\nAnalyzing Java file: {file_path}")
    result = analyzer.analyze_file(file_path)

    if result:
        print("\nAnalysis Results:")
        for function in result['functions']:
            print(f"\nMethod: {function['name']}")
            print(f"Signature: {function['signature']}")
            print(f"Operations: {function['operations']}")

if __name__ == "__main__":
    test_java()
