"""Check the Python devcontainer environment as the vscode user."""

import os
import sys
import tempfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
venv = Path("/home/vscode/.venv")
assert Path(sys.prefix) == venv, f"Wrong Python environment: {sys.prefix}"
assert os.getuid() != 0, "Run this check as vscode"
assert os.access(venv, os.W_OK), "Virtual environment is not writable"
with tempfile.TemporaryFile(dir=root) as handle:
    handle.write(b"Workspace writes work")
print(
    "Python environment, non-root workspace writes, and virtual environment permissions: OK"
)
