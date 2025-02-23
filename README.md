# Simple cookiecutter template
This is a simple cookiecutter template for python projects with the following features:
 - simple setup
 - standard package structure
 - dev environment and CI included

 It is compatible with both windows and linux.

## Usage

Ensure you have cookiecutter, git, and uv installed. See [uv](https://docs.astral.sh/uv/) for install instructions.

You can make a new project based on this repository:
```bash
uvx cookiecutter https://github.com/MathanGeurtsen/simple_cookiecutter
```

Once cookiecutter has ran, activate the new virtual environment with:

bash compatible on linux:
```bash
source .venv/bin/activate
```
powershell compatible on windows:
```bash
. .venv/Scripts/activate
```

You can run checks (linting, type checking, and tests) with `poe check`. 

## Requirements

- cookiecutter
- uv 
- git

## License

This project is licensed under the MIT License - see the LICENSE file for details.
