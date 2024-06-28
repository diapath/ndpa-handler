from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("ndpa_handler")
except PackageNotFoundError:
    __version__ = "dev"

from .core import Annotation