import subprocess
import shlex

print("initializing git repo")
subprocess.run(shlex.split("git init"), check=True)
print("installing dev dependencies in venv")
subprocess.run(shlex.split("uv sync"), check=True)
print("done!")
