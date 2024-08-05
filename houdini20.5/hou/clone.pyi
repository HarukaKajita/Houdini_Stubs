# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.clone

def __init__(*args: Any, **kwargs: Any): ...
def runAsClone(
    start_port: int = 0,
    end_port: int = -1,
    debug: bool = False,
    block: bool = False,
    print_port: bool = False,
    connection_timeout_seconds: int = -1,
) -> None:
    """hou.clone.runAsClone

    Causes the current process to operate as a clone process.

    USAGE
      runAsClone(start_port=0, end_port=-1, debug=False, block=False,
      print_port=False, connection_timeout_seconds=-1)

    This method opens a network port to receive connections from a host
    process. Once connected, the host process sends its hip file contents
    and any changes made in the host process. This process maintains its
    network state to match the host process, and sends back rendered images
    to the host.

    Both graphical and non-graphical Houdini processes can act as clones.
    Using a graphical Houdini process as a clone may be useful for
    debugging, but generally clone processes will be non-graphical (hbatch
    or hython). Note that the synchronization if one way, from host to
    clones. Changes made in the clone process are not sent to the host
    process, and may cause issues with the synchronization of future changes
    from the host.

    Generally (except for debugging) it is easiest to run a clone process in
    a blocking mode where user input and interaction with the clone process
    is not permitted until the host process disconnects. This is controlled
    with the block parameter.


    start_port
        The lowest TCP/IP port number that can be opened for the host to
        establish a connection. The default value of 0 indicates that any
        available port can be used. In some renderfarm setups, only certain
        ports will allow a connection to be made from the host to the clone
        process. These restrictions will depend on the configuration of the
        firewall between the host and clone machines.

    end_port
        Highest TCP/IP port number that can be opened to receive the host
        connection. The default value of -1 allows any port number higher
        than the start_port.

    debug
        Sets the clone process' networking debug mode. Setting this to True
        will cause additional logging of networking events.

    block
        Controls whether user interation with this process should be
        blocked. This block lasts as long as a host process is connected to
        this clone (or the connection timeout expires without any host
        connection being established).

    print_port
        Set this to True to have this process output its port number to the
        standard output stream. The output will be of the form
        HOUDINI_CLONE_PORT=12345. The printing of this port is often
        necessary for the host process (which often launches the clone
        process) to know what port number it can use to connect to the clone
        process. The only other way to know the clone's port number is by
        setting the start_port and end_port parameters to the same fixed
        value.

    connection_timeout_seconds
        Indicates how long this method should wait for a host connection to
        be established before giving up and closing the connection port.
        This setting can help prevent zombie processes on a render farm, but
        be sure to allocate enough time for the host process to establish
        communication with the clone."""

def createClone(id: Optional[str] = None) -> hou.clone.Connection:
    """hou.clone.createClone

    Creates a new hou.clone.Connection object.

    USAGE
      createClone(cloneid=None)

    Creates and returns a new default hou.clone.Connection object with the
    provided unique identifier. Note that this does not start a new clone
    process or establish a connection. It simply creates the connection
    object so that it can be configured and connected later. The
    hou.clone.Connection.duplicate method can also be used to create a new
    connection object.


    cloneid
        The unique identifier for the new clone connection. If this value is
        None or an empty string, a unique identifier is created
        automatically. If a clone with the provided identifier already
        exists, the provided identifier increments a numeric suffix until
        the identifier does not match any existing connectino object."""

def clones() -> list[hou.clone.Connection]:
    """hou.clone.clones

    Return a tuple of all hou.clone.Connection objects.

    USAGE
      clones()

    Use this method to get access to all hou.clone.Connection objects that
    currently exist. To more efficiently look up a specific connection
    object, use hou.clone.clone instead."""

def clone(id: str) -> hou.clone.Connection:
    """hou.clone.clone

    Return a specific hou.clone.Connection object.

    USAGE
      clone(cloneid)

    Every hou.clone.Connection object has a unique identifier associated
    with it (see hou.clone.Connection.sessionId). This method returns the
    connection object that corresponds to the provided unique identifier.


    cloneid
        The unique identifier of the clone object that should be returned.
        If the provided identifier does not correspond to an existing
        hou.clone.Connection object, this method returns None."""

def deleteClone(id: str) -> None:
    """hou.clone.deleteClone

    Deletes a hou.clone.Connection.

    USAGE
      deleteClone(cloneid)

    Disconnects and deletes an existing hou.clone.Connection object. This is
    different from simply disconnecting a clone using
    hou.clone.Connection.disconnect, after which the connection object still
    exists and can be reconnected. After calling this method, the provided
    clone identifier ceases to be valid,


    cloneid
        The unique identifier of the clone conenction object to delete. If
        the provided clone identifier doesn't correspond to an existing
        clone, this method does nothing."""

def deleteDisconnectedClones() -> None:
    """hou.clone.deleteDisconnectedClones

    Deletes all disconnected hou.clone.Connection.

    USAGE
      deleteDisconnectedClones()

    This method is a shortcut for calling hou.clone.clones, checking the
    connection status of each clone, and calling for every clone that is not
    currently connected."""

def removeAllConnectionChangeCallbacks() -> None:
    """hou.clone.removeAllConnectionChangeCallbacks

    Deregister all connection change callback methods.

    USAGE
      removeAllConnectionChangeCallbacks()

    This method is a shortcut for calling
    hou.clone.connectionChangeCallbacks and calling
    hou.clone.removeConnectionChangeCallback for each returned callback
    method."""

def removeAllImageChangeCallbacks() -> None:
    """hou.clone.removeAllImageChangeCallbacks

    Deregister all image change callback methods.

    USAGE
      removeAllImageChangeCallbacks()

    This method is a shortcut for calling hou.clone.imageChangeCallbacks and
    calling hou.clone.removeImageChangeCallback for each returned callback
    method."""

def addConnectionChangeCallback(callback: Any) -> None:
    """hou.clone.addConnectionChangeCallback

    Registers a callback method to be run any time a hou.clone.Connection is
    modified.

    USAGE
      addConnectionChangeCallback(callback)

    This method allows code to monitor clone connections for creation,
    removal, and changes of configuration or state. To monitor changes to
    incoming rendered images, the hou.clone.addImageChangeCallback method
    must be used.


    callback
        The function that is invoked when a connection object changes. This
        method should accept a single cloneid parameter, which is the unique
        identifier of the clone object that has changed. Because this
        callback can indicate the destruction of a clone object, be aware
        that calling hou.clone.clone with this cloneid value may return
        None."""

def removeConnectionChangeCallback(callback: Any) -> None:
    """hou.clone.removeConnectionChangeCallback

    Deregisters a specific connection change callback method.

    USAGE
      removeConnectionChangeCallback(callback)

    Removes the provided callback from the list of methods that are run when
    a clone connection's state changes. This is the opposite of the
    hou.clone.addConnectionChangeCallback method.


    callback
        The callback method that should be deregistered. If this callback is
        not curently registered, this method raises a hou.OperationFailed
        exception."""

def connectionChangeCallbacks() -> list[Any]:
    """hou.clone.connectionChangeCallbacks

    Return a tuple of all registered connection change callbacks.

    USAGE
      connectionChangeCallbacks()

    Provides access to every callback method registered with the
    hou.clone.addConnectionChangeCallback method."""

def addImageChangeCallback(callback: Any) -> None:
    """hou.clone.addImageChangeCallback

    Registers a callback method to be run any time a hou.clone.Connection
    receives a new image.

    USAGE
      addImageChangeCallback(callback)

    This method allows code to monitor clone connections for changes to the
    any clone's rendered image. To monitor changes to the connection state,
    use hou.clone.addConnectionChangeCallback.


    callback
        The function that is invoked when a clone's rendered image is
        updated. This method should accept a single cloneid parameter, which
        is the unique identifier of the clone object whose image has
        changed."""

def removeImageChangeCallback(callback: Any) -> None:
    """hou.clone.removeImageChangeCallback

    Deregisters a specific image change callback method.

    USAGE
      removeImageChangeCallback(callback)

    Removes the provided callback from the list of methods that are run when
    a clone connection's rendered image changes. This is the opposite of the
    hou.clone.addImageChangeCallback method.


    callback
        The callback method that should be deregistered. If this callback is
        not curently registered, this method raises a hou.OperationFailed
        exception."""

def imageChangeCallbacks() -> list[Any]:
    """hou.clone.imageChangeCallbacks

    Return a tuple of all registered image change callbacks.

    USAGE
      imageChangeCallbacks()

    Provides access to every callback method registered with the
    hou.clone.addImageChangeCallback method."""

class Connection(object):
    """hou.clone.Connection

    Represents a connection to a clone process.

    These objects represent an active or potential connection to a Houdini
    clone process, either on the local machine or a remote machine. A
    connection can be connected and disconnected repeatedly, but the object
    continues to be valid. As with hou.Node objects, objects of thie type
    are references to the underlying connection object owned by the Houdini
    cloning framework. This means that all instances of this class that
    refer to the same underlying clone connection will affect each other.
    The underlying object can even be deleted in which case almost all
    methods on this object will raise exceptions (though the
    hou.clone.Connection.isValid method can be used to test if the
    underlying object still exists without raising an exception).

    Clone connections are identified by a unique session id string which
    behaves much like a Houdini node name. At any given time, the session id
    for each clone connection is unique. But session ids can be reused if a
    connection is deleted and a new one created. Clones connections are
    saved to the hip file, and are automatically disconnected when Huodini
    is shut down or a new hip file is opened. When opening a hip file, the
    loaded connection objects are always left in a disconnected state, and
    must be explicitly connected to start the clones processes.

    New connections can only be created by calling hou.clone.createClone or
    hou.clone.Connection.duplicate. Existing connection can be accessed
    using hou.clone.clone or hou.clone.clones."""

    def __init__(self, *args: Any, **kwargs: Any): ...
    def isValid(self) -> bool:
        """isValid() -> bool

        Return True if the connection associated with this object is still
        valid. Valid simply means that the underlying connection has not
        been deleted. This method and hou.clone.Connection.sessionId are the
        only methods that will not raise an exception when run after the
        underlying connection has been deleted."""
    def sessionId(self) -> str:
        """sessionId() -> str

        Return the unique string that can be used to identify this
        connection object, or fetch it from the cloning framework using the
        hou.clone.clone method. This value is set when constructing the
        connection and cannot be changed. This value has limitations like
        those for node names."""
    def name(self) -> str:
        """name() -> str

        Return the user-facing name for this clone."""
    def setName(self, name: str) -> None:
        """setName(name)

        Checng the user-facing name for this clone. This is the name shown
        in the Clone control pane, and does not have any restrictions on its
        value (spaces and punctuation are allowed)."""
    def lopNode(self) -> hou.Node:
        """lopNode() -> hou.LopNode

        Return the LOP node that defines the stage which will be rendered by
        this clone."""
    def setLopNode(self, lop: hou.Node) -> None:
        """setLopNode(lop)

        Set the LOP node that defines the stage which will be rendered by
        this clone. This value must be set for the clone to generate an
        image."""
    def cameraPath(self) -> str:
        """cameraPath() -> str

        Return the USD primitive path of the camera prim that defines the
        view that will be rendered by this clone."""
    def setCameraPath(self, camerapath: str) -> None:
        """setCameraPath(camerapath)

        Set the USD primitive path of the camera prim that defines the view
        that will be rendered by this clone. This path should point to a USD
        Camera primitive on the stage defined by the
        hou.clone.Connection.lopNode. This value must be set for the clone
        to generate an image."""
    def renderer(self) -> str:
        """renderer() -> str

        Return the name of the Render Delegate this clone will use."""
    def setRenderer(self, renderer: str) -> None:
        """setRenderer(renderer)

        Set the name of the Render Delegate this clone will use. This can be
        the internal name or label of any render delegate installed on the
        computer running this clone."""
    def renderSettings(self) -> str:
        """renderSettings() -> str

        Return the USD primitive path of the render settings prim that
        controls therendering configurations for this clone."""
    def setRenderSettings(self, rendersettings: str) -> None:
        """setRenderSettings(rendersettings)

        Return the USD primitive path of the render settings prim that
        controls therendering configurations for this clone. This path
        should point to a USD Render Settings primitive on the stage defined
        by the hou.clone.Connection.lopNode."""
    def availableAovs(self) -> list[str]:
        """availableAovs(self) -> tuple of str

        Return the names of all AOVs generated by the clone render. This
        will return an empty tuple if the clone has not yet returned an
        image."""
    def displayAov(self) -> str:
        """displayAov(self) -> str

        Return the name of the AOV this clone should return to the host.
        This string may contain wildcards in which case multiple matching
        AOVs may be returned."""
    def setDisplayAov(self, displayaov: str) -> None:
        """setDisplayAov(self, aov)

        Set the name of the AOV this clone should return to the host. A
        string matching pattern can be specified to return multiple AOVs.
        Passing an empty string or None for the aov parameter instructs the
        clone to return all AOVs."""
    def resolutionScale(self) -> float:
        """resolutionScale(self) -> float

        Return the override resolution scale factor. This scaling is applied
        to the resolution set on the render settings for this clone. A value
        of 0 indicates that the render settings resolution will be used. A
        non-zero resolution scale value takes precedence over an override
        resolution explicitly set using setResolution."""
    def setResolutionScale(self, resolution_scale: float) -> None:
        """setResolutionScale(self, resolution_scale)

        Set the resolution scale for the image generated by this clone. This
        scale value is always applied to the resolution set on the render
        settings primitive. The value can be less than one to render a lower
        resolution image, or greater than one to render a higher resolution
        image. A value of 0 disables the resolution scaling."""
    def resolution(self) -> tuple[int, int]:
        """resolution(self) -> (int, int)

        Return the override resolution set for the clone's returned image.
        If no override resolution has been set, this method returns (0, 0).
        In this case, the clone will generate an image with a resolution
        determined by the render settings primitive. A non-zero resolution
        scale value takes precedence over an override resolution explicitly
        set using setResolution, but the resolution scale setting does not
        affect the value returned by this method."""
    def setResolution(self, width: int, height: int) -> None:
        """setResolution(self, width, height)

        Set the resolution of the image generated by this clone. Specifying
        a width and height of 0 instructs the clone to generate an image
        with a resolution determined by the render settings primitive. A
        non-zero resolution scale value set with setResolutionScale takes
        precedence over an override resolution explicitly set using this
        method."""
    def frameExpression(self) -> str:
        """frameExpression(self) -> str

        Return a string specifying the expression that is run to generate
        the frame to which this clone should be set when cooking. If the
        returned string is empty, the frame number used by the clone will
        match the host's current frame number."""
    def setFrameExpression(self, expression: str) -> None:
        """setFrameExpression(self, expression)

        Set the expression that is run to generate the frame to which this
        clone should be set when cooking. The expression must always be a
        string, but can be any hscript expression that returns a number. For
        example, $F + 10 instructs the clone to cook ten frames ahead of the
        host's current frame. The expression is run in the host process, and
        the resulting value is sent to the clone."""
    def contextOptionExpression(self, opt: str) -> Any:
        """contextOptionExpression(self, opt) -> str

        Return a string specifying the expression that is run to generate
        the value for the context option opt that this clone will use when
        cooking. If the returned string is empty, the context option value
        used by the clone will match the host's value for this option."""
    def setContextOptionExpression(self, opt: str, expression: str) -> None:
        """setContextOptionExpression(self, opt, expression)

        Set the expression that is run to generate the the value for the
        context option opt that this clone use when cooking. The expression
        must always be a string, but can be any hscript expression that
        returns a number or string. For example, $SHOT + 1 instructs the
        clone to cook with a value for SHOT that is one more than the host's
        value for this option. The expression is run in the host process,
        and the resulting value is sent to the clone."""
    def contextOptionsWithExpressions(self) -> list[str]:
        """contextOptionsWithExpressions(self) -> str

        Return a tuple of context option names that have expressions set for
        this clone, and thus where the clone's value for these context
        options may differ from the host process."""
    def processUpdates(self) -> bool:
        """processUpdates(self) -> bool

        Return a boolean value indicating whether the clone will restart its
        render in response to updates from the host."""
    def setProcessUpdates(self, process_updates: bool) -> None:
        """setProcessUpdates(self, process_updates)

        Configure the clone process to ignore updates from the host process,
        and continue rendering whatever stage is currently being rendered."""
    def launcherConfig(self) -> dict[str, Any]:
        """launcherConfig(self) -> dict

        Return a dictionary of configuration options that control the
        launcher plugin when starting up this clone process."""
    def setLauncherConfig(self, config: dict[str, Any]) -> None:
        """setLauncherConfig(self, config)

        Store the dictionary of launcher configuration options that should
        be used when launching this clone process. The contents and
        interpretation of this dictionary is under the discretion of the
        launcher plugin. It is stored with the clone connection object for
        convenience since launching a clone process is generally a pre-
        requisite to connecting to the clone."""
    def connect(self, host: str, port: int) -> bool:
        """connect(self, host, port) -> bool

        Connect this host to a running clone process on the specified host
        machine accessible through the provided TCP/IP port number. The
        connection attempt lasts for one second. If the connection is made,
        this method returns True. Returns False if the connection cannot be
        made for any reason. The host and port values are generally provided
        by the launcher plugin, which starts the clone process and reads the
        output from the process to determine the port number (which is
        output by the hou.clone.runAsClone method."""
    def disconnect(self) -> None:
        """disconnect(self)

        Disconnects from a connected clone process. Does nothing if the
        clone is not currently connected."""
    def isConnected(self) -> bool:
        """isConnected(self) -> bool

        Return true if this clone connection object represents an active
        connection to a clone process."""
    def isWaitingToConnect(self) -> bool:
        """isWaitingToConnect(self) -> bool

        Return true if setWaitingToConnect(True) has been called on this
        connection."""
    def setWaitingToConnect(self, waiting_to_connect: bool) -> None:
        """setWaitingToConnect(self, waiting_to_connect)

        Sets a flag on this connection indicating that it is waiting to
        connect to a clone process. This flag is only used as a visual hint
        and does not affect the operation of the clone framework. This flag
        can be set whether the clone is connected or disconnected. Only
        launcher plugins should set this flag, and only while waiting for a
        clone process to initialize or for a connection to be made to the
        clone process. Calling disconnect will also set this flag to False."""
    def host(self) -> str:
        """host(self) -> str

        Return the name of the host machine on which the connected clone
        process is running. Returns an empty string if there is no connected
        clone process."""
    def port(self) -> int:
        """port(self) -> int

        Return the port number used to connect to this object's clone
        process. Returns 0 if there is no connected clone process."""
    def imagePath(self) -> str:
        """imagePath(self) -> str

        Returns a string that can be used to access the image most recently
        returned by this clone. This string generally does not change when
        new images are sent from the clone, but this is not guaranteed. The
        format of this string will be of the form membuf:XXXXX. This unusual
        path value indicates that the image is not written to disk, but
        instead exists only as a block of memory. But Houdini nodes and HOM
        methods which can load images from disk will also be able to load
        the rendered image using this membuf path."""
    def imageVersion(self) -> int:
        """imageVersion(self) -> int

        A number that is increased every time a new image is sent to the
        host by this clone. This number can be used to detect when the image
        needs to be reloaded, redrawn, or otherwise re-processed to account
        for the updated image."""
    def imageSize(self) -> list[int]:
        """imageSize(self) -> tuple of int

        Returns a tuple of two integers that are the width and height of the
        image most recently returned by this clone. Note that the image size
        may change any time a new image is sent to the host if the
        resolution parameters or render settings primitive has changed.
        Becuase this is the true size of the most recently sent image, this
        value may differ from the resolution requested from this clone
        through the setResolution method."""
    def percentComplete(self) -> float:
        """percentComplete(self) -> float

        Indicates the progress of the render as reported through the render
        statistics."""
    def renderGalleryDataSource(self) -> hou.AssetGalleryDataSource:
        """renderGalleryDataSource(self) -> hou.AssetGalleryDataSource

        If this clone is currently connected and rendering, the resulting
        images are placed into the snapshot gallery for the target LOP
        Network. This method returns a hou.AssetGalleryDataSource that
        provides access to the snapshot gallery database in which the image
        metadata is stored. If this clone is not connected or has not
        generated any image data yet, this method returns None."""
    def renderGalleryItemId(self) -> str:
        """renderGalleryItemId(self) -> str

        If this clone is currently connected and rendering, the resulting
        images are placed into the snapshot gallery for the target LOP
        Network. This method returns the unique identifier of this image's
        entry in the snapshot gallery database. This identifier can be
        passed to the hou.AssetGalleryDataSource object returned by the
        renderGalleryDataSource method to look up additional information
        about the image. If this clone is not connected or has not generated
        any image data yet, this method returns an empty string."""
    def createSnapshot(self) -> str:
        """createSnapshot(self) -> str

        If this clone is currently connected and rendering, this method
        creates a snapshot in the LOP Network's snapshot gallery database,
        along with the current state of the LOP Network's nodes, just as
        when hitting the snapshot button to save the current viewport
        contents. The snapshot will contain all AOVs currently being sent
        from the clone process. Returns the snapshot gallery item identifier
        of the newly created snapshot. Returns an empty string if no
        snapshot could be created, or the clone is not connected or doesn't
        have image data avilable."""
    def duplicate(self) -> hou.clone.Connection:
        """duplicate(self) -> hou.clone.Connection

        Makes a copy of this clone object. All the settings and
        configuration information is duplicated. The new clone does not
        launch or connect to a new clone process even if this clone
        connection is currently active. This must be done explicitly, after
        creating the duplicate."""
