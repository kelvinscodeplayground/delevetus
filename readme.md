# Delevetus

Delevetus is a command-line tool that helps to manage and delete files in a working directoty recursively. It provides
a simple way to delete files based on expiry, such as cleaning up files that have sitting for 7 days or more.

The goal of this project is to replace the previous [manage.rb](https://gist.github.com/kelvinchincc/bb07e3a643ed7bcb9c2646417d9b69d8) script that wrote in Ruby, which is now currently unmaintained and to migrate away
from Ruby stacks for better community support and maintainability.

## Installation

To install the Delevetus package, you can use uv tools (recommended) or pip. Make sure you have Python 3.15 or higher
installed.

## Features

- Recursively delete files in a directory based on expiry (e.g., files older than 7 days). Expiry is based on the last modified time of the file.
- Simple command-line interface to work with cron jobs or other automation tools.
- Unlike the previous Ruby script, Delevetus is a python package, so each machine have only one copy of the package installed, and to maintained.

### Using uv tools

```bash
uv tools install <link to delevetus package on github release page>
```

### Using pip

```bash
pip install <link to delevetus package on github release page>
```

## Usage

```python
delevetus --days 7 --path /path/to/directory
```

## License

Delevetus is licensed under the Mozilla Public License 2.0. See the [LICENSE](license.md) file for more information.
