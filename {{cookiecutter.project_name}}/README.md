# {{cookiecutter.project_name}}
{{cookiecutter.project_description}}

## Usage

Write usage example here (will be tested by doccheck):
```python
>>> from {{cookiecutter.project_name}} import add_two
>>> print(add_two(1,1))
2

```

## Requirements

- Python 3.9+

## Development

For testing and linting, setup the extra dependencies in a virtual environment using [uv](https://docs.astral.sh/uv/):
```
uv sync --extra dev
```


Activate the virtual environment (bash compatible on linux):
```bash
source .venv/bin/activate
```
Activate the virtual environment (powershell compatible on windows):
```bash
. .venv/Scripts/activate
```

You can run checks (linting, type checking, and tests) with `poe check`. 

## License

This project is licensed under the MIT License - see the LICENSE file for details.
