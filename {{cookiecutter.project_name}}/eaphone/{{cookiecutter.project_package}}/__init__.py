from loguru import logger

from .version import __version__

logger.disable("eaphone.{{ cookiecutter.project_package }}")

__all__ = [
    "__version__",
]
