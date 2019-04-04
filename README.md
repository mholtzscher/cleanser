# cleanser

<p>
  <a href="https://badge.fury.io/py/cleanser"><img src="https://badge.fury.io/py/cleanser.svg" alt="PyPI version"></a>
  <a href="https://mholtzscher.visualstudio.com/cleanser/_build"><img src="https://mholtzscher.visualstudio.com/cleanser/_apis/build/status/cleanser-CI?branchName=master" alt="Azure Pipelines"></a>
  <a href="https://github.com/mholtzscher/cleanser"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black"></a>
  <a href="https://codecov.io/gh/mholtzscher/cleanser">
  <img src="https://codecov.io/gh/mholtzscher/cleanser/branch/master/graph/badge.svg" alt="Codecov"/></a>
</p>

Utilities for cleaning text for NLP and other workflows.
 
## Installation

```
pip install cleanser
```

## Usage
```
from cleanser import Cleanser

text = """Hello World....

😺😺 Python is 👌😀😀 awesome  
"""

Cleanser(text).emoji().double_punctuation().whitespaces().text
>>> "Hello World. Python is awesome"
```

# Contributing

#### Setup
1. Install [Poetry](https://poetry.eustace.io/)
1. Run `make setup` to prepare workspace

#### Testing
1. Run `make test` to run all tests

#### Linting and Formatting
1. Run `make format` to run black code formatter
1. Run `make lint` to run pylint
1. Run `make mypy` to run mypy