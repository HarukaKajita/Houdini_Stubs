# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.playbar

def __init__(*args: Any, **kwargs: Any): ...
def isPlaying() -> bool:
    """isPlaying(self) -> bool

    Return True if the playbar is playing. Return False otherwise."""

def play() -> None:
    """play(self)

    Play in the forward direction.

    Raises hou.NotAvailable if the playbar is not available."""

def stop() -> None:
    """stop(self)

    Stop playing.

    Raises hou.NotAvailable if the playbar is not available."""

def reverse() -> None:
    """reverse(self)

    Play in the reverse direction.

    Raises hou.NotAvailable if the playbar is not available."""

def jumpToNextKeyframe() -> None: ...
def jumpToPreviousKeyframe() -> None: ...
def playMode() -> hou.EnumValue:
    """playMode(self) -> hou.playMode

    Return the playbar's play mode.

    Raises hou.NotAvailable if the playbar is not available."""

def setPlayMode(mode: hou.EnumValue) -> None:
    """setPlayMode(self, mode)

    Set the play mode to one of the following: hou.playMode.Loop - Loop
    to the start of the range when the playback slider reaches the end
    of the range. hou.playMode.Once - Stop playback when the slider
    reaches the end of the range. hou.playMode.Zigzag - Play in the
    forward direction until reaching the end of the playback range, then
    play in the reverse direction.

    Raises hou.NotAvailable if the playbar is not available."""

def frameIncrement() -> float:
    """frameIncrement(self) -> float

    Return the frame increment step size."""

def setFrameIncrement(increment: float) -> None:
    """setFrameIncrement(self, increment)

    Set the frame increment step size. This value is ignored when
    playing with realtime playback turned on.

    Raises hou.NotAvailable if the playbar is not available."""

def playbackRange() -> hou.Vector2:
    """playbackRange(self) -> hou.Vector2

    Return a 2-tuple containing the start and end frame of the playback
    range."""

def setPlaybackRange(start: float, end: float) -> None:
    """setPlaybackRange(self, start, end)

    Set the playback range.

    Raises hou.NotAvailable if the playbar is not available."""

def isRangeRestricted() -> bool:
    """isRangeRestricted(self) -> bool

    Return true if playback is restricted to within the playbar's start
    frame and end frame."""

def setRestrictRange(on: bool) -> None:
    """setRestrictRange(self, on)

    Turn restriction on the playback range on or off. When the
    restriction is turned on, playback will remain with the start and
    end frames of the playback range.

    Raises hou.NotAvailable if the playbar is not available."""

def usesIntegerFrames() -> bool:
    """usesIntegerFrames(self) -> bool

    Return True if playback uses integer frame values. Return False
    otherwise."""

def setUseIntegerFrames(on: bool) -> None:
    """setUseIntegerFrames(self, on)

    Turn integer frame values on or off.

    Raises hou.NotAvailable if the playbar is not available."""

def isRealTime() -> bool:
    """isRealTime(self) -> bool

    Return True if realtime playback is turned on. Return False
    otherwise."""

def setRealTime(on: bool) -> None:
    """setRealTime(self, on)

    Turn realtime playback either on or off.

    Raises hou.NotAvailable if the playbar is not available."""

def realTimeFactor() -> float:
    """realTimeFactor(self) -> float

    Return the multiplier factor used when playing with realtime
    playback turned on."""

def setRealTimeFactor(factor: float) -> None:
    """setRealTimeFactor(self, factor)

    Set the realtime playback multiplier. A multiplier value of less
    than 1 slows down the playback. A multiplier value of greater than 1
    speeds up the playback. A multiplier value equal to 1 maintains
    realtime playback. The multiplier has no effect if realtime playback
    is turned off.

    Raises hou.NotAvailable if the playbar is not available."""

def isRealTimeSkipping() -> bool:
    """isRealTimeSkipping(self) -> bool

    Return True if realtime playback skipping is turned on. Return False
    otherwise."""

def setRealTimeSkipping(on: bool) -> None:
    """setRealTimeSkipping(self, on)

    Turn realtime playback skipping either on or off.

    Raises hou.NotAvailable if the playbar is not available."""

def isAudioShown() -> bool:
    """isAudioShown(self) -> bool

    Return True if the display of audio in the playbar is turned on.
    Return False otherwise."""

def showAudio(on: bool) -> None:
    """showAudio(self, on)

    Turn display of audio on the playbar on or off.

    Raises hou.NotAvailable if the playbar is not available."""

def areKeysShown() -> bool:
    """areKeysShown(self) -> bool

    Return True if the display of keyframes in the playbar is turned on.
    Return False otherwise."""

def showKeys(on: bool) -> None:
    """showKeys(self, on)

    Turn display of keyframes on the playbar on or off.

    Raises hou.NotAvailable if the playbar is not available."""

def isSimCacheShown() -> bool: ...
def showSimCache(on: bool) -> None: ...
def isRangeSliderShown() -> bool:
    """isRangeSliderShown(self) -> bool

    Return True if the display of the range slider in the playbar is
    turned on. Return False otherwise."""

def showRangeSlider(on: bool) -> None:
    """showRangeSlider(self, on)

    Turn display of the range slider on the playbar on or off.

    Raises hou.NotAvailable if the playbar is not available."""

def areTicksShown() -> bool:
    """areTicksShown(self) -> bool

    Return True if the display of frame ticks in the playbar is turned
    on. Return False otherwise."""

def showTicks(on: bool) -> None:
    """showTicks(self, on)

    Turn display of the frame ticks on the playbar on or off.

    Raises hou.NotAvailable if the playbar is not available."""

def moveToBottom() -> None:
    """moveToBottom(self)

    Move the playbar to the bottom of the desktop.

    Raises hou.NotAvailable if the user interface is not available."""

def moveToPane(pane: hou.Pane) -> None:
    """moveToPane(self, pane)

    Move the playbar to the bottom of the specified pane.

    Raises hou.ObjectWasDeleted if pane does not point to a valid pane.
    Raises hou.NotAvailable if the user interface is not available."""

def addEventCallback(callback: Any) -> None:
    """addEventCallback(self, callback)

      Register a Python callback to be called whenever a playbar event
      occurs (i.e. frame change, playback stopped).


      callback
          Any callable Python object that expects two arguments. The first
          argument is a hou.playbarEvent enum value and the second
          argument is a float storing the frame number of when the event
          took place.

    > def outputPlaybarEvent(event_type, frame):
    >     print \"Playbar event\", event_type, \"at frame\", frame
    >
    > hou.playbar.addEventCallback(outputPlaybarEvent)"""

def removeEventCallback(callback: Any) -> None:
    """removeEventCallback(callback)

    Remove a Python callback that was previously registered with
    hou.playbar.addEventCallback. See hou.playbar.addEventCallback for
    more information.

    Raises hou.OperationFailed if the callback was not previously
    registered."""

def clearEventCallbacks() -> None:
    """clearEventCallbacks()

    Remove all Python callbacks that have been registered with
    hou.playbar.addEventCallback."""

def eventCallbacks() -> list[Any]:
    """eventCallbacks() -> tuple of callback

    Return a tuple of all the Python callbacks that have been registered
    with hou.playbar.addEventCallback."""

def selectedKeyframes() -> dict[hou.Parm, list[hou.BaseKeyframe]]: ...
def selectionRange() -> hou.Vector2:
    """selectionRange(self) -> hou.Vector2 or None

    This function exists for backwards compatibility.

    Returns a 2-tuple containing the start and end frame of the
    selection range. If there are multiple selections, the returned
    2-tuple contains the start and end frame of the selection that
    occurs first on the playbar. If there is no selection, then None is
    returned."""

def selectionRanges() -> list[hou.Vector2]:
    """selectionRanges(self) -> tuple of hou.Vector2

    Returns a list of 2-tuples containing the start and end frame of
    each selection range."""

def timelineRange() -> hou.Vector2:
    """timelineRange(self) -> hou.Vector2

    Return a 2-tuple containing the start and end frames of the global
    frame range."""

def timeRange() -> hou.Vector2:
    """timeRange(self) -> hou.Vector2

    Return a 2-tuple containing the start and end times of the global
    time range."""

def setTimeRange(start: float, end: float) -> None:
    """setTimeRange(self, start, end)

    Set the global time range using time in seconds."""

def frameRange() -> hou.Vector2:
    """frameRange(self) -> hou.Vector2

    Return a 2-tuple containing the start and end frame of the global
    time range."""

def setFrameRange(start: float, end: float) -> None:
    """setFrameRange(self, start, end)

    Set the global time range using frame numbers."""

def frameBookmark(bookmark: hou.Bookmark) -> None:
    """frameBookmark(self, bookmark)

    Frames the given bookmark by setting the playback range to the start
    and end time of that bookmark."""

def channelList() -> hou.ChannelList:
    """channelList(self) -> hou.ChannelList

    Return a copy of the current channel list."""

def setChannelList(l: hou.ChannelList) -> None:
    """setChannelList(self, [Hom:hou.ChannelList])

    Set the current channel list."""

def channelListFromSelection() -> hou.ChannelList:
    """channelListFromSelection(self) -> hou.ChannelList

    Return a channel list from the selected nodes. This relies on the
    auto-add to channel list flags."""

def channelListFromNodes(nodes: tuple[hou.Node]) -> hou.ChannelList:
    """channelListFromNodes(self,nodes) -> hou.ChannelList

    Return a channel list from the a list of nodes. This relies on the
    auto-add to channel list flags."""

def channelListFromParms(parms: list[hou.Parm]) -> hou.ChannelList:
    """channelListFromParms(self,parms) -> hou.ChannelList

    Return a channel list from the a list of parameters. This relies on
    the auto-add to channel list flags."""

def channelListFromParmTuples(parms: list[hou.ParmTuple]) -> hou.ChannelList:
    """channelListFromParmTuples(self,parms) -> hou.ChannelList

    Return a channel list from the a list of parameter tuples. This
    relies on the auto-add to channel list flags."""

def isAnimBarShown() -> bool:
    """isAnimBarShown(self) -> bool

    Return whether or not the Animation Toolbar is currently displayed."""

def showAnimBar(show: bool) -> None:
    """showAnimBar(self, show: bool)

    Shows or hides the Animation Toolbar."""

def animBar() -> hou.AnimBar:
    """animBar(self): -> hou.AnimBar

    Return a hou.AnimBar, which provides control over the playbar's
    Animation Toolbar."""
