# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.takes

def __init__(*args: Any, **kwargs: Any): ...
def takes() -> list[hou.Take]:
    """takes() -> tuple of hou.Take

    Return a tuple of all the takes in the scene."""

def currentTake() -> hou.Take:
    """currentTake() -> hou.Take

    Return the current take."""

def setCurrentTake(take: hou.Take) -> None:
    """setCurrentTake(take)

    Set the current take to the specified take.

    Raise hou.OperationFailed if the take argument is None."""

def rootTake() -> hou.Take:
    """rootTake() -> hou.Take

    Return the main (master) take."""

def findTake(take_name: str) -> hou.Take:
    """findTake(take_name) -> hou.Take or None

    Return the take with the specified name or None if no such take
    exists."""

def defaultTakeName() -> str:
    """defaultTakeName()

    Return the default take name used for new takes. The default name
    acts like a prefix since new takes will contain the default name
    plus a numerical suffix in their take names."""

def setDefaultTakeName(default_name: str) -> None:
    """setDefaultTakeName()

    Sets the default take name. The default take name is used as a
    prefix for the names of new takes."""
