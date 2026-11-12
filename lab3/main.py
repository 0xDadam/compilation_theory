import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:
    from lab1.scanner import Scanner
    from .parser import Mparser
    from . import TreePrinter
except ImportError:
    try:
        from lab1.scanner import Scanner
    except ImportError:
        from scanner import Scanner
    from parser import Mparser
    import TreePrinter


def main(filename):
    with open(filename, encoding="utf-8") as file:
        text = file.read()

    lexer = Scanner()
    parser = Mparser()
    tree = parser.parse(lexer.tokenize(text))
    if not parser.has_error and tree is not None:
        TreePrinter.printTree(tree)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} FILE")
    main(sys.argv[1])
