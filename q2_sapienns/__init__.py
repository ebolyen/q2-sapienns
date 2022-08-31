# flake8: noqa

from . import _version
__version__ = _version.get_versions()['version']

from .plugin_setup import (
    HumannGeneFamilyDirectoryFormat, HumannGeneFamilyFormat,
    HumannPathAbundanceDirectoryFormat, HumannPathAbundanceFormat,
    MetaphlanMergedAbundanceDirectoryFormat, MetaphlanMergedAbundanceFormat,
    MetaphlanMergedAbundanceTable, HumannPathAbundanceTable,
    HumannGeneFamilyTable
)
