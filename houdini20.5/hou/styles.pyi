# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.styles

def __init__(*args: Any, **kwargs: Any): ...
def hasStyle(name: str) -> bool:
    """hasStyle(name) -> bool

    Returns true if there is a style with the specified name."""

def styles(pattern: Optional[str] = None) -> list[str]:
    """styles() -> tuple of str

    Return a tuple containing the names of all styles in the style
    manager."""

def description(style: str) -> str:
    """description(name) -> str

    Returns the description associated with the named style. If there is
    no style with the provided name, an empty string is returned."""

def stylesheet(style: str) -> str:
    """stylesheet(name) -> str

    Returns the style sheet text associated with the named style. If
    there is no style with the provided name, an empty string is
    returned."""

def errors(style: str) -> str:
    """errors(name) -> str

    Returns any error messages generated while parsing the named style.
    If there is no style with the provided name, an empty string is
    returned."""

def addStyle(name: str, description: str, stylesheet: str) -> None:
    """addStyle(name, description, stylesheet)

    Create a new named style. If a style sheet with the supplied name
    already exists, it will be overwritten with the new values.


    name
        A unique name that will be used to identify the style sheet.
        Follows the same naming limitations as node names (no spaces, no
        slashes, etc).

    description
        An arbitrary string that can optionally be used to identify the
        purpose of this style sheet.

    stylesheet
        The style sheet definition expressed as a string in JSON format."""

def renameStyle(old_name: str, new_name: str) -> None:
    """renameStyle(old_name, new_name)

    Changes the name of an existing style sheet. If there is no style
    with the provided old_name, or there is already a style with the
    provided new_name, an exception will be generated. References to
    this style sheet in the hip file will be automatically updated to
    refer to the new name."""

def reorderStyles(names: tuple[str]) -> None:
    """reorderStyles(names)

    Changes the order of the style sheets defined in the hip file. This
    order determines the order of the style names returned by the styles
    function. This in turn may affect the final material assignments in
    a mantra render, since priority is given to style sheets listed last
    in the Apply Style Sheets parameter of the ROP.


    names
        A tuple of strings which must contain exactly the same set of
        strings returned by the styles function, but in a different
        order. If the set of strings do not match, this function raises
        a ValueError."""

def removeStyle(name: str) -> None:
    """removeStyle(name)

    Deletes an existing style sheet."""

def removeAll() -> None:
    """removeAll()

    Deletes all existing style sheets."""
