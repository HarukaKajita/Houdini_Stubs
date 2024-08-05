# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.hipFile

def __init__(*args: Any, **kwargs: Any): ...
def save(file_name: Optional[str] = None, save_to_recent_files: bool = True) -> None:
    """save(file_name=None, save_to_recent_files=True)

    Saves the current scene to a .hip file.


    file_name
        If this is a string, saves the current scene to a file at this
        path, like File > Save As. The path can be absolute or relative
        to the current directory.

        If this is None, saves the scene to its current path
        (hou.hipFile.path), like File > Save.

        If intermediate directories in the path do not exist, Houdini
        will create them.

    save_to_recent_files
        In a graphical session, whether to add this file to the list of
        recent files in the File > Open Recent Files menu. The default
        is True.

        In a non-graphical session (hython), the function always acts
        like save_to_recent_files is off.

    Raises hou.OperationFailed if Houdini can't create intermediate
    directories or write to the specified file (for example, because of
    filesystem permissions).

    Also raises hou.OperationFailed if you call this while Houdini is
    shutting down (see hou.hipFile.isShuttingDown) or if Houdini is
    already loading or saving the scene file (see
    hou.hipFile.isLoadingHipFile)."""

def saveAndIncrementFileName() -> None:
    """saveAndIncrementFileName()

    Saves the scene to its current path (same as File > Save), but
    increments a number at the end of the filename.

    Raises hou.OperationFailed if Houdini can't create intermediate
    directories or write to the specified file (for example, because of
    filesystem permissions).

    Also raises hou.OperationFailed if you call this while Houdini is
    shutting down (see hou.hipFile.isShuttingDown) or if Houdini is
    already loading or saving the scene file (see
    hou.hipFile.isLoadingHipFile)."""

def saveAndBackup() -> str:
    """saveAndBackup() -> str

    Saves the current scene but first creates a backup of the previous
    saved state to a backup file in $HOUDINI_BACKUP_DIR with _bak and an
    increasing number added before the .hip extension. If
    $HOUDINI_BACKUP_DIR is not set, then this method creates the backup
    file in a backup directory in the same directory as the scene file.

    Returns the absolute path of the backup file.

    Raises hou.OperationFailed if Houdini can't create intermediate
    directories or write to the specified file (for example, because of
    filesystem permissions).

    Also raises hou.OperationFailed if you call this while Houdini is
    shutting down (see hou.hipFile.isShuttingDown) or if Houdini is
    already loading or saving the scene file (see
    hou.hipFile.isLoadingHipFile)."""

def saveAsBackup() -> str:
    """saveAsBackup() -> str

    Saves the current scene to a new file in $HOUDINI_BACKUP_DIR with
    _bak and an increasing number added before the .hip extension. If
    $HOUDINI_BACKUP_DIR is not set, this saves the file to a backup
    directory in the same directory as the scene file.

    Returns the absolute path of the backup file.

    Raises hou.OperationFailed if Houdini can't create intermediate
    directories or write to the specified file (for example, because of
    filesystem permissions).

    Also raises hou.OperationFailed if you call this while Houdini is
    shutting down (see hou.hipFile.isShuttingDown) or if Houdini is
    already loading or saving the scene file (see
    hou.hipFile.isLoadingHipFile)."""

def basename() -> str:
    """basename() -> str

    Return the filename portion of the current scene's path (including
    the .hip extension)."""

def name() -> str:
    """name() -> str

    Return the path of the current hip file relative to the current
    directory. Remember that a file may not exist at this path if the
    current scene hasn't been saved yet.

    This function returns a relative path from the current directory.
    For example, if the current directory is /home/alyah/ and the
    current scene file is /home/alyah/Houdini/Projects/city.hip, this
    would return Houdini/Projects/city.hip. If the current scene file,
    this is the same as calling hou.hipFile.basename().

    If you want an absolute path to the current scene file, use
    Hom:hou.hipFile#path instead."""

def path() -> str:
    """path() -> str

    Return the absolute file path of the current scene file. Remember
    that a file may not exist at this path if the current scene hasn't
    been saved yet."""

def setName(file_name: str) -> None:
    """setName(file_name)

    Sets the in-memory path of the current scene file. This is the path
    Houdini will save to if the user chooses File > Save or you call
    hou.hipFile.save without a file path.


    file_name
        The path to use. This can be an absolute path or relative to the
        current directory.

    This function does not save the scene, it only changes the path
    Houdini thinks the scene should be saved at. To actually save the
    scene to a new path, use hou.hipFile.save."""

def saveMode() -> hou.EnumValue:
    """saveMode(self) -> hou.saveMode

    Return the save mode of the current scene, either
    hou.saveMode.Binary or hou.saveMode.Text."""

def setSaveMode(savemode: hou.EnumValue) -> None:
    """setSaveMode(self, save_mode)

    Set the save mode of the current scene to either hou.saveMode.Binary
    or hou.saveMode.Text."""

def clear(suppress_save_prompt: bool = False) -> None:
    """clear(suppress_save_prompt=False)

    Clears the contents of the current scene file, starting a new
    unsaved file.


    suppress_save_prompt
        Normally, in a graphical session, this function acts the same as
        if the user had chosen File > New, and prompts to save the
        current file if it has unsaved changes. You can force Houdini to
        clear without prompting by passing suppress_save_prompt=True.

        In a non-graphical session (hython), the function always acts
        like suppress_save_prompt is on."""

def load(file_name: str, suppress_save_prompt: bool = False, ignore_load_warnings: bool = False) -> None:
    """load(file_name, suppress_save_prompt=False, ignore_load_warnings=False)

    Loads a new scene (.hip) file.

    Raises hou.OperationFailed if Houdini cannot read the file.

    Raises hou.LoadWarning if loading the new file triggers warnings
    (such as missing assets). You can prevent these exceptions by
    passing ignore_load_warnings=True.


    file_name
        The path to the scene file to load.

    suppress_save_prompt
        Normally, in a graphical session, this function acts the same as
        if the user had chosen File > Open, and prompts to save the
        current file if it has unsaved changes. You can force Houdini to
        load the new file without prompting by passing
        suppress_save_prompt=True.

        In a non-graphical session (hython), the function always acts
        like suppress_save_prompt is on.

    ignore_load_warnings
        Prevents Houdini from raising hou.LoadWarning exceptions if
        loading the new file triggers warnings (such as missing assets).

    Raises hou.OperationFailed if you call this while Houdini is cooking
    a node, shutting down (see hou.hipFile.isShuttingDown) or if Houdini
    is saving the scene file. If this method is called when loading a
    hip file (from 456.py), the operation will succeed, but after
    merging the hip file the 456.py script will not be run again."""

def merge(*args: Any, **kwargs: Any) -> None:
    """merge(file_name, node_pattern=\"*\", overwrite_on_conflict=False,
    ignore_load_warnings=False)

        Imports the contents of the file at path file_name into the current
        scene. (This does not save the current scene file.)

        Raises hou.LoadWarning if loading the new file triggers warnings
        (such as missing assets). You can prevent these exceptions by
        passing ignore_load_warnings=True.


        node_pattern
            Only merge in nodes matching this pattern.

        overwrite_on_conflict
            What to do if merged-in nodes have the same path/name as
            existing nodes. If this is True, merged in nodes replace
            existing nodes. If this is False (the default), merged in nodes
            are renamed if the conflict with existing nodes.

            See hou.hipFile.collisionNodesIfMerged to check for conflicts
            before merging.

        ignore_load_warnings
            Prevents Houdini from raising hou.LoadWarning exceptions if
            loading the new file triggers warnings (such as missing assets).

        Raises hou.OperationFailed if the file to merge doesn't exist or
        Houdini cannot read the file.

        Also raises hou.OperationFailed if you call this while Houdini is
        cooking a node, shutting down (see hou.hipFile.isShuttingDown) or if
        Houdini is saving the scene file. If this method is called when
        loading a hip file (from 456.py), the operation will succeed, but
        after merging the hip file the 456.py script will not be run again."""

def collisionNodesIfMerged(*args: Any, **kwargs: Any) -> list[hou.Node]:
    """collisionNodesIfMerged(file_name, node_pattern=\"*\") -> tuple of
    hou.OpNode

        Returns a sequence of hou.OpNode objects representing the nodes that
        would have conflicts if you tried to merge the given file with
        hou.hipFile.merge.


        node_pattern
            Only check nodes matching this pattern.

        Raises hou.OperationFailed if the file to merge doesn't exist or
        Houdini cannot read the file.

        Also raises hou.OperationFailed if you call this while Houdini is
        shutting down (see hou.hipFile.isShuttingDown) or if Houdini is
        already loading or saving the scene file (see
        hou.hipFile.isLoadingHipFile)."""

def isLoadingHipFile() -> bool:
    """isLoadingHipFile() -> bool

    Returns True if Houdini is currently loading a scene file."""

def isShuttingDown() -> bool:
    """isShuttingDown() -> bool

    Returns True if Houdini is currently exiting."""

def isNewFile() -> bool:
    """isNewFile() -> bool

    Returns whether the current Houdini file is a new file or is a
    previously loaded file.

    This function only works accurately in a graphical session. In a
    non-graphical session (hython) it will always return True if the
    filename matches the default filename."""

def hasUnsavedChanges() -> bool:
    """hasUnsavedChanges() -> bool

    Returns whether the current Houdini session has been modified since
    it was last saved. (This is sometimes referred to as the current
    file being dirty.)

    This function only works in a graphical session. In a non-graphical
    session (hython) it will always return True."""

def groupColorTable() -> dict[str, hou.Color]:
    """groupColorTable() -> dict of str to hou.Color

    Returns a dictionary of color overrides for the viewport group list.
    The viewport group list automatically assigns colors to groups based
    on a hash of the group name. The group color table is a dictionary
    of overrides to these default color assignments. This allows
    particular important groups to be assigned distinctive colors. The
    group color table is saved with the hip file. The color table can be
    modified with hou.hipFile.setGroupColorTable."""

def setGroupColorTable(color_table: dict[str, hou.Color]) -> None:
    """setGroupColorTable(color_table)

      Sets a dictionary of color overrides for the viewport group list.
      The viewport group list automatically assigns colors to groups based
      on a hash of the group name. The group color table is a dictionary
      of overrides to these default color assignments. This allows
      particular important groups to be assigned distinctive colors. The
      group color table is saved with the hip file. The current color
      table can be queried with hou.hipFile.groupColorTable.

      The supplied color_table must be a dict of str to hou.Color. The
      following example will cause groups names 'special_group' to appear
      with a red overlay:

    > color_table = { 'special_group' : hou.Color([1,0,0]) }
    > hou.hipFile.setGroupColorTable(color_table)"""

def importFBX(*args: Any, **kwargs: Any) -> tuple[hou.Node, str]:
    """importFBX(file_name, suppress_save_prompt=False, merge_into_scene=True,
    import_cameras=True, import_joints_and_skin=True, import_geometry=True,
    import_lights=True, import_animation=True, import_materials=True,
    resample_animation=False, resample_interval=1.0,
    override_framerate=False,framerate=-1,
    hide_joints_attached_to_skin=True,
    convert_joints_to_zyx_rotation_order=False,
    material_mode=hou.fbxMaterialMode.FBXShaderNodes,
    compatibility_mode=hou.fbxCompatibilityMode.Maya,
    single_precision_vertex_caches=False, triangulate_nurbs=False,
    triangulate_patches=False, import_global_ambient_light=False,
    import_blend_deformers_as_blend_sops=False,
    segment_scale_already_baked_in=True,
    convert_file_paths_to_relative=True, unlock_geometry=False,
    unlock_deformations=False, import_nulls_as_subnets=False,
    import_into_object_subnet=True,
    convert_into_y_up_coordinate_system=False, create_sibling_bones=True,
    override_scene_frame_range=False, convert_units=False) -> (hou.ObjNode,
    str)

        Imports the contents of an FBX file into the scene, like when the
        user chooses File > Import > FBX. Returns a tuple of the parent
        Subnetwork Object node containing the FBX nodes (see
        import_into_object_subnet option) and a string containing any
        generated load messages.

        Important: see the help for the FBX import dialog for information on
        the various options.


        import_into_object_subnet
            When this is True (the default), Houdini creates a new
            Subnetwork node at the object level and puts imported FBX nodes
            inside the subnet. If you pass import_into_object_subnet=False,
            Houdini creates the FBX nodes directly at the object level (and
            the first item in the returned tuple will be the /obj network
            node).

        Raises hou.OperationFailed if the file to merge doesn't exist or
        Houdini cannot read the file.

        Also raises hou.OperationFailed if you call this while Houdini is
        shutting down (see hou.hipFile.isShuttingDown) or if Houdini is
        already loading or saving the scene file (see
        hou.hipFile.isLoadingHipFile)."""

def addEventCallback(callback: Any) -> None:
    """addEventCallback(self, callback)

      Register a Python callback to be called whenever a .hip file event
      occurs (for example, file load, file save).


      callback
          Any callable Python object that expects one argument. The
          argument is an hou.hipFileEventType enum value.

      See how to write a scene event callback for more information.

    > def scene_event_callback(event_type):
    >     hou.ui.displayMessage(\"An event of type {} occured\".format(event_type))
    >
    > hou.hipFile.addEventCallback(scene_event_callback)"""

def removeEventCallback(callback: Any) -> None:
    """removeEventCallback(callback)

    Removes a Python callback that was previously registered with
    hou.hipFile.addEventCallback. See hou.hipFile.addEventCallback for
    more information.

    Raises hou.OperationFailed if the callback was not previously
    registered."""

def clearEventCallbacks() -> None:
    """clearEventCallbacks()

    Removes all Python callbacks that have been registered with
    hou.hipFile.addEventCallback."""

def eventCallbacks() -> list[Any]:
    """eventCallbacks() -> tuple of callback

    Returns a tuple of all the callback functions that have been
    registered with hou.hipFile.addEventCallback."""
