# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.viewportVisualizers

def __init__(*args: Any, **kwargs: Any): ...
def visualizers(*args: Any, **kwargs: Any) -> list[hou.ViewportVisualizer]:
    """visualizers(category=hou.viewportVisualizerCategory.Common, node=None)
    -> tuple of hou.ViewportVisualizer

        Return a tuple of viewport visualizers registered with Houdini for
        the given category.

        The category argument must be a hou.viewportVisualizerCategory enum
        value. If the category is set to Node, then the node argument must
        be specified.

        Raise TypeError if the category is set to Common or Scene and the
        node argument is also set. Raise TypeError if the category is set to
        Node and the node argument is set to None."""

def createVisualizer(*args: Any, **kwargs: Any) -> hou.ViewportVisualizer:
    """createVisualizer(type, category=hou.viewportVisualizerCategory.Common,
    node=None) -> hou.ViewportVisualizer

        Create a new viewport visualizer for the specified type.

        The type argument must be a hou.ViewportVisualizerType. You can
        retrieve a visualizer type by calling hou.viewportVisualizers.types
        or hou.viewportVisualizers.type.

        The category argument must be a hou.viewportVisualizerCategory enum
        value. If the category is set to Node, then the node argument must
        be specified.

        Raise TypeError if the category is set to Common or Scene and the
        node argument is also set. Raise TypeError if the category is set to
        Node and the node argument is set to None."""

def copyVisualizer(source: hou.ViewportVisualizer) -> hou.ViewportVisualizer:
    """copyVisualizer(source) -> hou.ViewportVisualizer

    Create a duplicate of the specified source visualizer."""

def types() -> list[hou.ViewportVisualizerType]:
    """types() -> tuple of hou.ViewportVisualizerType

    Return a tuple of visualizer types registered with Houdini."""

def type(name: str) -> hou.ViewportVisualizerType:
    """type(name) -> hou.ViewportVisualizerType

    Return the visualizer type registered with the specified name.
    Return None if no such type exists."""

def isCategoryActive(
    category: hou.EnumValue, node: Optional[hou.Node] = None, viewport: Optional[hou.GeometryViewport] = None
) -> bool:
    """isCategoryActive(category, node=None, viewport=None) -> bool

    Return True if the visualizer category is active and False
    otherwise. For Common and Scene categories return True if it is
    active for the specified viewport. The viewport argument must be a
    hou.GeometryViewport.

    Raise TypeError if category is set to Common or Scene and the node
    argument is also set. Raise TypeError if category is set to Node and
    the node argument is set to None. Raise TypeError if both the node
    and viewport arguments are set. Node visualizers are either active
    in all viewports or none of them. They cannot be activated for a
    specific viewport."""

def setIsCategoryActive(
    on: bool, category: hou.EnumValue, node: Optional[hou.Node] = None, viewport: Optional[hou.GeometryViewport] = None
) -> None:
    """setIsCategoryActive(on, category, node=None, viewport=None) -> bool

    Set the activation state of the specified visualizer category. For
    Common and Scene categories the activation state must be set for a
    specific viewport. The viewport argument must be a
    hou.GeometryViewport.

    Raise TypeError if category is set to Common or Scene and the node
    argument is also set. Raise TypeError if category is set to Node and
    the node argument is set to None. Raise TypeError if both the node
    and viewport arguments are set. Node visualizers are either active
    in all viewports or none of them. They cannot be activated for a
    specific viewport."""

def visualizerBySessionId(session_id: int) -> hou.ViewportVisualizer:
    """visualizerBySessionId(session_id) -> hou.ViewportVisualizer

    Given a visualizer's session id, return a ViewportVisualizer object.
    Return None if the id does not correspond to a valid visualizer.


    NOTE
        This function is for internal use by Houdini and isn't usually
        necessary for scripting Houdini or creating tools."""

def removeAllEventCallbacks(*args: Any, **kwargs: Any) -> None:
    """removeAllEventCallbacks(self,
    category=hou.viewportVisualizerCategory.Common, node=None)

        Remove all event callbacks for all event types from this category.

        See hou.viewportVisualizers.addEventCallback for more information."""

def addEventCallback(*args: Any, **kwargs: Any) -> None:
    """addEventCallback(self, event_types, callback,
    category=hou.viewportVisualizerCategory.Common, node=None)

        Register a Python callback that Houdini will call whenever a
        particular action, or event, occurs related to a particular
        visualizer category.


        event_types
            A sequence of hou.viewportVisualizerEventType enumeration values
            describing the event types that will cause Houdini to call the
            callback function.

        callback
            A callable Python object, such as a function or bound method.
            Houdini will call this function whenever one of the event types
            in event_types occurs.

            Houdini calls the function with an event_type keyword argument
            containing the hou.nodeEventType value corresponding to the
            event that triggered the callback.

            Houdini will pass additional keyword arguments depending on the
            event type. For example, in a callback for the
            VisualizerParmsChanged event, Houdini will pass a visualizer
            keyword argument containing a hou.ViewportVisualizer reference
            to the visualizer that changed. See
            hou.viewportVisualizerEventType for the extra arguments (if any)
            passed for each event type.

            You can add **kwargs to the argument list to accept all keyword
            arguments, to allow the same callback to be used for different
            events, or to be safe from future changes:

          > def event_callback(event_type, **kwargs):
          >     ...

        NOTE
            If you try to add the exact same callback function more than
            once, Houdini will still only call the function only once in
            response to an event. However, it may be useful to add the same
            function if you want to register it with different event_types.

        Raises hou.OperationFailed if the event_types list argument is
        empty.

        The following example shows to set up a function that's called
        whenever any parameter on a visualizer in the Common category
        changes:

      >
      > def parm_changed(event_type, **kwargs):
      >     print(\"The parms have changed on \", kwargs['visualizer'])
      >
      > hou.viewportVisualizers.addEventCallback((hou.viewportVisualizerEventType.VisualizeParmsChanged.NameChanged, ), parm_changed)

        See also hou.viewportVisualizers.removeEventCallback and
        hou.viewportVisualizers.removeAllEventCallbacks."""

def removeEventCallback(*args: Any, **kwargs: Any) -> None:
    """removeEventCallback(self, event_types, callback,
    category=hou.viewportVisualizerCategory.Common, node=None)

        Given a callback that was previously added on this category and a
        sequence of hou.viewportVisualizerEventType enumerated values,
        remove those event types from the set of event types for the
        callback. If the remaining set of event types is empty, the callback
        will be removed entirely from this node.

        Raises hou.OperationFailed if the callback had not been previously
        added.

        See hou.viewportVisualizers.addEventCallback for more information."""

def eventCallbacks(*args: Any) -> list[tuple[list[hou.EnumValue], Any]]:
    """eventCallbacks(category=hou.viewportVisualizerCategory.Common,
    node=None) -> tuple of (tuple of hou.viewportVisualizersEvent, callback)

        Return a tuple of all the Python callbacks that have been registered
        with this category with calls to
        hou.viewportVisualizers.addEventCallback."""
