# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.hda

def __init__(*args: Any, **kwargs: Any): ...
def installFile(
    file_path: str,
    oplibraries_file: Optional[str] = None,
    change_oplibraries_file: bool = True,
    force_use_assets: bool = False,
) -> None:
    """installFile(file_path, oplibraries_file=None,
    change_oplibraries_file=True, force_use_assets=False)

        Install all the node types defined in an hda file into the current
        Houdini session. This function is equivalent to File > Install
        Digital Asset Library... in Houdini.


        file_path
            The hda file to load.

        oplibraries_file
            The path to an OPlibraries file or None. OPlibraries files are
            text files containing lists of hda files to load on startup.
            When Houdini starts up it reads all the OPlibraries files it
            finds in the Houdini path and loads all the hda files listed in
            them. By creating OPlibraries files in $HOME/houdiniX.Y,
            $HSITE/houdiniX.Y, $JOB, etc. you can create libraries that are
            specific to a particular user, studio, job, etc.

            This parameter is only meaningful when change_oplibraries_file
            is True.

            Note that OPlibraries are only used when the Use OPlibraries
            files to find HDAS checkbox in the Configuration tab of the
            Operator Type Manager is checked.

            If None or Current HIP File, the hda file is loaded only into
            the current Houdini session. The file name will also be saved in
            the Hip file so that when the same Hip file is loaded, the hda
            file will also be loaded automatically.

            If Scanned Asset Library Directories, this is equivalent to the
            installation menu entry in the Install Digital Asset Library
            dialog.

        change_oplibraries_file
            When oplibraries_file is not None and this parameter is True,
            Houdini will modify the OPlibraries file, adding the hda file to
            it.

        force_use_assets
            When True, ensure that the definitions inside the hda file are
            current. If they would not otherwise provide the current
            definition, they are marked as preferred to ensure they are
            current. See hou.HDADefinition.isPreferred for more information.

        Note that, if you do not store the path to the hda file in an
        OPlibraries file, Houdini will store it in the current Houdini
        session. So, when you load a hip file, it will try to load the hda
        files that it references."""

def uninstallFile(file_path: str, oplibraries_file: Optional[str] = None, change_oplibraries_file: bool = True) -> None:
    """uninstallFile(file_path, oplibraries_file=None,
    change_oplibraries_file=True)

        Uninstall an hda file and all the node type definitions it provides
        from the current Houdini session. The hda file and its contents on
        disk are unchanged.

        You can set file_path to the special name \"Embedded\" to refer to the
        digital assets embedded in the current hip file. The following
        example removes any embedded digital asset definitions from the
        current Houdini session:

      > hou.hda.uninstallFile(\"Embedded\")

        If oplibraries_file is not None and change_oplibraries_file is True,
        Houdini will remove the path to the hda from the specified
        OPlibraries file. See hou.hda.installFile for more information about
        these parameters.

        If all the definitions of a node type are uninstalled, any instances
        of that node type will warn that they are using an incomplete asset
        definition. They will, however, retain their parameter values as
        spare parameters. Installing an hda file with the missing node type
        will restore those node instances and remove the warnings.

        See also hou.HDADefinition.destroy."""

def reloadFile(file_path: str) -> None:
    """reloadFile(file_path)

    Reload the contents of an hda file, loading any updated digital
    asset definitions inside it.

    You only need to call this function if an hda file was modified from
    outside the current Houdini session."""

def reloadAllFiles(rescan: bool = True) -> None:
    """reloadAllFiles(rescan=True)

    Reload the digital asset files and update asset definitions in the
    current session.

    If the rescan is true, Houdini will check the hda directories for
    any new hda files and load them too.

    See also hou.hda.reloadFile."""

def reloadNamespaceOrder() -> None:
    """reloadNamespaceOrder()

    Check HOUDINI_OPNAMESPACE_HIERARCHY environment variable and rebuild
    the node type preference order that determines the node type to use
    when only unqualified root name is used in scripts, or, when Tab
    menu settings specify to show only a single preferred entry among
    several potential choices from different namespaces."""

def expandToDirectory(file_path: str, directory_path: str) -> None:
    """expandToDirectory(file_path, directory_path)

    Expand the contents of the hda file in file_path into the directory
    directory_path. If the directory does not already exist it is
    created.

    When expanding an hda file, Houdini puts each digital asset
    definition in the file into its own directory. As well, it puts each
    section inside a definition into its own file. Each directory inside
    the expanded file tree contains a Sections.List file that maps the
    actual file or directory names into the section names, since section
    names may contain characters that cannot occur in directory or file
    names. See hou.HDASection for more information about sections.

    This function provides an easy way to inspect and modify the
    contents of an hda file. See also hou.hda.collapseFromDirectory."""

def collapseFromDirectory(file_path: str, directory_path: str) -> None:
    """collapseFromDirectory(file_path, directory_path)

    Given a directory that contains a previously expanded hda file,
    collapse it into the hda file specified by file_path.

    This function provides the inverse of hou.hda.expandToDirectory."""

def loadedFiles() -> list[str]:
    """loadedFiles() -> tuple of str

      Return a tuple of paths to the hda files that are loaded into the
      current Houdini session.

      This method is can be approximately implemented as follows:

    > def loadedFiles():
    >     '''Return a list of hda files loaded into this Houdini session.'''
    >     # Look through all the node types, and for those that have digital
    >     # asset definitions, remember the hda file containing the definition.
    >     result = []
    >     for category in hou.nodeTypeCategories().values():
    >         for node_type in category.nodeTypes().values():
    >             definition = node_type.definition()
    >             if definition is None:
    >                 continue
    >             if definition.libraryFilePath() not in result:
    >                 result.append(definition.libraryFilePath())
    >     return result

      See hou.HDADefinition.isCurrent for an example."""

def renameSource(oplibraries_file: str, source_name: Optional[str] = None) -> None:
    """renameSource(oplibraries_file, source_name=None)

    Give a name to an OPlibraries file. This name appears in the
    Operator Type Manager's list of OPlibraries file. If source_name is
    None, the name is removed from the OPlibraries file.

    If the oplibraries_file does not already exist, it is created.

    See hou.hda.installFile for more information about OPlibraries
    files."""

def definitionsInFile(file_path: str) -> list[hou.HDADefinition]:
    """definitionsInFile(file_path) -> tuple of hou.HDADefinition

      Return all the digital asset definitions inside an hda file. See
      hou.HDADefinition for more information.

      Raises hou.OperationFailed if file_path does not refer to a valid
      hda file.

    > # Print the node types defined by digital assets in $HOME/houdiniX.Y/hda/OPcustom.hda:
    > >>> import os
    > >>> my_hda_file = \"%s/hda/OPcustom.hda\" % hou.homeHoudiniDirectory()
    > >>> for definition in hou.hda.definitionsInFile(my_hda_file):
    > ...     print definition.nodeTypeCategory().name() + \"/\" + definition.nodeTypeName()
    > Sop/gcoggeo
    > Sop/gCogFlatGeo
    > Sop/gDivideAtCentroid
    > Object/gAxle
    > Object/gCog"""

def componentsFromFullNodeTypeName(node_type_name: str) -> list[str]:
    """componentsFromFullNodeTypeName(node_type_name) -> tuple of str

      Returns a tuple of operator type name components that constitute the
      full node type name. The components in the tuple appear in the
      following order: scope network type, node type namespace, node type
      core name, and version.

    > >>> # Parse the full name into components
    > >>> hou.hda.componentsFromFullNodeTypeName('MyUserNamespace::MyHDA::2.5')
    > ('', 'MyUserNamespace', 'MyHDA', '2.5')
    > >>> hou.hda.componentsFromFullNodeTypeName('Sop/foreach::MyCounterHDA')
    > ('Sop/foreach', '', 'MyCounterHDA', '')"""

def fullNodeTypeNameFromComponents(scope_node_type: str, name_space: str, name: str, version: str) -> str:
    """fullNodeTypeNameFromComponents(scope_node_type, name_space, name,
    version) -> str

        Returns a full node type name build out of the given components. The
        arguments represent the following components: scope network type,
        node type namespace, node type core name, and version.

      > >>> # Compose the node type full name from components
      > >>> hou.hda.fullNodeTypeNameFromComponents('', 'userA', 'sphere', '')
      > 'userA::sphere'
      > >>> hou.hda.fullNodeTypeNameFromComponents('', 'userB', 'myHda', '2.6')
      > 'userB::myHda::2.6'
      > >>> hou.hda.fullNodeTypeNameFromComponents('Sop/foreach', '', 'MyCounterHDA', '')
      > 'Sop/foreach::MyCounterHDA'"""

def changeCurrentStoreUser(new_user: str) -> None: ...
def safeguardHDAs() -> bool:
    """safeguardHDAs() -> bool

    Return True if the Safeguard Operator Definitions configuration
    option is turned on. When safeguarding is turned on then no digital
    asset definition can be modified in the Houdini session."""

def setSafeguardHDAs(on: bool) -> None:
    """setSafeguardHDAs(on)

    Set whether the Safeguard Operator Definitions configuration option
    should be turned on or off. The on argument must be either True of
    False."""

def removeAllEventCallbacks() -> None:
    """removeAllEventCallbacks(self)

    Remove all event callbacks for all event types.

    See hou.hda.addEventCallback for more information."""

def defaultFileExtension() -> str:
    """defaultFileExtension(self) -> str

    Returns the default hda file extension for the current session based
    on the taint."""

def addEventCallback(event_types: tuple[enum.Enum], callback: Any) -> None:
    """addEventCallback(self, event_types, callback)

      Register a Python callback that Houdini will call whenever a
      particular action, or event, occurs with digital asset libraries.

      Callbacks only persist for the current session. For example, they
      are not saved to the .hip file. If you want persistent callbacks in
      every session, you can add them in code in pythonrc.py (runs on
      startup) or 456.py (runs when the user opens a .hip file). See where
      to add Python scripting for more information.


      event_types
          A sequence of hou.hdaEventType enumeration values describing the
          event types that will cause Houdini to call the callback
          function.

      callback
          A callable Python object, such as a function or bound method.
          Houdini will call this function whenever one of the event types
          in event_types occurs.

          Houdini calls the function with an event_type keyword argument
          containing the hou.hdaEventType value corresponding to the event
          that triggered the callback.

          Houdini will pass additional keyword arguments depending on the
          event type. For example, in a callback for the LibraryInstalled
          or LibraryUninstalled events, Houdini will pass a library_path
          keyword argument containing the path of the .hda file that was
          installed or uninstalled. See hou.hdaEventType for the
          additional arguments passed for each event type.

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
      whenever a new asset is added to Houdini:

    >
    > def hda_event(event_type, asset_definition, **kwargs):
    >     label = asset_definition.description()
    >     library_path = asset_definition.libraryFilePath()
    >     print(\"New asset %s in %s\" % (label, library_path))
    >
    > hou.hda.addEventCallback((hou.hdaEventType.AssetCreated, ), hda_event)

      See also hou.hda.removeEventCallback and
      hou.hda.removeAllEventCallbacks."""

def removeEventCallback(event_types: tuple[enum.Enum], callback: Any) -> None:
    """removeEventCallback(self, event_types, callback)

    Given a callback that was previously added and a sequence of
    hou.hdaEventType enumerated values, remove those event types from
    the set of event types for the callback. If the remaining set of
    event types is empty, the callback will be removed entirely.

    Raises hou.OperationFailed if the event_types list argument is
    empty.

    Raises hou.OperationFailed if the callback had not been previously
    added.

    See hou.hda.addEventCallback for more information."""

def eventCallbacks() -> list[tuple[list[hou.EnumValue], Any]]: ...
