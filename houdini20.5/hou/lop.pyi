# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.lop

def __init__(*args: Any, **kwargs: Any): ...
def defaultNewPrimPath() -> str:
    """defaultNewPrimPath() -> str

    Return the USD primitive path that will be used by default on new
    LOP nodes with a primpath parameter with a default of /$OS."""

def setDefaultNewPrimPath(path: str) -> None:
    """setDefaultNewPrimPath(path)

    Set the USD primitive path that will be used by default on new LOP
    nodes with a primpath parameter with a default of /$OS. This
    identifies a parameter that is used to create a new USD primitive.
    Being able to control this default makes it easier to conform to
    studio-wide standard naming conventions for primitive paths."""

def defaultCollectionsPrimPath() -> str:
    """defaultCollectionsPrimPath() -> str

    Return the USD primitive path that will be used as the default
    location when creating new collections. If not set, the default
    value is /collections."""

def setDefaultCollectionsPrimPath(path: str) -> None:
    """setDefaultCollectionsPrimPath(path)

    Set the USD primitive path that will be used as the default location
    when creating new collections. Being able to control this default
    makes it easier to conform to studio-wide standard naming
    conventions for primitive paths."""

def defaultCollectionsPrimType() -> str:
    """defaultCollectionsPrimType() -> str

    Return the USD primitive type that will be created for holding
    collections when the destination primitive doesn't already exist. If
    not set, the default value is an empty string, indicating that a
    typeless primitive will be created."""

def setDefaultCollectionsPrimType(primtype: str) -> None:
    """setDefaultCollectionsPrimType(path)

    Set the USD primitive type that will be created for holding
    collections when the destination primitive doesn't already exist.
    Being able to control this default makes it easier to conform to
    studio-wide standard conventions for using primitive types."""

def defaultLightsPrimPath() -> str:
    """defaultLightsPrimPath() -> str

    Return the USD primitive path that will be used as the default
    location when creating new lights. If not set, the default value is
    /lights."""

def setDefaultLightsPrimPath(path: str) -> None:
    """setDefaultLightsPrimPath(path)

    Set the USD primitive path that will be used as the default location
    when creating new lights. Being able to control this default makes
    it easier to conform to studio-wide standard naming conventions for
    primitive paths."""

def defaultCamerasPrimPath() -> str:
    """defaultCamerasPrimPath() -> str

    Return the USD primitive path that will be used as the default
    location when creating new cameras. If not set, the default value is
    /cameras."""

def setDefaultCamerasPrimPath(path: str) -> None:
    """setDefaultCamerasPrimPath(path)

    Set the USD primitive path that will be used as the default location
    when creating new cameras. Being able to control this default makes
    it easier to conform to studio-wide standard naming conventions for
    primitive paths."""

def defaultTransformSuffix() -> str:
    """defaultTransformSuffix() -> str

    Return the string that will be used as the default suffix on
    transform attribute names."""

def setDefaultTransformSuffix(suffix: str) -> None:
    """setDefaultTransformSuffix(suffix)

    Set the string that will be used as the default suffix on transform
    attribute names. USD transforms always start with xformOp: followed
    by the transform type (translate, rotate, transform), followed by an
    optional suffix that describes the transform. This string is the
    default Houdini will use in situations where this suffix can be
    provided, which can help make USD layers authored in LOPs conform to
    studio-wide standard naming conventions."""

def showResolvedPaths() -> bool:
    """showResolvedPaths() -> bool

    Return True if the option to show resolved layer file paths is
    turned on."""

def setShowResolvedPaths(show_resolved_paths: bool) -> None:
    """setShowResolvedPaths(show_resolved_paths)

    Set the option to control whether panels that show layer file paths
    should display the exact path set on the layer, or the path after
    passing it through the USD path resolver. The resolved path will
    generally be a full path to a file on disk, where the unresolved
    path may be a relative path, a search path, or a path format that is
    specific to a custom resolver."""

def panesFollowCurrentNode() -> bool:
    """panesFollowCurrentNode() -> bool

    Return True if LOP panes such as the Scene Graph Tree and Scene
    Graph Details should follow the current node selected in the network
    editor."""

def setPanesFollowCurrentNode(follow_current_node: bool) -> None:
    """setPanesFollowCurrentNode(follow_current_node)

    Set the option for LOP panes such as the Scene Graph Tree and Scene
    Graph Details to follow the current node selected in the network
    editor. If set to False, these panes will instead show information
    for the LOP node with its display flag set."""

def panesShowViewportStage() -> bool:
    """panesShowViewportStage() -> bool

    Return True if LOP panes such as the Scene Graph Tree and Scene
    Graph Details should show information about the USD stage generated
    by applying any viewport overrides set in the Scene Graph Tree."""

def setPanesShowViewportStage(show_viewport_stage: bool) -> None:
    """setPanesShowViewportStage(show_viewport_stage)

    Set the option for LOP panes such as the Scene Graph Tree and Scene
    Graph Details to show information about the USD stage generated by
    applying any viewport overrides set in the Scene Graph Tree.

    Turning this option off will improve the performance of these panes
    when there are viewport overrides applied to the scene. The tradeoff
    is that the values shown in the scene graph tree and scene graph
    details for visibility and activation may not match what is shown in
    the viewport. However it will better match the scene description
    that would be used by a final render, as viewport overrides are not
    included in the USD sent to a final render."""

def panesShowPostLayers() -> bool:
    """panesShowPostLayers() -> bool

    Return True if LOP panes such as the Scene Graph Tree and Scene
    Graph Details should show information about the USD stage generated
    by applying any post-layers applied to the parent LOP Network."""

def setPanesShowPostLayers(show_post_layers: bool) -> None:
    """setPanesShowPostLayers(show_post_layers)

    Set the option for LOP panes such as the Scene Graph Tree and Scene
    Graph Details to show information about the USD stage generated by
    applying any post-layers applied to the parent LOP Network."""

def autoSetAssetResolverContext() -> bool:
    """autoSetAssetResolverContext() -> bool

    Return True if the Sublayer and Reference LOP nodes should
    automatically use their first USD layer loaded from disk as the
    resolver context asset path passed to the USD stage to define it's
    asset resolver context."""

def setAutoSetAssetResolverContext(auto_set_context: bool) -> None:
    """setAutoSetAssetResolverContext(auto_set_context)

    Pass in a value of True if the Sublayer and Reference LOP nodes
    should automatically use their first USD layer loaded from disk as
    the resolver context asset path passed to the USD stage to define
    it's asset resolver context. The resolver context is used by the USD
    asset resolver to help find the right files when opening a layer
    file in the context of a particular stage. Often this resolver
    context can be determined by looking at the root layer of the stage.
    In the case of LOPs, the first layer loaded by a Sublayer or
    Reference LOP is the closest thing we have to a root layer. This
    preference makes it easier to implement this workflow. The
    alternative involves using a Configure Stage LOP as the first node
    in the LOP Network to explicitly set the resolver context asset
    path. Similarly this option only affects a Sublayer or Reference LOP
    if it is the first node in the chain."""

def updateRendererInBackground() -> bool:
    """updateRendererInBackground() -> bool

    Return True if the LOP viewport has been configured to run update
    tasks in the background."""

def setUpdateRendererInBackground(update_in_background: bool) -> None:
    """setUpdateRendererInBackground(update_in_background)

    Pass in a value of True to cause the LOP viewport to run update
    tasks in the background, which results in better interactivity but
    allows the viewport display to be temporarily out of sync with the
    current cooked LOP stage."""

def loadPayloadsByDefault() -> bool:
    """loadPayloadsByDefault() -> bool

    Return True if new LOP Networks will be created with the option to
    load all payloads in the viewport enabled."""

def setLoadPayloadsByDefault(load_payloads: bool) -> None:
    """setLoadPayloadsByDefault(load_payloads)

    Pass in a value of True to cause new LOP Networks to be created with
    the option to load all payloads in the viewport enabled. Pass in a
    value of False to disable the loading of payloads in the viewport
    for any new LOP Networks. No existing LOP Networks are affected by
    this method. The default value for this preference is True."""

def allowViewportOnlyPayloads() -> bool:
    """allowViewportOnlyPayloads() -> bool

    Return True if the scene graph tree can allow the user to force the
    loading of a payload into the viewport which has been prevented from
    loading by a Configure Stage node. Return False if the scene graph
    tree should prevent the explicit loading of such payloads. This
    value ensures that the viewport will only show payloads that have
    been processed by the LOP network, eliminating a potential mismatch
    between the scene displayed in the viewport, and the same scene
    rendered with the USD Render ROP with a different set of loaded
    payloads processed by the LOP Network."""

def setAllowViewportOnlyPayloads(allow_viewport_only_payloads: bool) -> None:
    """setAllowViewportOnlyPayloads(allow_viewport_only_payloads)

    Set the flag that indicates whether the viewport is allowed to load
    payloads that have been specified as unloaded by a Configure Stage
    node."""

def pathParameterCompletion() -> bool:
    """pathParameterCompletion() -> bool

    Return True if USD Primitive Path parameters should provide syntax
    highlighting and prim path completion hints. Enabling this may cause
    pauses when editing Primitive Path parameters with very large USD
    stages."""

def setPathParameterCompletion(path_parameter_completion: bool) -> None:
    """setPathParameterCompletion(path_parameter_completion)

    Set the flag that indicates whether the USD Primitive Path
    parameters should provide path completion hints."""

def defaultMetersPerUnit() -> float:
    """defaultMetersPerUnit() -> float

    Return the default meters per unit metric that will be saved into
    USD layers that do not have this value explicitly set. A value of
    zero indicates that Houdini's Unit Length option will be used to
    generate an equivalent meters per unit value."""

def setDefaultMetersPerUnit(meters_per_unit: float) -> None:
    """setDefaultMetersPerUnit(meters_per_unit)

    Set the default meters per unit metric that will be saved into USD
    layers that do not have this value explicitly set. A value of zero
    indicates that Houdini's Unit Length option should be used to
    generate an equivalent meters per unit value."""

def defaultUpAxis() -> str:
    """defaultUpAxis() -> str

    Return the default up axis value that will be saved into USD layers
    that do not have this value explicitly set. An empty string
    indicates that the USD up axis fallback value
    (pxr.UsdGeom.GetFallbackUpAxis) should be used."""

def setDefaultUpAxis(up_axis: str) -> None:
    """setDefaultUpAxis(up_axis)

    Set the default up axis that will be saved into USD layers that do
    not have this value explicitly set. An empty string indicates that
    the USD up axis fallback value (pxr.UsdGeom.GetFallbackUpAxis)
    should be used. Other acceptable values are Y and Z. Trying to set
    any other value will raise a hou.ValueError exception."""

def savePreferences() -> bool:
    """savePreferences() -> bool

    Saves out the current LOP preferences to
    $HOME/houdiniX.Y/solaris.pref. This happens automatically when the
    preferences are modified in the preferences dialog, and when exiting
    Houdini. But in a batch scripting environment, changes made to these
    preferences will not be saved automatically, so this method must be
    used. Returns True is the preference file was saved successfully."""

def reloadLayer(layer_path: str, recursive: bool = False) -> None:
    """reloadLayer(layer_path, recursive = False)

    This method calls the USD Reload method for the specified layer
    path. In addition, it updates internal Houdini data structures of
    the reload so that they can update. This method should be used in
    place of the pxr.Sdf.Layer.Reload or similar methods when running in
    Houdini.

    Setting the recursive parameter to True will cause Houdini to
    recursively look for other layers referenced by the specified layer,
    and reload them as well."""

def makeValidPrimName(name: str) -> str:
    """makeValidPrimName(name) -> str

    This function ensures that a string meets the requirements of a
    legal USD primitive name that can be used as part of a valid
    primitive path. Invalid characters such as spaces and most
    punctuation will be converted to underscores. Note that this means
    the translation is not reversible. If the original string is already
    a legal primitive name, the name is returned unchanged."""

def makeValidPrimPath(path: str, allow_relative: bool = False) -> str:
    """makeValidPrimPath(path, allow_relative = False) -> str

    This function ensures that a string meets the requirements of a
    legal USD primitive path that can be converted into a psx.Sdf.Path
    object. Invalid characters such as spaces and most punctuation will
    be converted to underscores. Note that this means the translation is
    not reversible. If the original string is already a legal primitive
    path, the string is returned unchanged.

    If the allow_relative value is True, the path is allowed to be a
    relative primitive path. A relative path is one that starts with ./
    or ../. If this argument is False, only absolute paths (which start
    with /) are allowed. Relative prefixes are simply removed from the
    path and the returned path will always start with a /."""

def createParmsForProperty(*args: Any) -> hou.ParmTemplateGroup:
    """createParmsForProperty(source, primpath, propertyname, parametername,
    prepend_control_parm, prefix_xform_parms) -> [Hom:hou.ParmTemplateGroup]

        Given a property on a USD stage, this method returns a
        hou.ParmTemplateGroup object that describes the parameters that can
        be placed on an Edit Properties LOP node to control that USD
        property.


        source
            Either a hou.LopNode object or a string. If a hou.LopNode, the
            property is extracted from the USD stage owned by that LOP node.
            If a string, the USD file on disk at the specified path will be
            loaded, and the property extracted from there.

        primpath
            Path to the USD primitive where the property lives.

        propertyname
            The name of the USD property for which parameters will be
            created.

        parametername
            The name of the parameter to generate. This value can be a
            string or None, in which case the parameter name will match the
            property name. It is the parameter names that determines the
            name of the property that will be authored by the Edit
            Properties node, so setting a value for this parameter will
            cause a different property to be authored than the one used to
            generate the parameter.

        prepend_control_parm
            Set to True if the returned parameter template group should
            include a menu for choosing whether the property value should be
            set, ignored, or one of the other standard actions supported by
            the Edit Properties node.

        prefix_xform_parms
            If the specified property is a transform property, this method
            will generate separate translate, rotate, scale, and other
            parameters that get combined to generate a transformation
            matrix. If this option is set to False, these additional
            parameters will use standard Houdini transform parameter names
            like t, s, and r. If set to True, these parameter will be
            prefixed by the property name, which means the parameter names
            will not conflict with other transform parameters on the Edit
            Properties node."""

def createParmsForParameter(
    source: hou.ParmTemplate,
    parametername: Optional[str] = None,
    usdvaluetype: Optional[str] = None,
    prepend_control_parm: bool = True,
    propertyname: Optional[str] = None,
) -> hou.ParmTemplateGroup:
    """createParmsForParameter(source, parametername, usdvaluetype,
    prepend_control_parm, propertyname) -> [Hom:hou.ParmTemplateGroup]

        Given a source node parameter, this method returns a
        hou.ParmTemplateGroup object that describes the parameters that can
        be placed on an Edit Properties LOP node to control a value of a
        corresponding USD property.

        The returned group contains a control parameter that decides how the
        USD property is changed and a value parameter, which is very similar
        to the given parameter, except for disable-when condition and a few
        other small differences.


        source
            A hou.ParmTemplate object on which to base the returned edit
            parameter group.

        parametername
            The name of the parameter to generate. This value can be a
            string or None, in which case the parameter name will match the
            given parameter.

        usdvaluetype
            The name of the USD type of the corresponding USD attribute.

        prepend_control_parm
            Set to True if the returned parameter template group should
            include a menu for choosing whether the property value should be
            set, ignored, or one of the other standard actions supported by
            the Edit Properties node.

        propertyname
            The name of the USD property that corresponds to this parameter.
            Usually, property name is inferred from the parameter name, but,
            optionally, it can be explicitly specified with this parameter."""

def createConnectionParmsForProperty(*args: Any) -> hou.ParmTemplateGroup:
    """createConnectionParmsForProperty(source, primpath, propertyname,
    parametername=None, prepend_control_parm=True) ->
    [Hom:hou.ParmTemplateGroup]

        Given a property on a USD stage, this method returns a
        hou.ParmTemplateGroup object that describes the parameters that can
        be placed on an Edit Properties LOP node to modify the connection of
        that USD (destination) property to a source attribute.


        source
            Either a hou.LopNode object or a string. If a hou.LopNode, the
            property is extracted from the USD stage owned by that LOP node.
            If a string, the USD file on disk at the specified path will be
            loaded, and the property extracted from there.

        primpath
            Path to the USD primitive where the property lives.

        propertyname
            The name of the USD property for which parameters will be
            created.

        parametername
            The name of the parameter to generate. This value can be a
            string or None, in which case the parameter name will be based
            on the property name.

        prepend_control_parm
            Set to True if the returned parameter template group should
            include a menu for choosing whether the property connection
            should be set, severed, or ignored or one of the other standard
            actions supported by the Edit Properties node."""

def setParmTupleFromProperty(*args: Any) -> None:
    """setParmTupleFromProperty(parmtuple, source, primpath, propertyname)

    Set the value of a node parameter tuple from the value of a property
    on a USD primitive. If the parameter cannot be set because the data
    type of the parameter is not compatible with the data type of the
    USD property, or the USD property cannot be found, raises a
    hou.OperationFailed exception.


    parmtuple
        A hou.ParmTuple object specifying the parameter which should be
        set to the value of the USD property.

    source
        A hou.LopNode object holding the USD stage from which the USD
        property value will be extracted.

        Either a hou.LopNode object or a string. If a hou.LopNode, the
        property value is extracted from the USD stage owned by that LOP
        node. If a string, the USD file on disk at the specified path
        will be loaded, and the property value extracted from there.

    primpath
        A string indicating the scene graph path of the USD primitive.

    propertyname
        A string indicating the name of the property on the USD
        primitive."""

def shaderTranslatorID(node: hou.Node) -> int:
    """shaderTranslatorID(node) -> int

    Returns the ID of the shader translator for the given node. The ID
    is specific to Houdini session and can change between them."""

def shaderRenderContextName(node: hou.Node, node_output_name: str) -> str:
    """shaderRenderContextName(node, node_output_name) -> str

    Returns the render context name for the given node and output. It is
    used in the USD material primitive output name, to associate the
    connected shader with a given renderer.


    node
        The shader node to whose render context name to return.

    node_output_name
        The output name for which to return the render context name.
        Nodes can have several output, each for a different renderer."""

def translateShader(*args: Any) -> str:
    """translateShader(node, node_output_name, material_prim_path,
    container_prim_path, shader_prim_name=None, frame=None ) -> str

        Creates a new shader primitive and returns a path to the shader
        primitive output.


        node
            The shader node to translate into a USD shader primitive.

        node_output_name
            The node output that represents the shader to translate (if the
            node is a material), or an output value that is needed as an
            input to another USD shader primitive.

        material_prim_path
            The USD path to the material primitive that contains the USD
            shader.

        container_prim_path
            The path to the parent primitive (ie, NodeGraph or Material) in
            which the USD shader should be directly authored.

        shader_prim_name
            The name to be used for the created USD shader primitive. If not
            given, it will be inferred from the node.

        frame
            The frame number at which to evaluate node parameters, and also
            the USD time code at which to author animated attributes. If not
            given, the current time is used for evaluating parameters, and
            the USD attribute values are authored at the default time code."""

def reportShaderTranslation(node: hou.Node, usd_shader_path: str) -> None:
    """reportShaderTranslation(node, usd_shader_path)

    Adds an entry to the table of known shader translations. This allows
    LOPs to find out the USD shader primitives given a shader VOP node,
    which is necessary for incremental re-translation of shaders.


    node
        The shader node that was translated into a USD shader primitive.

    usd_shader_path
        The USD shader primitive path to which the node was translated."""

def shaderNodeType(shader_name: str) -> hou.NodeType:
    """shaderNodeType(shader_name) -> hou.NodeType

    Returns a shader hou.NodeType given the shader name.

    Shader name is generic identifier of the abstract shader entity, and
    the returned node type is a representation of that shader in a form
    of the node of that type.

    For example, shader \"foo\" may correspond to a VOP node of type
    my_namespace::FooShader::2.0."""

def availableRendererNames() -> list[str]:
    """availableRendererNames() -> tuple of str

    Returns a tuple with the internal names of registered renderer
    plugins."""

def availableRendererLabels() -> list[str]:
    """availableRendererLabels() -> tuple of str

    Returns a tuple with the display labels of registered renderer
    plugins."""

def outputProcessors() -> list[tuple[str, str]]:
    """outputProcessors() -> tuple of tuple of str

    Returns a tuple holding the internal name and user facing label for
    each output processor plugin in the registry. See the USD ROP for
    more information about output processors."""

def outputProcessorParms(name: str) -> hou.ParmTemplateGroup:
    """outputProcessorParms(name) -> hou.ParmTemplateGroup

    Returns the parameters that can be used to configure the output
    processor with an internal name that matches the name parameter. See
    the USD ROP for more information about output processors."""

def usdVersionInfo() -> dict[str, str]:
    """usdVersionInfo() -> dict of str to str

    Returns a dictionary holding information about the USD library built
    into Houdini.


    usdversion
        The USD release number converted to a string. USD releases take
        the form YY.MM, where YY and MM are the year and month in which
        the release occurred.

    packageurl
        The URL of the git repository from which the USD library was
        built.

    packagerevision
        The git commit hash code for the specific branch used to build
        the USD library.

    The packageurl and packagerevision values may return an empty string
    if the USD library that ships with Houdini is replaced with a custom
    USD build."""

def usdOutputMinimumSeverity() -> hou.EnumValue:
    """usdOutputMinimumSeverity() -> hou.severityType

    Returns the minimum USD message severity that will be output to
    standard output. The USD library can produce a variety of messages
    indicating error or warning conditions, or just status messages. If
    such a message is generated while a LOP node is cooking, the message
    will never be output to the console, regardless of this setting."""

def setUsdOutputMinimumSeverity(severity: hou.EnumValue) -> None:
    """setUsdOutputMinimumSeverity(hou.severityType)

    Sets the minimum message severity produced by the USD library that
    should be written to standard output. This method only controls the
    output of messages produced when a LOP node is not cooking."""

def addLockedGeometry(*args: Any) -> str:
    """addLockedGeometry(self, identifier, geo, args = {}) -> str

      Adds a locked copy of a hou.Geometry to a registry, so that it can
      be used as a USD reference or sublayer.

      The returned string is a USD layer identifier that can be used when
      adding a composition arc.

      If an args dictionary is specified, the contents must be pre-
      converted to be strings. For example: { 't': '1.0' } is valid, but {
      't': 1.0 } is not.


      NOTE
          The registry entries created by using this function must be
          explicitly removed via hou.lop.removeLockedGeometry.

      Example:

    > from pxr import Usd
    > geo = hou.Geometry()
    > geo.loadFromFile('shaderteapot.bgeo')
    > stage = Usd.Stage.CreateInMemory()
    > layer_id = hou.lop.addLockedGeometry('teapot', geo)
    > stage.GetRootLayer().subLayerPaths.append(layer_id)

      See also hou.LopNode.addLockedGeometry"""

def removeLockedGeometry(identifier: str) -> bool:
    """removeLockedGeometry(self, identifier) -> bool

      Removes a locked hou.Geometry from the registry, returning a bool to
      indicate success or failure.


      NOTE
          The identifier should be the str value returned from a previous
          call to hou.lop.addLockedGeometry.

      Example:

    > geo = hou.Geometry()
    > geo.loadFromFile('shaderteapot.bgeo')
    > layer_id = hou.lop.addLockedGeometry('teapot', geo)
    > hou.lop.removeLockedGeometry(layer_id)"""

def forceReloadAllFilesFromDisk(reload_viewports: bool = False) -> None:
    """forceReloadAllFilesFromDisk(self, reload_viewports)

    Presses the reload button on every LOP node with such a parameter.
    If the reload_viewports parameter is True, this method also clears
    all USD stages owned by scene viewer panes, which will effectively
    cause all USD stages in Houdini to be rebuilt from scratch. This is
    a potentially very expensive operation, but in some cases may be
    required to force USD to reload and re-resolve paths to assets on
    disk, such as when the configuration of an asset resolver has been
    changed."""

def _isProceduralSigned(filepath: str) -> bool: ...
def availableRendererInfo() -> Any:
    """availableRendererInfo() -> list of dict

    Returns a list of dicts containing meta data for registered renderer
    plugins."""

def addPreferenceChangeCallback(callback: Any) -> None:
    """addPreferenceChangeCallback(callback)

    Registers a callback function that is invoked any time one of these
    preferences is changed."""

def removePreferenceChangeCallback(callback: Any) -> None:
    """removePreferenceChangeCallback(callback)

    Deregisters a callback function previously registered with a call to
    addPreferenceChangeCallback."""
