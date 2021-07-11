from pathlib import Path

path = Path("ecommerce")

# path.exists()
# path.mkdir()
# path.rmkdir()
# path.rename("ecommerce2")

paths = [p for p in path.iterdir() if p.is_dir()]

py_files = [p for p in path.rglob("*.py")]
print(py_files)
