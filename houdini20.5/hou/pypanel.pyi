# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.pypanel

def __init__(*args: Any, **kwargs: Any): ...
def installFile(file_path: str) -> None:
    """installFile(file_path)

    Install all the Python Panel interfaces defined in the given
    .pypanel file into the current Houdini session.


    file_path
        The .pypanel file to load."""

def interfacesInFile(file_path: str) -> list[hou.PythonPanelInterface]:
    """interfacesInFile(file_path) -> tuple of hou.PythonPanelInterface

    Return all the Python Panel interface definitions inside the given
    .pypanel file. See hou.PythonPanelInterface for more information.

    Raises hou.OperationFailed if file_path does not refer to a valid
    .pypanel file."""

def interfaces() -> dict[str, hou.PythonPanelInterface]:
    """interfaces() -> dict of str to hou.PythonPanelInterface

    Return all the Python Panel interface definitions currently
    installed. Returns a dictionary mapping interface names to
    corresponding hou.PythonPanelInterface instances.

    See hou.PythonPanelInterface for more information."""

def interfaceByName(name: str) -> hou.PythonPanelInterface:
    """interfaceByName(name) -> hou.PythonPanelInterface

    Return the Python Panel interface definition that corresponds to the
    given interface name.

    Return None if no such interface definition exists."""

def setMenuInterfaces(names: tuple[str]) -> None:
    """setMenuInterfaces(names)

    Set the Python Panel drop-down menu to the list of interface names.
    Note that __separator__ is a valid name to indicate a separator in
    the list.

    Raises hou.OperationFailed if names contains interfaces that are not
    installed"""

def menuInterfaces() -> list[str]:
    """menuInterfaces() -> tuple of str

    Return a tuple of the names of the interfaces currently shown in the
    Python Panel drop-down menu."""
