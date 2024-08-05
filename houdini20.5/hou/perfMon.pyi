# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.perfMon

def __init__(*args: Any, **kwargs: Any): ...
def startProfile(title: str, options: Optional[hou.PerfMonRecordOptions] = None) -> hou.PerfMonProfile:
    """startProfile(title, options=None) -> hou.PerfMonProfile

    Create a new profile and start it so that it can record events. When
    the profile is stopped, it will generate statistics for the events
    that it recorded.


    options
        A hou.PerfMonRecordOptions object that specifies the types of
        Houdini events and statistics to record. If None is passed in or
        if the options argument is not specified, then the profile will
        record all events and statistics."""

def loadProfile(file_path: str) -> hou.PerfMonProfile:
    """loadProfile(file_path) -> hou.PerfMonProfile

    Load a profile from disk and return the loaded profile.

    Raises hou.OperationFailed if file_path points to a file that does
    not exist or is not a valid Houdini performance monitor profile
    file."""

def saveProfile(profile: hou.PerfMonProfile, file_path: str) -> None:
    """saveProfile(profile, file_path)

    Save the profile to disk.

    Raises hou.OperationFailed if the profile is still active or if the
    file could not be written to disk (i.e. permission problems)."""

def activeProfile() -> hou.PerfMonProfile:
    """activeProfile() -> hou.PerfMonProfile or None

    Return the profile currently visible in the performance monitor
    pane, or"""

def startTimedEvent(description: str, auto_nest_events: bool = True) -> hou.PerfMonEvent:
    """startTimedEvent(description, auto_nest_events=True) -> hou.PerfMonEvent

    This method is deprecated in favor of startEvent."""

def startEvent(description: str, auto_nest_events: bool = True) -> hou.PerfMonEvent:
    """startEvent(description, auto_nest_events=True) -> hou.PerfMonEvent

    Create a generic event and start it. When the event is stopped, it
    will be logged by the performance monitor and added to any profiles
    that are recording script or memory statistics.

    Use this function to time and measure memory growth in generic
    scripts, functions or code blocks.

    Return the new event.


    description
        The description of the event that you are starting. For example,
        this can be a function name or a script name or a description of
        a code block.

    auto_nest_events
        If set to True, the event will automatically 'nest' other events
        that are started and stopped while this event is running. When
        the event is stopped, it will decrement the times and memory of
        its nested events from its total time and memory. That way, the
        event's total time and memory will reflect the work performed in
        the event itself and not in any of its nested events.

    Raises hou.OperationFailed if description is an empty string."""

def startTimedCookEvent(description: str, node: hou.Node) -> hou.PerfMonEvent:
    """startTimedCookEvent(description, node) -> hou.PerfMonEvent

    This method is deprecated in favor of startCookEvent."""

def startCookEvent(description: str, node: hou.Node) -> hou.PerfMonEvent:
    """startCookEvent(description, node) -> hou.PerfMonEvent

    Create an event that is related to node cooking and start it. When
    the event is stopped, it will be logged by the performance monitor
    and added to any profiles that are recording cook or memory
    statistics.

    Use this function to time code blocks and measure memory growth in
    the Code section of Python operators.

    Return the cook event.


    description
        The description of the event that you are timing. For example,
        this can be a function name or a description of a code block.

    node
        The node that the timed event applies to. This must be a
        hou.OpNode object. When calling startCookEvent() from within the
        Code section of a Python operator, set node to the current node
        (i.e. hou.pwd()).

    Raises hou.OperationFailed if description is an empty string or if
    node does not exist."""

def startPaneEvent(panetype: str, operation: str) -> hou.PerfMonEvent:
    """startPaneEvent(panetype, operation) -> hou.PerfMonEvent

    Create an event that is related to the operation of a scriped pane
    and start it. When the event is stopped, it will be logged by the
    performance monitor and added to any profiles that are recording
    cook or memory statistics.

    Use this function to time code blocks and measure memory growth in
    the code for python panels.

    Return the cook event.


    panetype
        A description of the python panel running this code.

    operation
        The specific operation being timed by this event.

    Raises hou.OperationFailed if either panetype or operation are empty
    strings."""

def isRecording() -> bool:
    """isRecording() -> bool

    Return True if the performance monitor is recording Houdini events."""
