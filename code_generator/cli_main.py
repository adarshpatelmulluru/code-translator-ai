import argparse
from pathlib import Path
from .translate_anlyz import translate_code, analyze_code

def main():
    parser = argparse.ArgumentParser(
        description="Universal Code Translator and Analyzer",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  # Translate C++ to Rust and analyze source
  python -m code_translator --translate app.cpp app.rs
  
  # Analyze a Java file
  python -m code_translator --analyze Main.java
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--translate', nargs=2, metavar=('SOURCE', 'DEST'),
                     help='Translate source file to destination language')
    group.add_argument('--analyze', metavar='SOURCE',
                     help='Analyze source code and generate report')
    
    args = parser.parse_args()
    
    if args.translate:
        source, dest = args.translate
        if not translate_code(source, dest):
            exit(1)
    elif args.analyze:
        if not analyze_code(args.analyze):
            exit(1)

if __name__ == "__main__":
    main()