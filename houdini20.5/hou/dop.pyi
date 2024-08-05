# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.dop

def __init__(*args: Any, **kwargs: Any): ...
def isScriptSolverRunning() -> bool:
    """isScriptSolverRunning() -> bool

    Return whether or not a Python script solver DOP is currently
    running.

    This function is called from the Python code that is automatically
    generated when you create a new Python solver DOP type."""

def scriptSolverData() -> hou.DopData:
    """scriptSolverData() -> hou.DopData

    Return the solver solver data corresponding to the currently running
    Python script solver DOP.

    A Python script solver DOP runs in two passes. During the first
    pass, it evaluates its node parameters and stores them in the solver
    data. During this pass, hou.dop.isScriptSolverRunning returns False
    and you can access a writable version of the script solver data with
    hou.DopNode.pythonSolverData. During the second pass the solver is
    invoked to actually solve the objects. During this pass,
    hou.dop.isScriptSolverRunning returns True and you use this function
    to access a read-only version of the script solver data. You can
    access the objects being solved in this pass with
    hou.dop.scriptSolverNewObjects and hou.dop.scriptSolverObjects.

    DOP nodes attach data named Solver to each of the DOP objects being
    solved. If the only solver in use is the script solver, this data
    will be of type SIM_SolverScript. Otherwise, this data will be of
    type SIM_SolverMulti, and the SIM_SolverScript will be subdata of
    the multisolver data. This function provides an easy way of
    retrieving this data, regardless of where it exists.

    Typically, the solver data is shared between all the objects being
    solved. For this reason, the data returned by this function is read-
    only. Otherwise, if you modified this data, the DOP engine would
    copy it and the objects being solved would not share this data."""

def scriptSolverNetwork() -> hou.Node:
    """scriptSolverNetwork() -> hou.OpNode or None

    Return the DOP network node that contains the script solver DOP that
    is currently running, or None if not script solver is running. You
    would call this function from a script solver DOP."""

def scriptSolverSimulation() -> hou.DopSimulation: ...
def scriptSolverObjects() -> list[hou.DopData]:
    """scriptSolverObjects() -> tuple of hou.DopObject

    Return a tuple of DOP objects being solved by the current script
    solver DOP. If no script solver is running, returns an empty tuple."""

def scriptSolverNewObjects() -> list[hou.DopData]:
    """scriptSolverNewObjects() -> tuple of hou.DopObject

    Return a tuple of newly-created DOP objects to later be solved by
    the current script solver DOP. If no script solver is running,
    returns an empty tuple."""

def scriptSolverTimestepSize() -> float:
    """scriptSolverTimestepSize() -> float

    Return the timestep size for the script solver that is currently
    running, or 0.0 if no script solver is running."""

def scriptSolverTime() -> float: ...
