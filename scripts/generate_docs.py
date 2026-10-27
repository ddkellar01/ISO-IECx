"""Automated documentation index generator for ISO-IECx modules."""
from pathlib import Path

def generate_markdown_docs():
    root = Path(__file__).resolve().parent.parent
    docs_path = root / "DOCUMENTATION.md"
    
py_files = list(root.glob("**/*.py"))
    
    content = "# ISO-IECx Auto-Generated Code Index\n\n"
    content += f"Total Python modules tracked: {len(py_files)}\n\n"
    content += "## Modules\n"
    
    for file in sorted(py_files):
        rel_path = file.relative_to(root)
        if "venv" not in str(rel_path) and ".git" not in str(rel_path):
            content += f"- `{rel_path}`\n"
            
    docs_path.write_text(content)
    print(f"Documentation index generated at {docs_path}")

if __name__ == "__main__":
    generate_markdown_docs()
