# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.undos

def __init__(*args: Any, **kwargs: Any): ...
def areEnabled() -> bool:
    """areEnabled() -> bool

    Returns True is undos are currently enabled."""

def disabler() -> hou.UndosDisabler:
    """disabler() -> hou.UndosDisabler

      Returns a context manager, within which changes to Houdini will not
      be added to the undo stack.

      For example:

    > with hou.undos.disabler():
    >     # Move all object nodes 1 unit to the left.
    >     # This cannot be undone!
    >     for n in hou.node(\"/obj\").children():
    >         n.move(hou.Vector2(-1, 0))"""

def group(label: str, editor: Optional[hou.NetworkEditor] = None) -> hou.UndosGroup:
    """group(label, editor=None) -> hou.UndosGroup

      Returns a context manager, within which all changes to Houdini are
      recorded as a single action on the undo stack.

      For example:

    > with hou.undos.group(\"Move all nodes to the left\"):
    >     # Move all object nodes 1 unit to the left.
    >     # This is
    >     for n in hou.node(\"/obj\").children():
    >         n.move(hou.Vector2(-1, 0))

      This has no effect when run inside parameter callback scripts
      because they are already executed within an undo group.

      The optional editor argument is a hou.NetworkEditor object should be
      used when the undo group is being created as part of executing an
      action inside a Network View pane that might contain APEX Nodes.
      This ensures that edits to the APEX graph are only saved to the
      current SOP when all operations inside the undo group have been
      completed."""

def removeUndos(tag: str) -> None:
    """removeUndos(tag)

      Invalidates and removes all undo and redo events that are tagged
      with tag.

    > # Removes all undos with the tag \"myTag\"
    > hou.undos.removeUndos(\"myTag\")"""

def clear() -> None:
    """clear()

    Clear all undo and redo information."""

def memoryUsage() -> int:
    """memoryUsage() -> int

    The current memory used (in bytes) for undos."""

def memoryUsageLimit() -> int:
    """memoryUsageLimit() -> int

    The maximum allowed memory usage size (in bytes) for undos."""

def performUndo() -> bool:
    """performUndo()

    Undo the last action."""

def performRedo() -> bool:
    """performRedo()

    Redo the last undoed action."""

def undoLabels() -> list[str]:
    """undoLabels() -> tuple of str

    Provides a tuple of the undo operations currently on the stack. Note
    that the first item (ie. undoLabels()) is the next operation that
    will be undone."""

def redoLabels() -> list[str]:
    """redoLabels() -> tuple of str

    Provides a tuple of the redo operations currently on the stack. Note
    that the first item (ie. redoLabels()) is the next operation that
    will be redone."""

def add(undo: Any, label: str, tag: Optional[str] = None) -> None:
    """add(undo, label, tag=None)

      Add an undo operation to the undo history. undo must be an object
      with undo() and redo() methods. The undo() method is executed when
      the operation is undone and the redo() method is executed when the
      operation is redone.

      label is a description of the undo operation as it appears in the
      undo history.

      A hou.OperationFailed is raised if the undo object passed in does
      not have an undo() method or a redo() method.

      For example, a valid python object passed to this function would
      look like:

    > class MyUndoClass():
    >
    >     def __init__(self):
    >         # ... Initialization ...
    >         pass
    >
    >     def undo(self):
    >         # Add in what needs to be done on undo
    >         pass
    >
    >     def redo(self):
    >         # Add in what needs to be done on redo
    >         pass

      Using the above class, a call to this function would look like:

    > foo = MyUndoClass()
    > hou.undos.add(foo, \"My Undo\")

      An optional string tag can also be set for this undo object, which
      will allow it to be removed from the undo stack using
      hou.undos.removeUndos.

    > foo = MyUndoClass()
    > hou.undos.add(foo, \"My Undo\", \"myTag\")"""
