# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.properties

def __init__(*args: Any, **kwargs: Any): ...
def classes(*args: Any) -> list[str]:
    """classes(tags=None) -> tuple of str

    Returns a list of render property classes. If the tags argument is
    provided, only those classes that match the provided tag expression
    will be returned."""

def classLabel(class_name: str) -> str:
    """classLabel(class_name) -> str

    Returns the descriptive label for the provided render property
    class."""

def categories(class_name: str) -> list[str]:
    """categories(class_name) -> tuple of str

    Returns the property categories in the provided render property
    class."""

def parameters(class_name: str, category_name: str) -> list[str]:
    """parameters(class_name, category_name) -> tuple of str

    Returns the names of all parameters under the category within the
    provided render property class."""

def parmTemplate(class_name: str, parm_name: str) -> hou.ParmTemplate:
    """parmTemplate(class_name, parm_name) -> hou.ParmTemplate

    Returns an object that represents the template for the specified
    render property parameter. This parameter may be a folder parameter
    if several parameters are intended to be added as a group."""
