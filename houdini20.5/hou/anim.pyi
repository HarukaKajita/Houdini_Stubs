# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.anim

def __init__(*args: Any, **kwargs: Any): ...
def bookmarks() -> list[hou.Bookmark]:
    """bookmarks() -> tuple of hou.Bookmarks

    Returns a tuple of current hou.Bookmarks, sorted by start time."""

def saveBookmarks(*args: Any, **kwargs: Any) -> bool:
    """saveBookmarks(filename, bookmarks=None, include_temporary=False) -> bool

    Saves a provided list of hou.Bookmark objects to the given json
    file. If the second argument is left empty, the list of current
    bookmarks will be saved instead. Returns True on success, or False
    otherwise.


    filename
        Name of the file to export the bookmarks to. It should have
        either a .json or .otio extension.

    bookmarks
        If provided, only the given bookmarks will be saved instead of
        saving all bookmarks.

    include_temporary
        Whether or not bookmarks marked as temporary should be included
        in the saved file. False by default. See
        hou.Bookmark.setTemporary."""

def loadBookmarks(filename: str, remove_existing: bool = True) -> bool:
    """loadBookmarks(filename, remove_existing=True) -> bool

    Loads the list of bookmarks from the given file, returning True on
    success or False otherwise. Note that any existing hou.Bookmark
    objects will be invalid.


    filename
        Name of the file to load the bookmarks from. It should have
        either a .json or .otio extension.

    remove_existing
        Whether or not to remove existing bookmarks before loading the
        new ones."""

def saveBookmarksToString(*args: Any, **kwargs: Any) -> dict:
    """saveBookmarksToString(bookmarks=None, include_temporary=False,
    binary=True) -> bytes

        Returns the data for the bookmarks as ASCII or binary, depending on
        the binary argument.


        bookmarks
            If provided, only the given bookmarks will be saved instead of
            saving all bookmarks.

        include_temporary
            Whether or not bookmarks marked as temporary should be included
            in the saved file. False by default. See
            hou.Bookmark.setTemporary.

        binary
            Whether to return the data string in ASCII or binary."""

def loadBookmarksFromString(data: dict, remove_existing: bool = True) -> bool:
    """loadBookmarksFromString(data, remove_existing=True)

    Loads the given bookmarks from the provided string.


    data
        ASCII or binary string returned by saveBookmarksToString.

    remove_existing
        Whether or not to remove existing bookmarks before loading the
        new ones."""

def clearBookmarks() -> None:
    """clearBookmarks()

    Clears out all bookmarks. Note that any existing hou.Bookmark
    objects will be invalid."""

def newBookmark(name: str, start: int, end: int) -> hou.Bookmark:
    """newBookmark(name, start_frame, end_frame) -> hou.Bookmark

    Creates and returns a new hou.Bookmark object using the provided
    options. You must use this function to create new bookmarks; you
    cannot instantiate the Bookmark class directly."""

def bookmark(bookmark_id: int) -> hou.Bookmark:
    """bookmark(session_id) -> hou.Bookmark

    Returns the hou.Bookmark with the matching session id, or returns
    None if there is no such bookmark."""

def getBookmark(bookmark_id: int) -> hou.Bookmark:
    """getBookmark(session_id) -> hou.Bookmark

    This method is deprecated in favor of hou.anim.bookmark.

    Returns the hou.Bookmark with the matching session id, or returns
    None if there is no such bookmark."""

def removeBookmarks(bm: tuple[Bookmark]) -> None:
    """removeBookmarks(bookmarks)

    Deletes the given bookmarks and removes them from the list of active
    bookmarks. The bookmarks parameter should be a list of hou.Bookmark
    objects."""

def mergeGeometryChannels(*args: Any) -> None:
    """mergeGeometryChannels(collection_name, geometry, channel_names=None)

      Writes geometry channels which were previously added to the channel
      list back into the provided geometry as channel primitives.


      collection_name
          Name of the collection from which to fetch the geometry
          channels.

      geometry
          Writeable geometry which the channel primitives will be written
          to.

      channel_names
          List of names of channels in the given collection to fetch. If
          not specified, all channels in the collection will be fetched.

      See also:

    * hou.ChannelList.addGeometryChannels

    * hou.ChannelList.addNodeGeometryChannels

    * hou.playbar.setChannelList"""

def getGeometryChannels(*args: Any) -> None:
    """getGeometryChannels(collection_name, geometry, channel_names=None)

      This method is deprecated in favor of
      hou.anim.mergeGeometryChannels.

      Writes geometry channels which were previously added to the channel
      list back into the provided geometry as channel primitives.


      collection_name
          Name of the collection from which to fetch the geometry
          channels.

      geometry
          Writeable geometry which the channel primitives will be written
          to.

      channel_names
          List of names of channels in the given collection to fetch. If
          not specified, all channels in the collection will be fetched.

      See also:

    * hou.ChannelList.addGeometryChannels

    * hou.ChannelList.addNodeGeometryChannels

    * hou.playbar.setChannelList"""

def setGeometryChannels(collection_name: str, geometry: hou.Geometry, channel_names: tuple[str]) -> None:
    """setGeometryChannels(collection_name, geometry, channel_names)

    Updates an existing scoped geometry channels collection with
    channels from the specified geometry. If channels with conflicting
    names already exist in the geometry, they will be overwritten.


    collection_name
        Name of the collection which the given channels will be added
        to.

    geometry
        Geometry from which to fetch the new channel primitives from.

    channel_names
        List of names of channels to add to the collection. If empty,
        all channels in the geometry will be added."""

def setGeometryChannelsFromPattern(*args: Any) -> None:
    """setGeometryChannelsFromPattern(collection_name, geometry, pattern)

    Updates an existing scoped geometry channels collection with
    channels from the specified geometry. If channels with conflicting
    names already exist in the geometry, they will be overwritten.


    collection_name
        Name of the collection which the given channels will be added
        to.

    geometry
        Geometry from which to fetch the new channel primitives from.

    pattern
        Pattern string, of channel primitives to add to the collection."""

def setGeometryChannelPending(collection_name: str, channel_name: str, value: hou.OptionalDouble) -> None:
    """setGeometryChannelPending(collection_name, channel_name, value)

    Sets the value of the scoped geometry channel at the current frame
    and marks it as pending.


    collection_name
        Name of the collection which the channel belongs to.

    channel_name
        Name of the channel to modify.

    value
        Pending value to set at the current frame. If None, any pending
        keys for the channel will be cleared."""

def isGeometryChannelPending(collection_name: str, channel_name: str) -> bool:
    """isGeometryChannelPending(collection_name, channel_name)

    Returns whether or not a channel has a pending value.


    collection_name
        Name of the collection which the channel belongs to.

    channel_name
        Name of the channel."""

def isGeometryChannelPinned(*args: Any) -> bool:
    """isGeometryChannelPinned(collection_name, channel_name=None) -> bool

    Returns whether or not a geometry channel is pinned. If the second
    argument is left empty, returns whether or not all channels in the
    collection are pinned.


    collection_name
        Name of the collection which the channel belongs to.

    channel_name
        Name of the channel."""

def pinnedGeometryChannels(collection_name: str) -> list[str]:
    """pinnedGeometryChannels(collection_name)

    Returns a list of all pinned geometry channels in the provided
    collection.


    collection_name
        Name of the collection."""

def getPinnedGeometryChannels(collection_name: str) -> list[str]:
    """getPinnedGeometryChannels(collection_name)

    This method is deprecated in favor of
    hou.anim.pinnedGeometryChannels.

    Returns a list of all pinned geometry channels in the provided
    collection.


    collection_name
        Name of the collection."""

def lockGeometryChannelCollection(collection_name: str, lock: bool) -> None:
    """lockGeometryChannelCollection(collection_name, lock)

    Locks or unlocks a geometry channel collection, by preventing
    editing of its channels.


    collection_name
        Name of the collection to modify

    lock
        Whether to lock or unlock the collection."""

def addBookmarksChangedCallback(callback: Any) -> None:
    """addBookmarksChangedCallback(callback)

    Registers a callback function to be executed whenever the current
    bookmarks are modified."""

def removeBookmarksChangedCallback(callback: Any) -> None:
    """removeBookmarksChangedCallback(callback)

    Removes an existing callback."""

def addGeometryChannelsChangedCallback(collection_name: str, callback: Any, on_mouse_up: bool = True) -> bool:
    """addGeometryChannelsChangedCallback(collection_name, callback,
    on_mouse_up=True)

        Registers a callback function to be executed whenever geometry
        channels in the given collection are modified. The collection must
        have already been added to the channel list with
        hou.playbar.setChannelList.


        collection_name
            Name of the collection from which to listen for changes.

        callback
            Callback function, accepting two parameters, a tuple of the
            names of geometry channels that have been changed, and the
            collection name.

        on_mouse_up
            When modifying geometry channels in the Channel Editor, whether
            this callback should be triggered only on mouse up, or
            continuously as channels are modified. Defaults to True, for
            only on mouse up.

        See also:

      * hou.ChannelList.addGeometryChannels

      * hou.ChannelList.addNodeGeometryChannels

      * hou.playbar.setChannelList"""

def removeGeometryChannelsChangedCallback(collection_name: str, callback: Any, on_mouse_up: bool = True) -> bool:
    """removeGeometryChannelsChangedCallback(collection_name, callback,
    on_mouse_up=True)

        Removes an existing callback from the given geometry channels
        collection.


        collection_name
            Name of the collection from which to remove a callback.

        callback
            Callback function to remove.

        on_mouse_up
            Whether the callback to remove was registered for mouse up
            events or not. Must match the same value passed in when
            originally registering the callback with
            addGeometryChannelsChangedCallback."""

def slopeMode() -> hou.EnumValue:
    """slopeMode(self) -> hou.slopeMode

    Returns the current slope mode for inserting new keys, auto or
    manual."""

def setSlopeMode(mode: hou.EnumValue) -> None:
    """setSlopeMode(self, mode)

      Set the default slope mode to one of the following:

    * hou.slopeMode.Manual: Newly inserted keys will be set to manual
      slope mode.

    * hou.slopeMode.Automatic: Newly inserted keys will be set to
      automatic slope mode."""
