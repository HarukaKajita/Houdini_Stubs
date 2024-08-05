# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.shelves

def __init__(*args: Any, **kwargs: Any): ...
def shelfSets() -> dict[str, hou.ShelfSet]:
    """shelfSets() -> dict of str to hou.ShelfSet

    Returns a dictionary mapping the internal name of every known shelf
    tab to a corresponding hou.Shelf object."""

def shelves() -> dict[str, hou.Shelf]:
    """shelves() -> dict of str to hou.Shelf

    Returns a dictionary mapping the internal name of every known shelf
    tab to a corresponding hou.Shelf object."""

def tools() -> dict[str, hou.Tool]:
    """tools() -> dict of str to hou.Tool

    Returns a dictionary mapping the internal name of every known tool
    to a corresponding hou.Tool object.


    NOTE
        If you only want to get a single tool by its internal name, use
        the tool function. Using shelves.tool(name) is much faster that
        constructing this dictionary and then pulling a single tool out
        of it."""

def tool(tool_name: str) -> hou.Tool:
    """tool(tool_name) -> hou.Tool or None

      Gets a reference to a hou.Tool by its internal name.

    > >>> hou.shelves.tool(\"geometry_sphere\")
    > <hou.Tool 'geometry_sphere'>"""

def isToolDeleted(tool_name: str) -> bool: ...
def loadFile(file_path: str) -> None:
    """loadFile(file_path)

    Reads a shelf file and adds any shelves and tools defined in that
    file to Houdini."""

def reloadShelfFiles() -> None:
    """reloadShelfFiles()

    Reloading the shelf files found in the search path and update the
    shelf UI with any changed information."""

def runningTool() -> hou.Tool:
    """runningTool() -> hou.Tool or None"""

def beginChangeBlock() -> None:
    """beginChangeBlock()

      Prevents Houdini from automatically rewriting shelf information
      files until endChangeBlock is called.

      Normally, many shelf editing functions and methods cause Houdini to
      rewrite the shelf definition files with the new information. If
      you're changing a lot of shelves/tools at once, it could be quite
      slow as each individual change is written separately.

      To speed up batch changes, call beginChangeBlock() first, then
      perform the edits, then call endChangeBlock(). This delays rewriting
      the shelf files until the end when all changes are written at once.

    > # Change the icon of every tool to MISC_angry_fruit_salad.
    > # DON'T ACTUALLY DO THIS!
    >
    > # First, turn off writing changes
    > hou.shelves.beginChangeBlock()
    >
    > for shelf in hou.shelves.shelves().values():
    >     for tool in shelf.tools():
    >         tool.setIcon(\"MISC/angry_fruit_salad\")
    >
    > # Finish the change block and write all the changes to disk
    > hou.shelves.endChangeBlock()

      Each call to beginChangeBlock must have a matching call to
      endChangeBlock or Houdini will never actually write your changes to
      disk."""

def endChangeBlock() -> None:
    """endChangeBlock()

    See beginChangeBlock above."""

def newShelfSet(
    file_path: Optional[str] = None, name: Optional[str] = None, label: Optional[str] = None
) -> hou.ShelfSet:
    """newShelfSet(file_path=None, name=None, label=None) -> hou.ShelfSet

    Returns a new hou.ShelfSet object using the provided options. You
    must use this function to create new shelf sets, you can't
    instantiate the ShelfSet class directly."""

def newShelf(file_path: Optional[str] = None, name: Optional[str] = None, label: Optional[str] = None) -> hou.Shelf:
    """newShelf(file_path=None, name=None, label=None) -> hou.Shelf

    Returns a new hou.Shelf object using the provided options. You must
    use this function to create new shelf tabs, you can't instantiate
    the Shelf class directly."""

def newTool(*args: Any, **kwargs: Any) -> hou.Tool:
    """newTool(file_path=None, name=None, label=None, script=None,
    language=hou.scriptLanguage.Python, icon=None, help=None, help_url=None,
    network_categories=(), viewer_categories=(), cop_viewer_categories=(),
    network_op_type=None, viewer_op_type=None, locations=(),
    hda_definition=None) -> hou.Tool

        Returns a new hou.Tool object using the provided options. You must
        use this function to create new shelf tabs, you can't instantiate
        the Tool class directly."""

def _newAssetTool(
    name: Optional[str] = None,
    label: Optional[str] = None,
    icon: Optional[str] = None,
    help: Optional[str] = None,
    help_url: Optional[str] = None,
) -> hou.Tool: ...
def defaultFilePath() -> str:
    """defaultFilePath() -> str"""

def defaultToolName(nodetype_category_name: str, nodetype_name: str) -> str: ...
