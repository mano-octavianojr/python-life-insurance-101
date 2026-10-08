"""Validate notebook structure and run every lesson in an independent kernel."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["Story opening", "Learning goals", "Insurance in everyday words", "Python toolbox", "Predict, then run", "Your turn", "Hint", "Sample solution", "Check your results", "Story ending", "Exit ticket"]

def main():
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    assert len(notebooks) == 10, "Expected ten lessons"
    output = ROOT / ".validation"
    output.mkdir(exist_ok=True)
    total = 0
    for path in notebooks:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        prose = "\n".join(cell.source for cell in notebook.cells if cell.cell_type == "markdown")
        assert all("## " + heading in prose for heading in REQUIRED), path.name
        assert "fictional" in prose.lower() and "Maya" in prose and "Leo" in prose
        NotebookClient(notebook, timeout=120, kernel_name="python3", resources={"metadata": {"path": str(path.parent)}}).execute()
        cells = [cell for cell in notebook.cells if cell.cell_type == "code"]
        assert all(cell.execution_count is not None for cell in cells)
        assert not any(result.output_type == "error" for cell in cells for result in cell.outputs)
        if path.name.startswith("09_"):
            assert any("image/png" in result.get("data", {}) for cell in cells for result in cell.outputs), "Missing rendered chart"
        nbformat.write(notebook, output / path.name)
        total += len(cells)
        print(f"PASS {path.name}: {len(cells)} code cells", flush=True)
    print(f"Validated {len(notebooks)} notebooks and {total} code cells. Executed copies: {output}")

if __name__ == "__main__":
    main()
