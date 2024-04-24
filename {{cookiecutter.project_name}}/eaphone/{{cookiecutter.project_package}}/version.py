from __future__ import annotations

from sys import version_info

if version_info < (3, 10):
    # compatibility for python <3.10
    from importlib_metadata import version
else:
    from importlib.metadata import version

__version__ = version("{{ cookiecutter.project_full_package }}")
