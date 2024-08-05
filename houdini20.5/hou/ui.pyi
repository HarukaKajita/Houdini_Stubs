# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.ui

def __init__(*args: Any, **kwargs: Any): ...
def shellIO() -> hou.ShellIO:
    """shellIO() -> hou.ShellIO

    Return the hou.ShellIO object used to implement Houdini's graphical
    Python shell. This function is used internally by Houdini, and you
    shouldn't need to access the ShellIO directly."""

def curDesktop() -> hou.Desktop:
    """curDesktop() -> hou.Desktop

    Return the current desktop."""

def desktop(name: str) -> hou.Desktop:
    """desktop(name) -> hou.Desktop

    Return the desktop with the specified name. Return None if no such
    desktop exists."""

def desktops() -> list[hou.Desktop]:
    """desktops() -> tuple of hou.Desktop

    Return all the desktops.

    See hou.Desktop.setAsCurrent for an example."""

def radialMenu(name: str) -> hou.RadialMenu:
    """radialMenu(name) -> hou.RadialMenu

    Returns a hou.RadialMenu object representing the named menu, or None
    if the menu does not exist."""

def radialMenus() -> list[hou.RadialMenu]:
    """radialMenus() -> tuple of hou.RadialMenu

    Returns a tuple of hou.RadialMenu objects representing existing
    menus."""

def createRadialMenu(name: str, label: str) -> hou.RadialMenu:
    """createRadialMenu(name, label) -> hou.RadialMenu

    Creates a new radial menu object with the given name and label."""

def createRadialItem(submenu: bool = False, callback: bool = False) -> hou.RadialScriptItem:
    """createRadialItem(submenu=False, callback=false) -> hou.RadialScriptItem

    Creates a temporary radial menu item.


    submenu
        Whether this item is a submenu or action.

    callback
        Whether this item is uses python callback or script (text)."""

def injectRadialItem(location: int, item: hou.RadialItem) -> None:
    """injectRadialMenu(name)

    Injects a registered menu and override the current menu.


    name
        The name of the menu."""

def injectRadialMenu(name: str) -> None: ...
def _getActiveRadialMenu() -> str: ...
def _setActiveRadialMenu(name: str) -> None: ...
def updateMainMenuBar() -> None:
    """updateMainMenuBar()

    Forces label expressions to be re-evaluated for the main Houdini
    menu bar. These top level menu items are never automatically
    refreshed, so it is up to the creator of these menus to also install
    handlers that detect when a condition has changed that might affect
    the menu, and call this method to force a refresh."""

def panes() -> list[hou.Pane]:
    """panes(self) -> tuple of hou.Pane

    Return a tuple of all visible panes, including those in all floating
    windows.

    See also hou.Desktop.panes."""

def paneTabs() -> list[hou.PaneTab]:
    """paneTabs(self) -> tuple of hou.PaneTab

    Return a tuple of all visible pane tabs, including those in all
    floating windows.

    See also hou.Desktop.paneTabs."""

def currentPaneTabs() -> list[hou.PaneTab]:
    """currentPaneTabs(self) -> tuple of hou.PaneTab

    Return a tuple of all visible pane tabs that are selected in their
    containing panes, including those in all floating windows.

    See also hou.Desktop.currentPaneTabs."""

def paneTabOfType(type: hou.EnumValue, index: int = 0) -> hou.PaneTab:
    """paneTabOfType(self, type, index=0) -> hou.PaneTab or None

    Find and return the pane tab with the desired type. If no such tab
    exists, return None.


    type
        A hou.paneTabType enumerated variable.

    index
        If there are multiple tabs with the desired type, this parameter
        determines which one is returned. Use index=0 to return the
        first found tab, index=1 to return the second found tab, etc. By
        default, index is 0.

    See also hou.Desktop.paneTabOfType."""

def findPane(pane_id: int) -> hou.Pane:
    """findPane(self, pane_id) -> hou.Pane or None

    Return the pane with the given unique id, or None if no such pane
    exists.

    See also hou.Desktop.findPane."""

def findPaneTab(name: str) -> hou.PaneTab:
    """findPaneTab(self, name) -> hou.PaneTab or None

    Return the pane tab with the given name, or None if no such tab
    exists.

    The name may optionally be prefixed by the desktop name and a
    period.

    See also hou.Desktop.findPaneTab."""

def floatingPaneTabs() -> list[hou.PaneTab]:
    """floatingPaneTabs(self) -> tuple of hou.PaneTab

    Return all the pane tabs in floating panels.

    See also hou.Desktop.floatingPaneTabs."""

def floatingPanels() -> list[hou.FloatingPanel]:
    """floatingPanels(self) -> tuple of hou.FloatingPanel

    Return all the visible floating panels.

    See also hou.Desktop.floatingPanels."""

def paneUnderCursor() -> hou.Pane:
    """paneUnderCursor(self)

    Return the hou.Pane object located under the mouse cursor. Return
    None if no pane is located under the mouse cursor.

    This method searches all visible panes including panes not attached
    to the current desktop."""

def paneTabUnderCursor() -> hou.PaneTab:
    """paneTabUnderCursor(self)

    Similar to hou.ui.paneUnderCursor but return the hou.PaneTab object
    instead located under the mouse cursor. Return None if no pane tab
    is located under the mouse cursor.

    This method searches all visible pane tabs including pane tabs not
    attached to the current desktop."""

def isUserInteracting() -> bool:
    """isUserInteracting()

    Return True if the user is currently interacting with the UI in a
    way that is likely to cause a stream of node or parameter changes.
    This includes scrubbing the playbar, and dragging a handle in the
    viewport. Testing this value can be useful to avoid performing
    expensive updates to UI components that can wait until the user
    interaction is complete before performing their update."""

def setUserInteracting(interacting: bool) -> None:
    """setUserInteracting()

    Sets a flag checked by isUserInteracting(). That function will
    return True after setUserInteracting(True) is called, until you call
    setUserInteracting(False) to reset that flag.

    This can be used in python viewer states, or python panels to stop
    certain UI updates during viewport interaction or when using UI
    widgets.

    Set this to True when the interaction starts and False when it
    finishes."""

def orientationUpAxis() -> hou.EnumValue:
    """orientationUpAxis(self) -> hou.orientUpAxis enum value

    Return a hou.orientUpAxis indicating the current orientation mode's
    up axis."""

def handleOrientToNormalAxis() -> hou.EnumValue:
    """handleOrientToNormalAxis(self) -> hou.handleOrientToNormalAxis enum
    value

        Return a hou.handleOrientToNormalAxis indicating the handle axis
        that is to be aligned to component normals when orienting."""

def displayConfirmation(*args: Any, **kwargs: Any) -> bool: ...
def displayCustomConfirmation(*args: Any, **kwargs: Any) -> int:
    """displayCustomConfirmation(text, buttons=(),
    severity=hou.severityType.Message, default_choice=0, close_choice=-1,
    help=None, title=None, details=None, details_label=None,
    suppress=hou.confirmType.OverwriteFile) -> int

        This method is the same as displayConfirmation, except it also
        accepts a list of custom button labels and returns the selected
        button index instead of a boolean value. The button index
        corresponds to the entry in the label array that was selected in the
        pop up dialog. If fewer than two button labels are specified, the
        default labels OK and Cancel will be added as necessary to achieve
        the required length of at least two labels.


        text
            The message to display.

        buttons
            The labels for the buttons that appear in the dialog. If fewer
            than two labels are passed in, OK and Cancel will be added as
            needed. For example, if the method is called with
            buttons=(\"Continue\",) the dialog will display a Continue and
            Cancel button.

        severity
            A hou.severityType value that determines which icon to display
            on the dialog. Note that using hou.severityType.Fatal will exit
            Houdini after the user closes the dialog.

        default_choice
            The index of the button that is selected if the user presses
            enter.

        close_choice
            The index of the button that is selected if the user presses
            escape or closes the dialog.

        help
            Additional help information to display below the main message.

        title
            The window's title. If None, the title is Houdini.

        details
            A string containing extra messages that is not visible unless
            the user clicks Show Details.

        details_label
            A string containing the label for the expand/collapse button
            that controls whether or not the detail text is visible.


            suppress
                Used to skip the display of this dialog if the user
                requested not to be shown this confirmation dialog again.

      > '''Before cooking the TOP network, prompts the user to either save the .hip
      > file, cook without saving the file, or cancel the cook operation completely.'''
      >
      > def save_and_cook(top_network):
      >     buttons = (\"Save and Continue\", \"Continue Without Saving\", \"Cancel\")
      >     selected_button = hou.ui.displayCustomConfirmation(\"Save before cooking?\", suppress=hou.confirmType.TopCookSave, buttons=buttons)
      >
      >     if selected_button == 0:
      >         hou.hipFile.save()
      >
      >     if selected_button != 2:
      >         top_network.cookWorkItems(block=True)"""

def displayMessage(*args: Any, **kwargs: Any) -> int:
    """displayMessage(text, buttons=('OK',), severity=hou.severityType.Message,
    default_choice=0, close_choice=-1, help=None, title=None, details=None,
    details_label=None, details_expanded=False,
    suppress=hou.confirmType.NoConfirmType) -> int

        Pop up a small window with a message and one or more buttons and
        wait for the user to press a button. Return the index of the button
        the user pressed.


        text
            The message to display.

        buttons
            A sequence of strings containing the names of the buttons. By
            default the message window contains a single OK button.

        severity
            A hou.severityType value that determines which icon to display
            on the dialog. Note that using hou.severityType.Fatal will exit
            Houdini after the user closes the dialog.

        default_choice
            The index of the button that is selected if the user presses
            enter.

        close_choice
            The index of the button that is selected if the user presses
            Escape or closes the dialog.

        help
            Additional help information to display below the main message.

        title
            The window's title. If None, the title is Houdini.

        details
            A string containing extra messages that is not visible unless
            the user clicks Show Details.

        details_label
            A string containing the label for the expand/collapse button
            that controls whether or not the detail text is visible. If
            details_expanded is set to true this parameter has no effect.

        details_expanded
            A boolean, if true then the text area where the detail messages
            appear is always shown and cannot be collapsed. If false, the
            detail message area is initially folded when the message box is
            popped up and the user can expand to read the details.

        suppress
            Include a checkbox in the dialog to enable users to request the
            non-display of this dialog in future occurrences. The dialog
            cannot be suppressed by default.

      > def saveIfNeeded():
      >         '''Prompt the user if they want to save, and save the hip file if they choose Yes.'''
      >         if hou.ui.displayMessage(\"Save the current hip file?\", buttons=(\"Yes\", \"No\")) == 0:
      >             hou.hipFile.save()"""

def readInput(*args: Any, **kwargs: Any) -> tuple[int, str]:
    """readInput(message, buttons=('OK',), severity=hou.severityType.Message,
    default_choice=0, close_choice=-1, help=None, title=None,
    initial_contents=None) -> (int, str)

        Pop up a small window with a textbox and wait for the user to enter
        a line of text. Return a tuple containing an integer and the text
        they entered. The integer is the index of the pressed button. If
        close_choice is not None and the user closed the dialog by clicking
        on its close button or by pressing Escape, then the returned integer
        is set to close_choice.


        message
            The message to display above the text field.

        buttons
            A sequence of strings containing the names of the buttons. By
            default the message window contains a single OK button.

        severity
            A hou.severityType value that determines which icon to display
            on the dialog. Note that using hou.severityType.Fatal will exit
            Houdini after the user closes the dialog.

        default_choice
            The index of the button that is selected if the user presses
            enter.

        close_choice
            The index of the button that is selected if the user presses
            Escape or clicks on the dialog's close button. If there is more
            than one button and close_choice is -1, then the user cannot
            close the dialog with Escape or the dialog's close button. If
            there is only one button and close_choice is -1, then the user
            can close the dialog with Escape or the dialog's close button,
            and the button's index is returned.

        help
            Additional help information to display below the main message.

        title
            The window's title. If None, the title is Houdini.

        initial_contents
            The initial contents of the text field. If None, the text field
            is initially empty.

        See also hou.ui.readMultiInput"""

def readMultiInput(*args: Any, **kwargs: Any) -> tuple[int, list[str]]:
    """readMultiInput(message, input_labels, password_input_indices=(),
    buttons=('OK',), severity=hou.severityType.Message, default_choice=0,
    close_choice=-1, help=None, title=None, initial_contents=(\"\",)) -> (int,
    tuple of str)

        Pop up a small window with a textbox and wait for the user to enter
        a text into several input fields. Return a tuple containing an
        integer and the tuple of strings they entered, one for each input
        field. The integer is the index of the pressed button. If
        close_choice is not -1 and the user closed the dialog by clicking on
        its close button or by pressing Escape, then the returned integer is
        set to close_choice.


        message
            The message to display above the text field.

        input_labels
            A sequence of labels to appear in front of each input field. The
            length of the sequence determines the number of input fields
            that will appear in the window.

        password_input_indices
            A sequence of indices of which input fields are password fields.
            Fields whose index is not in this sequence will not be password
            fields.

        buttons
            A sequence of strings containing the names of the buttons. By
            default the message window contains a single OK button.

        severity
            A hou.severityType value that determines which icon to display
            on the dialog. Note that using hou.severityType.Fatal will exit
            Houdini after the user closes the dialog.

        default_choice
            The index of the button that is selected if the user presses
            enter.

        close_choice
            The index of the button that is selected if the user presses
            Escape or clicks the dialog's close button. If there is more
            than one button and close_choice is -1, then the user cannot
            close the dialog with Escape or the dialog's close button. If
            there is only one button and close_choice is -1, then the user
            can close the dialog with Escape or the dialog's close button,
            and the button's index is returned.

        help
            Additional help information to display below the main message.

        title
            The window's title. If this is None, the title is \"Houdini\".

        initial_contents
            A sequence of strings specifying the initial value of each text
            box specified by the input_labels argument. If this sequence is
            shorter than input_labels, the rest of the fields are left
            blank. The default is to start with all fields blank.

        The initial_contents values must be strings. If you use another type
        (for example, integers), the function will raise a TypeError. If you
        want to prompt the user for integers, convert the initial values
        into strings, and convert the results back into integers. For
        example:

      > start_int, end_int = hou.playbar.frameRange()
      > button_idx, values = hou.ui.readMultiInput(
      >     \"Set the new frame range\", (\"Start Frame\", \"End Frame\"),
      >     initial_contents=(str(start_int), str(end_int)),
      >     title=\"Frame Range\",
      >     buttons=(\"OK\", \"Cancel\"),
      >     default_choice=0, close_choice=1,
      > )
      > new_start_int = int(values[0])
      > new_end_int = int(values[1])

        See also hou.ui.readInput"""

def selectFromList(*args: Any, **kwargs: Any) -> list[int]:
    """selectFromList(choices, default_choices=(), exclusive=False,
    message=None, title=None, column_header=\"Choices\", num_visible_rows=10,
    clear_on_cancel=False, width=0, height=0, sort=False,
    condense_paths=False) -> tuple of int

        Pop up a window with a set of choices in a list box and prompt the
        user to choose zero or more of them. If selection is accepted then
        the list of selected row indices are returned. If selection is
        canceled then the initial selection (default choices) is returned.


        choices
            A sequence of strings containing the possible choices.

        default_choices
            A sequence of integers containing the indices of the choices
            that are initially selected.

        exclusive
            Whether or not the user must choose exactly one of the possible
            choices.

        message
            The message to display above the list box.

        title
            The window's title. If None, the title is Houdini.

        column_header
            The column header for the list of choices. Users can click this
            header label to sort the list. If None, then the header is
            removed. Note that the tuple of integers represents the original
            order of items, regardless of the displayed sort order.

        num_visible_rows
            The number of rows of entries that are visible at a time. If
            there are more possible choices than visible rows, Houdini will
            use a scrollbar.

        clear_on_cancel
            If set to True then an empty tuple is returned when selection is
            canceled. Otherwise the initial selection (default_choices) is
            returned when selection is canceled.

        width
            The chooser dialog's width. If 0, then the chooser dialog uses a
            default width.

        height
            The chooser dialog's height. If 0, then the chooser dialog uses
            a default height.

        sort
            Whether or not the chooser should sort the list immediately. If
            this flag is set to True the contents of the chooser will be
            sorted in ascending order, otherwise the order of the strings in
            choices will be used as-is.

        condense_paths
            Whether or not the chooser should convert absolute paths into
            paths containing variables like $HIP. when this flag is enabled,
            the chooser will also show a toggle to enable/disable it."""

def selectFromTree(*args: Any, **kwargs: Any) -> list[str]:
    """selectFromTree(choices, picked=(), exclusive=False, message=None,
    title=None, clear_on_cancel=False, width=0, height=0) -> tuple of str

        Pop up a window with a set of choices in a tree chooser and prompt
        the user to choose zero or more of them. The choices are arranged
        into a tree using a forward slash as a path separator. If selection
        is accepted then the list of selected paths are returned. If
        selection is canceled then the initial selection (picked) is
        returned.


        choices
            A sequence of strings containing the possible choices.

        picked
            A sequence of strings containing the items that should be
            initially selected.

        exclusive
            Whether or not the user must choose exactly one of the possible
            choices.

        message
            The message to display above the list box.

        title
            The window's title. If None, the title is Make Selection.

        clear_on_cancel
            If set to True then an empty tuple is returned when selection is
            canceled. Otherwise the initial selection (picked) is returned
            when selection is canceled.

        width
            The chooser dialog's width. If 0, then the chooser dialog uses a
            default width.

        height
            The chooser dialog's height. If 0, then the chooser dialog uses
            a default height."""

def _selectFile(*args: Any, **kwargs: Any) -> str: ...
def selectParmTag(width: int = 0, height: int = 0) -> list[str]:
    """selectParmTag(width=0, height=0) -> tuple of str

    Pop up a window with a tree view of recognized parameter tags and
    prompt the user to choose a tag. Parameter tags are metadata that
    can be attached to a parameter template with
    hou.ParmTemplate.setTags and queried with hou.ParmTemplate.tags.

    Tags listed in the window are recognized by Houdini. For example,
    choosing the GL Diffuse tag and assigning it to a parameter template
    causes the viewport to recognize the parameter as the diffuse color.

    This method returns a 2-tuple where the first element is the
    selected tag name and the second element is the selected tag value.
    If no tag is selected or if the selection operation is canceled,
    then a 2-tuple of empty strings is returned.


    width
        The chooser dialog's width. If 0, then the chooser dialog uses a
        default width.

    height
        The chooser dialog's height. If 0, then the chooser dialog uses
        a default height."""

def selectParm(*args: Any, **kwargs: Any) -> list[str]:
    """selectParm(category=None, bound_parms_only=False, relative_to_node=None,
    message=None, title=None, initial_parms=(), multiple_select=True,
    width=0, height=0) -> tuple of str

        Pop up a window with a parameter tree view and prompts the user to
        select parameters, populated initially with initial_parms. If
        selection is accepted then a list of selected parameter paths are
        returned. If selection is canceled then the initial selection
        (initial parameters) is returned.

        category: A hou.NodeTypeCategory if filtering by node type,
        otherwise None if all parameters should be shown

        bound_parms_only: True if the dialog should only display parameters
        that are bound to a default handle. False is all parameters should
        be shown.

        relative_to_node: A hou.OpNode that you want the selected parameters
        paths to be relative to.

        message: The message to display in the dialog.

        title: The title of the dialog.

        multiple_select: Whether the user may select multiple parameters.

        width: The chooser dialog's width. If 0, then the chooser dialog
        uses a default width.

        height: The chooser dialog's height. If 0, then the chooser dialog
        uses a default height."""

def selectParmTuple(*args: Any, **kwargs: Any) -> list[str]:
    """selectParmTuple(category=None, bound_parms_only=False,
    relative_to_node=None, message=None, title=None, initial_parm_tuples=(),
    multiple_select=True, width=0, height=0) -> tuple of str

        Pop up a window with a parameter tree view and prompts the user to
        select parameter tuples, populated initially with
        initial_parm_tuples.

        See hou.ui.selectParm for documentation on the arguments."""

def selectColor(initial_color: Optional[hou.Color] = None) -> hou.Color:
    """selectColor(initial_color=None) -> hou.Color or None

    Pop up a window with a color chooser, and waits for the user to
    choose a color and hit the OK or Cancel button. If the user hits the
    OK button, this method returns the color chosen in the dialog. If
    the user hits Cancel, this method returns None.

    The initial_color parameter specifies a hou.Color that will appear
    in the dialog when it first opens. If not set, the initial color
    will be white."""

def _openColorEditor(
    color_changed_callback: None,
    include_alpha: bool = False,
    initial_color: Optional[hou.Color] = None,
    initial_alpha: float = 1.0,
) -> None: ...
def loadPaletteFile(file: str) -> list[hou.Color]:
    """loadPaletteFile(self, file) -> tuple of hou.Color

    Load a palette file and return the colors listed in the palette. The
    file parameter can be a full path, or just a file name. In the
    latter case, the Houdini path is searched for the first instance of
    the named file under the config subdirectory."""

def savePaletteFile(file: str, colors: list[hou.Color]) -> None:
    """savePaletteFile(self, file, colors)

    Save a palette file with the contents of the colors parameter, a
    tuple of hou.Color objects. The file parameter must be a full path
    to the file where the palette should be saved.

    Raises hou.OperationFailed if the file could not be written."""

def updateValueLadder(cursor_x: int, cursor_y: int, alt_key: bool, shift_key: bool) -> None:
    """updateValueLadder(cursor_x, cursor_y, alt_key, shift_key)

    Updates the value in the currently opened ladder value window based
    on the given cursor position and boolean arguments.

    This function only works if hou.ui.openValueLadder was previously
    called. Raises hou.OperationFailed if no value ladder window is
    currently open.


    cursor_x
        The horizontal coordinate of the current mouse cursor position.

    cursor_y
        The vertical coordinate of the current mouse cursor position.

    alt_key
        Whether the [Alt] modifier key is currently held. This scales
        the ladder value.

    shift_key
        Whether the [Shift] modifier key is currently held. This changes
        the ladder's active level.

    See hou.ui.openValueLadder for more information."""

def closeValueLadder() -> None:
    """closeValueLadder()

    Closes the current value ladder window that was open by a previous
    call to hou.ui.openValueLadder.

    Raises hou.OperationFailed if no value ladder window is open.

    See hou.ui.openValueLadder for more information."""

def displayFileDependencyDialog(*args: Any, **kwargs: Any) -> tuple[bool, list[tuple[hou.Parm, str]]]:
    """displayFileDependencyDialog(rop_node=None, uploaded_files=(),
    forced_unselected_patterns=(), project_dir_variable='HIP',
    is_standalone=true) -> (bool, tuple of Parm and string tuples)

        Open a dialog displaying the file dependencies in the current .hip
        file.

        Return a 2-tuple where the first element in the tuple is True if the
        dialog was closed with the OK button and False otherwise, and the
        second element is a tuple of the selected file patterns. Each
        selected file pattern is represented as a <hou.Parm, string> pair
        which stores the source parameter that contains the file pattern and
        the file pattern itself.


        NOTE
            If the source parameter is not None then it is recommended that
            file pattern expansion be performed by evaluating the
            parameter's value instead of calling hou.expandString.
            Evaluating the source parameter is far more accurate since it
            accounts for channel references and context-specific variables
            like $OS."""

def displayNodeHelp(node_type: hou.NodeType) -> None:
    """displayNodeHelp(node_type)

      Display the help for the specified node type. If no help browser is
      open, this function will create a new one.

      If you want to display the help for a node instance, it is easy to
      access the hou.NodeType from the node, as illustrated in this
      example:

    > def displayHelpForNode(node):
    > '''Given a hou.OpNode, display its help.'''
    > hou.ui.displayNodeHelp(node.type())"""

def _openTypePropertiesDialogForNode(node: hou.Node, promote_spare_parms: bool, immediately_save: bool) -> None: ...
def _openTypePropertiesDialogForNodeType(
    node_type: hou.NodeType, promote_spare_parms: bool, immediately_save: bool
) -> None: ...
def openRenderDialog(rop: hou.RopNode) -> None:
    """openRenderDialog(rop_node)

    Given a hou.RopNode instance, open the render control dialog for the
    node. This dialog can be used to override certain render parameters,
    and launch a render."""

def openRenameSelectedDialog(network: hou.Node) -> None:
    """openRenameSelectedDialog(node)

    Given a hou.OpNode which contains other nodes, open a dialog for
    renaming all selected children of the node. The dialog uses pattern
    matching to rename all the selected nodes in one operation."""

def openParameterInterfaceDialog(
    node: hou.Node, open_tab: Optional[hou.EnumValue] = None, open_tab_tree_path: Optional[str] = None
) -> None:
    """openParameterInterfaceDialog(node, open_tab = None, open_tab_tree_path =
    '')

        Given a hou.OpNode, open the parameter interface editor dialog. This
        dialog is can be used to add or remove spare parameters, or
        rearrange the parameter layout for a node.


        open_tab
            A hou.parameterInterfaceTabType enum value that causes the
            dialog to appear with a particular parameter source tab
            displayed.

        open_tab_tree_path
            If an open_tab is specified, this parameter can further control
            the state of the dialog when it opens. This string can specify a
            full path to a branch in the tree of the open tab which will be
            expanded and set as current."""

def updateMode() -> hou.EnumValue:
    """updateMode() -> hou.updateMode enum value

    This method is deprecated in favor of hou.updateModeSetting."""

def setUpdateMode(mode: hou.EnumValue) -> None:
    """setUpdateMode(mode)

    This method is deprecated in favor of hou.setUpdateMode."""

def triggerUpdate() -> None:
    """triggerUpdate()

    Force the viewports to update and perform any cooks necessary. You
    might call this function when Houdini's Auto Update mode is on
    Manual."""

def reloadViewportColorSchemes() -> None:
    """reloadViewportColorSchemes()

    Reloads all 3DSceneColors configuration files (in
    $HFS/houdini/config). You must cause the viewport to redraw (for
    example, by tumbling) to see the new colors.

    This function may be useful if you are implementing a new color
    scheme: you can map to a hotkey or call it in the Python console so
    you can check your changes."""

def reloadColorScheme() -> None:
    """reloadColorScheme()

    Reloads all Houdini UI color settings from the configuration files
    (by default, in $HFS/houdini/config and
    $HOUDINI_USER_PREF_DIR/houdini/config).

    This function may be useful if you are implementing a new color
    scheme: you can map to a hotkey or call it in the Python console so
    you can check your changes."""

def currentColorScheme() -> str:
    """currentColorScheme() -> str

    Return the currently applied Houdini color scheme name."""

def isAutoKey() -> bool:
    """isAutoKey() -> bool`

    Returns if auto-key is currently enabled (changing an animated
    parameter will create a key at the current frame if it doesn't
    exist)."""

def _getTabMenuIconSize() -> list[int]: ...
def removeAllSelectionCallbacks() -> None:
    """removeAllSelectionCallbacks()

    Remove all Python callbacks previously registered with
    hou.ui.addSelectionCallback. See hou.ui.addSelectionCallback for
    more information."""

def createDialog(ui_file_name: str) -> hou.Dialog:
    """createDialog(ui_file_name) -> hou.Dialog

    Parse the given .ui file and return the dialog defined in the file.

    The dialog must be written with Houdini's User Interface Script
    Language. An overview of the language can be found in the Houdini
    Development Kit (HDK) documentation, specifically in the Houdini
    User Interface -> The .ui Script Language section.

    ui_file_name is the basename of the .ui file. The file must be
    located in a directory registered with the HOUDINI_UI_APP_PATH
    search path. For a list of HOUDINI_UI_APP_PATH search directories,
    run hconfig -ap from a terminal.

    Raises hou.OperationFailed if the .ui file contains errors and the
    dialog could not be created. Raises TypeError if ui_file_name is
    None."""

def findDialog(ui_file_name: str) -> hou.Dialog:
    """findDialog(ui_file_name) -> hou.Dialog

    Return the dialog defined by the given .ui file name and created by
    hou.ui.createDialog.

    Return None if no dialog has been created with hou.ui.createDialog
    for the specified .ui file.

    Raises TypeError if ui_file_name is None."""

def dialogs() -> list[hou.Dialog]:
    """dialogs() -> tuple of hou.Dialog

    Return all dialogs created by hou.ui.createDialog."""

def writePythonShellHistoryFile(filename: Optional[str] = None) -> None:
    """writePythonShellHistoryFile(filename=None)

    Save the command history from the current Python Shell to disk. If
    filename is None, then the history is written to
    $HOME/houdiniX.Y/pyshell.history. If this function is invoked
    outside of a Python Shell, then the history is taken from the last
    active shell (i.e. the last shell that was opened or accepted
    input).

    Raises hou.OperationFailed if no Python Shell has been opened.
    Raises hou.OperationFailed if filename cannot be created."""

def readPythonShellHistoryFile(filename: Optional[str] = None) -> None:
    """readPythonShellHistoryFile(filename=None)

    Load the contents from the specified file into the command history
    of the Python Shell. If filename is None, then the history is read
    from $HOME/houdiniX.Y/pyshell.history. If this function is invoked
    outside of a Python Shell, then the history is loaded into the the
    last active shell (i.e. the last shell that was opened or accepted
    input).

    Raises hou.OperationFailed if no Python Shell has been opened.
    Raises hou.OperationFailed if filename does not exist or cannot be
    read."""

def setStatusMessage(*args: Any, **kwargs: Any) -> None:
    """setStatusMessage(message, severity=hou.severityType.Message)

    Display a message in Houdini's status bar.


    severity
        A hou.severityType enum value that determines the background
        color of the message.

    To clear the status bar, call hou.ui.setStatusMessage(\"\")."""

def statusMessage() -> tuple[str, hou.EnumValue]:
    """statusMessage() -> (string, hou.severityType)

    Return the current message and severity from the status bar. This
    may not match the value most recently passed to setStatusMessage
    because Houdini itself often changes the message in the status bar."""

def _processEvents() -> bool: ...
def openAssetUploadDialog(uploading_node: hou.Node, session_key: str, containing_node: hou.Node) -> None: ...
def openAssetDependenciesDialog(
    uploading_nodes: tuple[hou.Node], uploaded_nodes: tuple[hou.Node], session_key: str, containing_node: hou.Node
) -> None: ...
def hasDragSourceData(label: str) -> bool:
    """getDragSourceData(label, index) -> data

    Query the current drag source to obtain the dragged data. Returns
    None when the specified data in unavailable (or unsupported by HOM).

    Raises hou.NotAvailable if no drag operation is currently active.


    label
        Specifies the type of the source event to query. See
        hou.ui.hasDragSourceData for the label types to use.

    index
        Index of the data in the source. Defaults to 0."""

def getDragSourceData(label: str, index: int = 0) -> Any: ...
def resourceValueFromName(name: str) -> str:
    """resourceValueFromName(self, name) -> str

    Return a string value from a symbolic resource name. The resource
    name should correspond to one of the entries in the $HH/config/*.hcs
    file for the currently selected color scheme.

    Raises: hou.ValueError if the provided symbolic name doesn't exist."""

def colorFromName(name: str) -> hou.Color:
    """colorFromName(self, name) -> hou.Color

      Return a color value from a symbolic color name. The color name
      should correspond to one of the entries in the $HH/config/*.hcs file
      for the currently selected color scheme.

      Raises: hou.ValueError if the provided symbolic name doesn't exist.

      For example:

    > >>> hou.ui.colorFromName(\"DisplayOnColor\")
    > <hou.Color r=0.3, g=0.5, b=1>

      TIP
          You can use hou.qt.getColor to get a Qt color object instead of
          a HOM color object."""

def globalScaleFactor() -> float:
    """globalScaleFactor(self) -> float

      Return the scale factor that is set by Houdini's Global UI Size
      preference. For example, this function returns 1.0 when Houdini is
      set to the Normal UI size.

      The scale factor can be used to scale components in a PySide or PyQt
      built UI where hou.ui.scaledSize cannot be called. For example, the
      scale factor can be used to set the zoom factor of a QWebEngineView
      object so that the web contents match the Global UI Size:

    > web_view = QWebEngineWidgets.QWebEngineView()
    > web_view.setZoomFactor(hou.ui.globalScaleFactor())"""

def scaledSize(size: int) -> int:
    """scaledSize(self, size) -> int

      Scale the specified size by the global UI scale factor and return
      the scaled size. The scale factor is determined by Houdini's Global
      UI Size preference. For example, the factor is 1.0 when Houdini is
      set to the Normal UI size.

      This function is useful for scaling hard-coded sizes in PySide or
      PyQt code. Here is an example of using scaled sizes when setting a
      widget to a fixed size that is 640x480 with the Normal UI size:

    > widget = QtWidgets.QWidget()
    > widget.resize(hou.ui.scaledSize(640), hou.ui.scaledSize(480))

      Here is another example of creating a scaled icon using the
      hou.qt.createIcon function:

    > icon = hou.qt.createIcon(hou.ui.scaledSize(32), hou.ui.scaledSize(32))"""

def inchesToPixels(inches: float) -> float:
    """inchesToPixels(self, inches) -> float

    Return the supplied inches argument, expressing a distance on the
    screen, converted to a number of pixels. This calculation combines
    the number of dots per inch reported by the operating system, the
    Global UI Size setting accessible from Edit > Preferences > General
    User Interface, and the HOUDINI_UISCALE environment variable, if it
    has been set. As such, this value may not be accurate, but is
    consistent with the way the rest of Houdini converts distances from
    inches to pixels."""

def pixelsToInches(pixels: float) -> float:
    """pixelsToInches(self, pixels) -> float

    Return the supplied pixels argument, expressing a number of pixels
    on the screen, converted to a distance in inches. This calculation
    combines the number of dots per inch reported by the operating
    system, the Global UI Size setting accessible from Edit >
    Preferences > General User Interface, and the HOUDINI_UISCALE
    environment variable, if it has been set. As such, this value may
    not be accurate, but is consistent with the way the rest of Houdini
    converts distances from pixels to inches."""

def copyTextToClipboard(text: str) -> None:
    """copyTextToClipboard(self, text)

    Sets the supplied text into the system clipboard."""

def getTextFromClipboard() -> str:
    """getTextFromClipboard(self) -> str

    Returns any text currently copied into the system clipboard. If the
    clipboard is empty or contains non-text data, an empty string is
    returned."""

def hotkeys(hotkey_symbol: str) -> list[str]:
    """hotkeys(self, hotkey_symbol) -> tuple of str

      Return a tuple of strings that represent the hotkeys currently
      assigned to the action associated with the hotkey symbol. The hotkey
      symbols can be found in the $HH/config/Hotkeys directory.

      Raises: hou.ValueError if the provided hotkey symbol doesn't exist.

      For example:

    > >>> hou.ui.hotkeys(\"h.copy\")
    > ('Alt+C', 'Ctrl+C')
    > >>> hou.ui.hotkeys(\"h.pane.copytab\")
    > ('Ctrl+T',)"""

def hotkeyDescription(hotkey_symbol: str) -> str:
    """hotkeyDescription(self, hotkey_symbol) -> str

      Return a string that contains a description of the action associated
      with the hotkey symbol. The hotkey symbols can be found in the
      $HH/config/Hotkeys directory.

      Raises: hou.ValueError if the provided hotkey symbol doesn't exist.

      For example:

    > >>> hou.ui.hotkeyDescription(\"h.pane.copytab\")
    > 'Copy Tab'"""

def isKeyMatch(key: str, hotkey_symbol: str) -> bool:
    """isKeyMatch(self, key, hotkey_symbol) -> bool

      Return True if the key described by the string key matches one of
      the hotkeys assigned to the provided hotkey symbol. The hotkey
      symbols can be found in the $HH/config/Hotkeys directory.

      Raises: hou.ValueError if the provided hotkey symbol doesn't exist,
      or the key string doesn't represent a valid hotkey.

      For example:

    > >>> hou.ui.isKeyMatch(\"Ctrl+C\", \"h.copy\")
    > True
    > >>> hou.ui.isKeyMatch(\"Ctrl+C\", \"h.pane.copytab\")
    > False"""

def _geoSpreadsheetCellText(sheet_id: int, row: int, col: int) -> str: ...
def openCaptureWeightSpreadsheet(node: hou.Node, pattern: Optional[str] = None) -> None:
    """openCaptureWeightSpreadsheet(node, pattern=None)

    Given an instance of a hou.SopNode that is a captureoverride type,
    open the edit capture weight spreadsheet for the node. If a string
    is passed for pattern, then only the points specified by the pattern
    will be shown, otherwise all the points for the node will be
    displayed in the spreadsheet."""

def _openCaptureWeightSpreadsheet2(node: hou.Node) -> str: ...
def _closeCaptureWeightSpreadsheet(identifier: str) -> None: ...
def registerViewerState(vs_templ: hou.ViewerStateTemplate) -> None:
    """registerViewerState(template)

    Registers a hou.ViewerStateTemplate object representing a custom
    viewer state. See installing viewer states for how to use this
    function.


    template
        The hou.ViewerStateTemplate object.

    Raises hou.NameConflict if the registration fails because a state
    with the same name is already registered. Raises hou.OperationFailed
    if the registration fails (for example, the state to register has no
    factory)."""

def registerViewerStateFile(state_file: str) -> None:
    """registerViewerStateFile(file_path)

    Registers a viewer state type implemented in a given python file.
    Any viewer state previously registered by this file will be
    unregistered first.

    See installing viewer states for more details about python state
    files.


    file_path
        A full path to the python file containing the viewer state.

    Raises hou.OperationFailed if the registration fails (for example,
    the state to register has no factory)."""

def registerViewerStates() -> None:
    """registerViewerStates()

    Scans the viewer state folders ($HH/viewer_states and
    $HOUDINI_USER_PREF_DIR/viewer_states) to register all viewer states
    they both contain. Viewer states already registered in Houdini are
    simply updated with the version on disk."""

def unregisterViewerState(state_typename: str) -> None:
    """unregisterViewerState(state_name)

    Unregisters an existing viewer state type.

    See installing viewer states for how to use this function.


    state_name
        The name of the state to unregister.

    Raises hou.OperationFailed if the unregistration fails (for example,
    if no state with the given name is registered)."""

def unregisterViewerStateFile(state_file: str) -> None:
    """unregisterViewerStateFile(file_path)

    Unregisters a viewer state previously registered with a given python
    file. See installing viewer states for more details about python
    state files.


    file_path
        A full path to the python file referring to a viewer state.

    Raises hou.OperationFailed if the unregistration fails (for example,
    if no state was registered with this file)."""

def isRegisteredViewerState(state_name: str) -> bool:
    """isRegisteredViewerState(state_name) -> bool

    Returns True if state_name has previously been registered with
    hou.ui.registerViewerState. Returns False if not.


    state_name
        The name of the state to validate."""

def reloadViewerState(state_typename: str) -> None:
    """reloadViewerStates(state_names=None)

    Reload multiple viewer states as specified in the state_names array.
    If the array is empty, all registered self-installed states in
    Houdini are reloaded. See hou.ui.reloadViewerState for more details
    on reloading a state.


    state_names
        Array of state names to reload. Empty by default.

    Raises hou.OperationFailed if the reload fails (for example, if no
    state with a given name is registered)."""

def reloadViewerStates(*args: Any, **kwargs: Any) -> None: ...
def viewerStateInfo(*args: Any, **kwargs: Any) -> str:
    """viewerStateInfo(state_names) -> str

      Return a JSON dictionary string describing all registered viewer
      states keyed by state type.


      state_names
          Array of state names to process. If the array is empty
          (default), all viewer states currently registered are processed.

    > import json
    >
    > info_str = hou.ui.viewerStateInfo([\"sidefx_stroke\"])
    > info_dict = json.loads(info_str)
    > info = json.dumps(info_dict[\"sidefx_stroke\"], indent=3)
    > print(info)
    >
    > {
    >    \"Type\": \"sidefx_stroke\",
    >    \"Label\": \"Stroke\",
    >    \"Icon\": \"$HFS/houdini/pic/minimizedicon.pic\",
    >    \"Category\": \"Sop\",
    >    \"Source\": \"$HFS/houdini/viewer_states/sidefx_stroke.py\",
    >    \"Contexts\": [
    >       \"SOP\"
    >    ],
    >    \"Handles\": {},
    >    \"Gadgets\": {},
    >    \"Selectors\": {
    >       \"sidefx_default_selector\": {
    >          \"Name\": \"sidefx_default_selector\",
    >          \"Auto start\": false,
    >          \"Hotkey\": {
    >             \"Path\": \"\",
    >             \"Label\": \"\",
    >             \"Description\": \"\",
    >             \"Keys\": []
    >          },
    >          \"Secure selection\": \"obey\",
    >          \"Prompt\": \"default geometry selector\",
    >          \"Allow drag\": false,
    >          \"Quick select\": true,
    >          \"Use existing selection\": true,
    >          \"Initial selection\": \"\",
    >          \"Initial selection type\": \"\",
    >          \"Ordered\": false,
    >          \"Geometry types\": [],
    >          \"Allow other sops\": true
    >       }
    >    },
    >    \"Menus\": {
    >       \"Stroke\": {
    >          \"Type\": \"Menu\",
    >          \"Handle\": \"stroke_menu\",
    >          \"Draw realtime\": {
    >             \"Type\": \"Toggle\",
    >             \"Handle\": \"realtime_mode\",
    >             \"Hotkey\": {
    >                \"Path\": \"h.pane.gview.state.sop.sidefx_stroke.realtime_mode\",
    >                \"Label\": \"realtime\",
    >                \"Description\": \"Enable realtime mode\",
    >                \"Keys\": [
    >                   48
    >                ]
    >             }
    >          },
    >          \"Brush settings...\": {
    >             \"Type\": \"Menu\",
    >             \"Handle\": \"brush_menu\",
    >             \"Cycle brushes\": {
    >                \"Type\": \"Action\",
    >                \"Handle\": \"cycle_brushes\",
    >                \"Hotkey\": {
    >                   \"Path\": \"h.pane.gview.state.sop.sidefx_stroke.cycle_brushes\",
    >                   \"Label\": \"Cycle brushes\",
    >                   \"Description\": \"Cycle stroke tools\",
    >                   \"Keys\": [
    >                      49
    >                   ]
    >                }
    >             },
    >             \"Brush display mode\": {
    >                \"Type\": \"Radio strip\",
    >                \"Handle\": \"brush_display_mode\",
    >                \"Default\": \"brush_viewport_display\",
    >                \"Wireframe\": {
    >                   \"Type\": \"Radio strip item\",
    >                   \"Handle\": \"brush_wireframe_display\",
    >                   \"Hotkey\": {
    >                      \"Path\": \"h.pane.gview.state.sop.sidefx_stroke.set_wireframe_brush\",
    >                      \"Label\": \"Set wireframe brush\",
    >                      \"Description\": \"Set wireframe brush\",
    >                      \"Keys\": [
    >                         50
    >                      ]
    >                   }
    >                },
    >                \"Viewport\": {
    >                   \"Type\": \"Radio strip item\",
    >                   \"Handle\": \"brush_viewport_display\",
    >                   \"Hotkey\": {
    >                      \"Path\": \"h.pane.gview.state.sop.sidefx_stroke.set_viewport_brush\",
    >                      \"Label\": \"Set viewport brush\",
    >                      \"Description\": \"Set viewport brush\",
    >                      \"Keys\": [
    >                         51
    >                      ]
    >                   }
    >                }
    >             }
    >          }
    >       }
    >    }
    > }"""

def viewerStateInfoFromFile(state_file: str) -> tuple[str, str]:
    """viewerStateInfoFromFile(state_filepath) -> (str, str)

      Returns the viewer state information for a given python state file.
      The information is returned as a tuple containing the python state
      type name and a JSON dictionary string describing the registered
      viewer state information.


      state_filepath
          A python state file path. The method returns an empty tuple if
          the file path is not a python state file or the python state
          contained in the file is not registered.


      NOTE
          This method doesn't work with HDA python state files.

    > import json
    >
    > (state_type, info_str) = hou.ui.viewerStateInfoFromFile(
    >     \"$HFS/packages/viewer_state_demo/viewer_states/drawable_selector_sop.py\"
    > )
    > info_dict = json.loads(info_str)
    > info = json.dumps(info_dict[state_type], indent=3)
    > print(info)
    >
    > {
    >    \"Type\": \"drawable_selector_sop\",
    >    \"Label\": \"State Drawable Selector Demo\",
    >    \"Icon\": \"DESKTOP_application_mac\",
    >    \"Category\": \"Sop\",
    >    \"Source\": \"$HFS/packages/viewer_state_demo/viewer_states/drawable_selector_sop.py\",
    >    \"Contexts\": [
    >       \"SOP\"
    >    ],
    >    \"Handles\": {},
    >    \"Gadgets\": {},
    >    \"Selectors\": {
    >       \"drawable_selector\": {
    >          \"Name\": \"drawable_selector\",
    >          \"Auto start\": true,
    >          \"Hotkey\": {
    >             \"Path\": \"h.pane.gview.state.sop.drawable_selector_sop.drawable selector\",
    >             \"Label\": \"drawable selector\",
    >             \"Description\": \"drawable selector\",
    >             \"Keys\": [
    >                49
    >             ]
    >          },
    >          \"Secure selection\": \"ignore\",
    >          \"Prompt\": \"Select a drawable component\",
    >          \"Allow drag\": false,
    >          \"Quick select\": true,
    >          \"Use existing selection\": true,
    >          \"Initial selection\": \"\",
    >          \"Initial selection type\": \"\",
    >          \"Ordered\": false,
    >          \"Geometry types\": [
    >             \"point\",
    >             \"edge\",
    >             \"prim\"
    >          ],
    >          \"Allow other sops\": false
    >       },
    >       \"primitive_selector\": {
    >          \"Name\": \"primitive_selector\",
    >          \"Auto start\": false,
    >          \"Hotkey\": {
    >             \"Path\": \"h.pane.gview.state.sop.drawable_selector_sop.primitive selector\",
    >             \"Label\": \"primitive selector\",
    >             \"Description\": \"primitive selector\",
    >             \"Keys\": [
    >                50
    >             ]
    >          },
    >          \"Secure selection\": \"ignore\",
    >          \"Prompt\": \"Select a primitive component\",
    >          \"Allow drag\": true,
    >          \"Quick select\": true,
    >          \"Use existing selection\": true,
    >          \"Initial selection\": \"\",
    >          \"Initial selection type\": \"\",
    >          \"Ordered\": false,
    >          \"Geometry types\": [
    >             \"prim\"
    >          ],
    >          \"Allow other sops\": false
    >       },
    >       \"sidefx_default_selector\": {
    >          \"Name\": \"sidefx_default_selector\",
    >          \"Auto start\": false,
    >          \"Hotkey\": {
    >             \"Path\": \"\",
    >             \"Label\": \"\",
    >             \"Description\": \"\",
    >             \"Keys\": []
    >          },
    >          \"Secure selection\": \"obey\",
    >          \"Prompt\": \"default geometry selector\",
    >          \"Allow drag\": false,
    >          \"Quick select\": true,
    >          \"Use existing selection\": true,
    >          \"Initial selection\": \"\",
    >          \"Initial selection type\": \"\",
    >          \"Ordered\": false,
    >          \"Geometry types\": [],
    >          \"Allow other sops\": true
    >       }
    >    },
    >    \"Menus\": {
    >       \"Drawable Selector Demo\": {
    >          \"Type\": \"Menu\",
    >          \"Handle\": \"drawable_selector_menu\",
    >          \"Log Info\": {
    >             \"Type\": \"Toggle\",
    >             \"Handle\": \"log_info\",
    >             \"Hotkey\": {
    >                \"Path\": \"\",
    >                \"Label\": \"\",
    >                \"Description\": \"\",
    >                \"Keys\": []
    >             }
    >          },
    >          \"Clear Console\": {
    >             \"Type\": \"Action\",
    >             \"Handle\": \"clear_console\",
    >             \"Hotkey\": {
    >                \"Path\": \"\",
    >                \"Label\": \"\",
    >                \"Description\": \"\",
    >                \"Keys\": []
    >             }
    >          }
    >       }
    >    }
    > }"""

def viewerHandleInfo(*args: Any, **kwargs: Any) -> str:
    """viewerHandleInfo(handle_names) -> string

      Return a JSON dictionary string describing all registered viewer
      handles in Houdini. The viewer handles can be queried by type name.


      handle_names
          Array of handle type names. The function returns a dictionary
          containing all registered handles specified in the array. If the
          array is empty (default), all registered viewer handles are
          returned.

    >     >>> import ast
    >     >>> viewer_handles = ast.literal_eval(hou.ui.viewerHandleInfo())
    >     >>> viewer_handles[\"move_tool_handle\"]
    > {
    >    \"Gadgets\":{
    >       \"zdisc\":{
    >          \"Drawable\":\"Line\",
    >          \"Name\":\"zdisc\",
    >          \"Label\":\"Z\"
    >       },
    >       \"yscale\":{
    >          \"Drawable\":\"Face\",
    >          \"Name\":\"yscale\",
    >          \"Label\":\"Y\"
    >       },
    >       \"yaxis\":{
    >          \"Drawable\":\"Line\",
    >          \"Name\":\"yaxis\",
    >          \"Label\":\"Y\"
    >       },
    >       \"zscale\":{
    >          \"Drawable\":\"Face\",
    >          \"Name\":\"zscale\",
    >          \"Label\":\"Z\"
    >       },
    >       \"zaxis\":{
    >          \"Drawable\":\"Line\",
    >          \"Name\":\"zaxis\",
    >          \"Label\":\"Z\"
    >       },
    >       \"xaxis\":{
    >          \"Drawable\":\"Line\",
    >          \"Name\":\"xaxis\",
    >          \"Label\":\"X\"
    >       },
    >       \"xscale\":{
    >          \"Drawable\":\"Face\",
    >          \"Name\":\"xscale\",
    >          \"Label\":\"X\"
    >       },
    >       \"pivot\":{
    >          \"Drawable\":\"Face\",
    >          \"Name\":\"pivot\",
    >          \"Label\":\"XYZ\"
    >       },
    >       \"xdisc\":{
    >          \"Drawable\":\"Line\",
    >          \"Name\":\"xdisc\",
    >          \"Label\":\"X\"
    >       },
    >       \"ydisc\":{
    >          \"Drawable\":\"Line\",
    >          \"Name\":\"ydisc\",
    >          \"Label\":\"Y\"
    >       }
    >    },
    >    \"Parameters\":{
    >       \"Sz\":{
    >          \"Default\":1,
    >          \"Range\":\"(0.1, 10)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"sz\",
    >          \"Label\":\"Sz\"
    >       },
    >       \"Sy\":{
    >          \"Default\":1,
    >          \"Range\":\"(0.1, 10)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"sy\",
    >          \"Label\":\"Sy\"
    >       },
    >       \"Sx\":{
    >          \"Default\":1,
    >          \"Range\":\"(0.1, 10)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"sx\",
    >          \"Label\":\"Sx\"
    >       },
    >       \"Tz\":{
    >          \"Default\":0,
    >          \"Range\":\"(-10, 10)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"tz\",
    >          \"Label\":\"Tz\"
    >       },
    >       \"Tx\":{
    >          \"Default\":0,
    >          \"Range\":\"(-10, 10)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"tx\",
    >          \"Label\":\"Tx\"
    >       },
    >       \"Ty\":{
    >          \"Default\":0,
    >          \"Range\":\"(-10, 10)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"ty\",
    >          \"Label\":\"Ty\"
    >       },
    >       \"Rx\":{
    >          \"Default\":0,
    >          \"Range\":\"(0, 360)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"rx\",
    >          \"Label\":\"Rx\"
    >       },
    >       \"Ry\":{
    >          \"Default\":0,
    >          \"Range\":\"(0, 360)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"ry\",
    >          \"Label\":\"Ry\"
    >       },
    >       \"Rz\":{
    >          \"Default\":0,
    >          \"Range\":\"(0, 360)\",
    >          \"Type\":\"Float\",
    >          \"Name\":\"rz\",
    >          \"Label\":\"Rz\"
    >       }
    >    },
    >    \"Settings\":{
    >       \"\":{
    >          \"Type\":\"Separator\",
    >          \"Name\":\"separator0\",
    >          \"Label\":\"\"
    >       },
    >       \"Drag Along Plane\":{
    >          \"Default\":\"XZ\",
    >          \"Menu Items\":[
    >             \"(XZ, XZ)\",
    >             \"(XY, XY)\",
    >             \"(ZY, ZY)\",
    >             \"(XYZ, XYZ)\"
    >          ],
    >          \"Type\":\"Menu\",
    >          \"Name\":\"planes\",
    >          \"Label\":\"Drag Along Plane\"
    >       },
    >       \"Draw dimension lines\":{
    >          \"Default\":1,
    >          \"Type\":\"Toggle\",
    >          \"Name\":\"dimensions\",
    >          \"Label\":\"Draw dimension lines\"
    >       }
    >    },
    >    \"Menus\":{
    >       \"Move Tool Handle\":{
    >          \"Cycle Gadgets\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   89
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.cycle\",
    >                \"Description\":\"cycle\",
    >                \"Label\":\"cycle\"
    >             },
    >             \"Handle\":\"cycle\",
    >             \"Type\":\"Action\"
    >          },
    >          \"Handle\":\"move_tool_handle_menu\",
    >          \"Trace\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   51
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.trace_handle\",
    >                \"Description\":\"Enable handle trace\",
    >                \"Label\":\"Trace\"
    >             },
    >             \"Handle\":\"trace_handle\",
    >             \"Type\":\"Toggle\"
    >          },
    >          \"Edit\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   53
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.edit_handle\",
    >                \"Description\":\"Edit Handle\",
    >                \"Label\":\"Edit\"
    >             },
    >             \"Handle\":\"edit_handle\",
    >             \"Type\":\"Action\"
    >          },
    >          \"XYZ\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   65
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.XYZ\",
    >                \"Description\":\"XYZ\",
    >                \"Label\":\"XYZ\"
    >             },
    >             \"Handle\":\"XYZ\",
    >             \"Type\":\"Action\"
    >          },
    >          \"Inspect\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   50
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.inspect_handle\",
    >                \"Description\":\"Inspect Handle\",
    >                \"Label\":\"Inspect\"
    >             },
    >             \"Handle\":\"inspect_handle\",
    >             \"Type\":\"Action\"
    >          },
    >          \"XZ\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   70
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.XZ\",
    >                \"Description\":\"XZ\",
    >                \"Label\":\"XZ\"
    >             },
    >             \"Handle\":\"XZ\",
    >             \"Type\":\"Action\"
    >          },
    >          \"Reload\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   54
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.reload_handle\",
    >                \"Description\":\"Reload Handle\",
    >                \"Label\":\"Reload\"
    >             },
    >             \"Handle\":\"reload_handle\",
    >             \"Type\":\"Action\"
    >          },
    >          \"XY\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   71
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.XY\",
    >                \"Description\":\"XY\",
    >                \"Label\":\"XY\"
    >             },
    >             \"Handle\":\"XY\",
    >             \"Type\":\"Action\"
    >          },
    >          \"ZY\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   66
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.ZY\",
    >                \"Description\":\"ZY\",
    >                \"Label\":\"ZY\"
    >             },
    >             \"Handle\":\"ZY\",
    >             \"Type\":\"Action\"
    >          },
    >          \"Clear console\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   49
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.clear_console\",
    >                \"Description\":\"Clear console\",
    >                \"Label\":\"Clear\"
    >             },
    >             \"Handle\":\"clear_console\",
    >             \"Type\":\"Action\"
    >          },
    >          \"Marker\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   52
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.add_marker\",
    >                \"Description\":\"Add Marker\",
    >                \"Label\":\"Marker\"
    >             },
    >             \"Handle\":\"add_marker\",
    >             \"Type\":\"Action\"
    >          },
    >          \"Logging\":{
    >             \"Hotkey\":{
    >                \"Keys\":[
    >                   48
    >                ],
    >                \"Path\":\"h.pane.gview.handle.move_tool_handle.console_logging\",
    >                \"Description\":\"Enable or disable console logging\",
    >                \"Label\":\"Logging\"
    >             },
    >             \"Handle\":\"console_logging\",
    >             \"Type\":\"Toggle\"
    >          },
    >          \"Type\":\"Menu\"
    >       }
    >    },
    >    \"Label\":\"Move Tool Handle\",
    >    \"Exported Parameters\":[
    >       \"tx\",
    >       \"ty\",
    >       \"tz\",
    >       \"rx\",
    >       \"ry\",
    >       \"rz\",
    >       \"sx\",
    >       \"sy\",
    >       \"sz\"
    >    ],
    >    \"Source\":\"C:/Users/marcb/DEV/HOUDINI/dev/hfs/packages/viewer_handle_demo/viewer_handles/move_tool_handle.py\",
    >    \"Type\":\"move_tool_handle\",
    >    \"Categories\":[
    >       \"Sop\"
    >    ],
    >    \"Icon\":\"$HFS/houdini/pic/Mandril.pic\"
    > }"""

def printResourceMessage(*args: Any, **kwargs: Any) -> None:
    """printResourceMessage(resource_type, message,
    message_type=hou.severityType.Message)

        Print a user message in the message window of a Viewer State Browser
        or Viewer Handle Browser. The
        hou.resourceEventMessage.OnPrintMessage event is sent when calling
        this function.


        resource_type
            A resource type to choose the browser console. Use
            hou.resourceType.ViewerState to print messages in the Viewer
            State Browser or hou.resourceType.ViewerHandle for the Viewer
            Handle Browser.

        message
            String message to print.

        message_type
            Type of message to print. Fatal and Important types are ignored
            and default to Message."""

def fireResourceCustomEvent(resource_type: hou.EnumValue, user_data: dict[str, Any], queue: bool = True) -> None:
    """fireResourceCustomEvent(resource_type, user_data, queue=True)

      This function triggers a custom resource event which can be used for
      implementing specific workflows. Client callbacks registered with
      hou.ui.addResourceEventCallback will get notified with the input
      user_data argument. The event can be processed immediately or later
      when Houdini is idle, see the queue argument for details.


      resource_type
          The event resource type.

      user_data
          A dictionary mapping user-defined entries to values of type int,
          double, bool and string. An exception is raised if user_data is
          empty or contains unsupported value types.


          fireResourceCustomEvent will add the following entries to the
          dictionary
              resource_type: The resource_type argument value. event_type:
              OnCustomEvent event type.

      queue
          If True (default), the event is put on a queue and processed
          when Houdini is idle. If False, the event is processed
          immediately.

      Here's how a custom event can be used.

    >
    > # Register a callback for viewer state events
    > hou.ui.addResourceEventCallback(myEventHandler)
    >
    > def myEventHandler(**kwargs):
    >     import json
    >     if kwargs['event_type'] == hou.resourceEventMessage.OnCustomEvent:
    >         if 'load_file' in kwargs:
    >             # load a json file and store results
    >             with open(kwargs['load_file']) as file:
    >                 json_values = json.load(file)
    >         elif 'save_file' in kwargs:
    >             # save json_values to a json file
    >             with open(kwargs['save_file'], 'w') as file:
    >                 json.dump(json_values, file, indent=3)
    >
    >     # process other non-custom viewer state events
    >     elif kwargs['event_type'] == hou.resourceEventMessage.OnEnter:
    >         pass
    >
    > ...
    > # load a json file via a custom event
    > hou.ui.fireResourceCustomEvent( hou.resourceType.ViewerState, { 'load_file': '/var/tmp/somefile.json'} )"""

def showInFileBrowser(file_path: str) -> None:
    """showInFileBrowser(file_path)

    Launch the system's file browser, navigating to the parent directory
    of the specified file and selecting it.


    file_path
        A string representing the full path to the file (or directory)
        to select.


        TIP
            If you do not want any file selected, simply ensure the
            filepath ends with a /.

        Examples:

      > # Launch the browser in /home/me/myDocs and select doc1.txt
      > hou.ui.showInFileBrowser('/home/me/myDocs/doc1.txt')
      >
      > # Launch the browser in /home/me/myDocs and select nothing
      > hou.ui.showInFileBrowser('/home/me/myDocs/')
      >
      > # Launch the browser in /home/me and select myDocs
      > hou.ui.showInFileBrowser('/home/me/myDocs')"""

def showFloatingParameterEditor(node: hou.Node, reuse: bool = True) -> hou.ParameterEditor:
    """showFloatingParameterEditor(node,reuse) -> hou.ParameterEditor

    Show a floating hou.ParameterEditor for a given hou.OpNode."""

def openParameterExpressionEditor(parm: hou.Parm) -> None:
    """openParameterExpressionEditor(parm)

    Open the expression editor to edit the expression of the given
    parameter.


    parm
        hou.Parm The parm whose expression to edit."""

def openPreferences(page: str, label: str) -> None:
    """openPreferences(page)

    Open the preferences dialog and show the given page.


    page
        A string that specifies the preference page to open. When there
        are tabs under the page, page:tab notation is used.

        The following values are supported:

        ui

        General User Interface

        network

        Network Editor

        viewport

        3D Viewports

        shelves

        Shelf Tools and Tab Menu

        takes

        Takes

        anim

        Animation

        lighting

        Lighting

        rendering

        Rendering

        handles

        Handles

        hud

        HUD Info

        hud_handles

        HUD Handles

        states

        Interactive Tools

        objsops

        Objects and Geometry

        objsops:preferences

        Objects and Geometry > Preferences

        objsops:sop_cache

        Objects and Geometry > SOP Cache

        objsops:obj_cache

        Objects and Geometry > OBJ Cache

        chops

        Motion and Audio

        composites

        Compositing

        composites:cache

        Compositing > Cache

        composites:cooking

        Compositing > Cooking

        composites:interactive

        Compositing > Interactive

        composites:selectors

        Compositing > Selectors

        composites:names

        Compositing > Names

        composites:colors

        Compositing > Colors

        composites:cineon

        Compositing > Cineon

        scripting

        Scripting

        resmgr

        Desktops and Toolbars

        persistence

        Save and Load Options

        hipoptions

        Hip File Options

        warnings

        Warning Dialogs

        notifications

        Notifications

        perfmon

        Performance Options

        exttools

        External Tools

        misc

        Miscellaneous"""

def hideAllMinimizedStowbars() -> bool:
    """hideAllMinimizedStowbars(self) -> bool

    Return the value of a global flag that hides all the minimized
    stowbars and split panes."""

def setHideAllMinimizedStowbars(hide: bool) -> None:
    """setHideAllMinimizedStowbars(self,on) -> bool

    Set the value of a global flag that hides all the minimized stowbars
    and split panes. When the flag is on, the minimized stowbars of all
    pane tabs ,menus , the shelf dock or toolbars will be hidden. It
    also affect the split bars of split panes, in which case, the split
    is rendered using a single pixel line."""

def registerViewerHandle(tmpl: hou.ViewerHandleTemplate) -> None:
    """registerViewerHandle(template)

      Registers a hou.ViewerHandleTemplate object representing a custom
      viewer handle. See installing viewer handle for how to use this
      function.


      template
          The hou.ViewerHandleTemplate object.

      Raises these exceptions if the registration fails:

    * hou.NameConflict if a handle with the same name is already
      registered.

    * hou.OperationFailed if the registration fails (for example, the
      handle to register has no factory)."""

def registerViewerHandles() -> None:
    """registerViewerHandles()

    Scans the viewer handle folders (e.g. $HH/viewer_handles and
    $HOUDINI_USER_PREF_DIR/viewer_handles) to register all viewer
    handles they both contain. Viewer handles already registered in
    Houdini are simply updated with the version on disk."""

def registerViewerHandleFile(handle_file: str) -> None:
    """registerViewerHandleFile(handle_file)

    Registers a viewer handle type implemented in a given python file.
    Any viewer handle previously registered by this file will be
    unregistered first.

    See installing viewer handles for more details about python handle
    files.


    file_path
        A full path to the python file containing the viewer handle
        implementation.

    Raises hou.OperationFailed if the registration fails (for example,
    the handle to register has no factory)."""

def unregisterViewerHandle(handle_name: str) -> None:
    """unregisterViewerHandle(handle_name)

    Unregisters an existing viewer handle type.

    See installing viewer handles for how to use this function.


    handle_name
        The name of the handle to unregister.

    Raises hou.OperationFailed if the unregistration fails (for example,
    if no handle with the given name is registered)."""

def unregisterViewerHandleFile(handle_file: str) -> None:
    """unregisterViewerHandleFile(handle_file)

    Unregisters a viewer handle previously registered with a given
    python file. See installing viewer handles for more details about
    python handle files.


    file_path
        A full path to the python file referring to a viewer handle.

    Raises hou.OperationFailed if the unregistration fails (for example,
    if no handle was registered with this file)."""

def isRegisteredViewerHandle(handle_name: str) -> bool:
    """isRegisteredViewerHandle(handle_name) -> bool

    Returns True if handle_name has previously been registered with
    hou.ui.registerViewerHandle. Returns False if not.


    handle_name
        The type name of the viewer handle to validate."""

def reloadViewerHandle(handle_name: str) -> None:
    """reloadViewerHandle(handle_name)

    Update a registered viewer handle by reloading its python module
    file from a viewer_handle folder. See installing handles in Houdini
    for more details.


    WARNING
        If you get an error message about a registration problem during
        a reload like the following,

        Error registering 'my_handle': factory not specified or invalid.

        Houdini will make its best to keep the broken viewer handle in
        the Viewer Handle Browser for editing the file. If not, the
        handle will be removed from Houdini and you will be forced to
        quit Houdini to fix the problem.


    handle_name
        The type name of the handle to reload.

    Raises hou.OperationFailed if the reload fails (for example, if no
    state with the given name is registered)."""

def loadPackage(package_filepath: str) -> None:
    """loadPackage(file_path)

      Packages are normally loaded on startup by Houdini, this API loads
      packages at runtime. loadPackage is typically used for loading
      resource files installed in a plugin folder. A plugin package file
      would typically set HOUDINI_PATH with the folder path containing the
      resource files. loadPackage will load and install the resources
      found in HOUDINI_PATH.


      file_path
          A full file path pointing to the package file to load.

      The following resource types are supported. The resource files must
      be installed in a subfolder as specified in this table:

      Desktops
      desktop

      Contains .desk file(s).

      Digital assets
      otls

      Contains HDA files along with OPlibraries files.

      Python modules
      pythonX.Ylibs

      Contains .py files. You are responsible to provide the python
      modules in the right platform folder. The system python path will be
      updated with the folder path.

      Python panels
      python_panels

      Contains .pypanel file(s).

      Shelf tools
      toolbar

      Contains .shelf file(s). The shelf tools are loaded but not active
      in a shelf set.

      Viewer states
      viewer_states

      Contains python states implementation files.

      Viewer handles
      viewer_handles

      Contains python handles implementation files.

      The following shows how to setup a plugin package folder by using
      the viewer handle demo package as example.

      The package file adds the folder path to HOUDINI_PATH:

    > > cat $HFS/houdini/viewer_handles/viewer_handle_demo.json
    > {
    >     \"path\" : \"$HFS/packages/viewer_handle_demo\"
    > }

      The viewer handle demo folder layout:

    > $HFS/packages/viewer_handle_demo/
    >     pythonX.Ylibs/
    >         move_tool_demo/
    >             utils.py
    >     scenes/
    >         move_tool_demo.hip
    >         viewer_handle_demo.hip
    >     toolbar/
    >         viewer_handle_demo.shelf
    >     viewer_handles/
    >         move_tool_handle.py
    >         viewer_handle_intro1.py
    >         viewer_handle_intro2.py
    >         viewer_handle_intro3.py"""

def loadPackageArchive(*args: Any, **kwargs: Any) -> list[str]:
    """loadPackageArchive(file_path, extract_path=None) -> list of string

    Extracts the content of a package archive file on disk and load the
    embedded packages. A package archive can be used to install multiple
    plugins in the user folder (default) or optionally in a folder of
    your choice. An exception is raised if the archive installation
    directory is read-only. The loaded package paths are returned in a
    list.


    NOTE
      * The package files must be added at the root level of the
        archive, do not put package files in a packages folder.

      * The resource files must be added in the archive subfolders as
        documented in hou.ui.loadPackage.

      * File or folder links are not permitted.

      * By default Houdini installs the archive in
        $HOUDINI_USER_PREF_DIR under a sub-folder with the name of the
        archive file. For instance, myarchive.zip would be installed in
        $HOUDINI_USER_PREF_DIR/myarchive.

      * The supported archive format is ZIP, other formats may be added
        in the future.


    file_path
        A file path pointing to a package archive file.

    extract_path
        Optional folder path to extract the files."""

def unloadPackage(package_filepath: str) -> None:
    """unloadPackage(file_path)

    Unloads (or removes) the resources previously loaded.


    file_path
        A full file path pointing to the package file to unload."""

def reloadPackage(package_filepath: str) -> None:
    """reloadPackage(file_path)

    Update a package previously loaded. The package is first unloaded to
    uninstall the current resources and loaded back.


    file_path
        A full file path pointing to the package file to reload."""

def packageInfo(*args: Any) -> str:
    """packageInfo(file_paths) -> string

      Return a JSON dictionary string describing one or multiple package
      plugins previously loaded in Houdini.


      file_paths
          Array of package file paths. If the array is empty (default),
          all packages currently loaded are added to the dictionary.

      This shows the content of the viewer handle demo package.

    > >>> import json
    > >>> print( json.loads(hou.ui.packageInfo()) )
    > {
    >     'viewer_handle_demo': {
    >         'File path': '$HFS/houdini/viewer_handles/viewer_handle_demo.json',
    >         'Load only once': False,
    >         'Name': 'viewer_handle_demo',
    >         'Resources': {
    >             'Shelf': [
    >                 '$HFS/packages/viewer_handle_demo/toolbar/viewer_handle_demo.shelf'],
    >             'Viewer Handle': [
    >                 '$HFS/packages/viewer_handle_demo/viewer_handles/move_tool_handle.py',
    >                 '$HFS/packages/viewer_handle_demo/viewer_handles/viewer_handle_intro1.py',
    >                 '$HFS/packages/viewer_handle_demo/viewer_handles/viewer_handle_intro2.py',
    >                 '$HFS/packages/viewer_handle_demo/viewer_handles/viewer_handle_intro3.py']
    >         },
    >         'Variables': {
    >             'HOUDINI_PATH': [
    >                 '$HFS/packages/viewer_handle_demo']
    >          }
    >     }
    > }"""

def sharedAssetGalleryDataSource(gallery_name: str) -> hou.AssetGalleryDataSource:
    """sharedAssetGalleryDataSource(self, gallery_name) ->
    hou.AssetGalleryDataSource

        Return the hou.AssetGalleryDataSource object that is currently being
        used to populate the asset gallery browsers spcified by
        gallery_name. The built in shared galleries are 'layout' for Layout
        LOP and 'material' for Material LOP ."""

def setSharedAssetGalleryDataSource(data_source: hou.AssetGalleryDataSource, gallery_name: str) -> None:
    """setSharedAssetGalleryDataSource(self, datasource)

    Set the hou.AssetGalleryDataSource object that should be used to
    populate the asset gallery browsers spcified by gallery_name. The
    built in shared galleries are 'layout' for Layout LOP and 'material'
    for Material LOP ."""

def reloadSharedAssetGalleryDataSource(gallery_name: str) -> None:
    """reloadSharedAssetGalleryDataSource(self)

    Forces all asset gallery browsers spcified by gallery_name to reload
    from the underlying shared hou.AssetGalleryDataSource. Call this
    method after manipulating the data source returned by
    hou.ui.sharedAssetGalleryDataSource to refresh the asset browsers."""

def _selectNodeData(*args: Any, **kwargs: Any) -> list[str]: ...
def _selectNode(
    relative_to_node: Optional[hou.Node] = None,
    initial_node: Optional[hou.Node] = None,
    node_type_filter: Optional[hou.EnumValue] = None,
    title: Optional[str] = None,
    width: int = 0,
    height: int = 0,
    multiple_select: bool = False,
    custom_node_filter_callback: Optional[Any] = None,
) -> list[str]: ...
def selectMultipleNodes(
    relative_to_node: Optional[hou.Node] = None,
    initial_node: Optional[hou.Node] = None,
    node_type_filter: Optional[hou.EnumValue] = None,
    title: Optional[str] = None,
    width: int = 0,
    height: int = 0,
    custom_node_filter_callback: Optional[Any] = None,
) -> list[str]:
    """selectMultipleNodes(relative_to_node=None, initial_node=None,
    node_type_filter=None, title=None, width=0, height=0,
    custom_node_filter_callback=None) -> tuple of str or None

        This method is deprecated in favor of hou.ui.selectNode. Same
        behavior as selectNode however if the user holds 'Ctrl' they can
        select multiple nodes which are returned as a list of paths."""

def openBookmarkEditor(bookmark: Optional[hou.Bookmark] = None) -> None:
    """openBookmarkEditor(bookmark)

    Open the Houdini Bookmark Edit Dialog and return immediately.

    The bookmark parameter should be a hou.Bookmark object, returned by
    hou.anim.bookmarks() or hou.anim.bookmark()"""

def openColorEditor(
    color_changed_callback: Any,
    include_alpha: bool = False,
    initial_color: Optional[hou.Color] = None,
    initial_alpha: float = 1.0,
) -> None:
    """openColorEditor( color_change_callback, include_alpha=False,
    initial_color=None, initial_alpha=1.0)

        Open the Houdini color editor and return immediately.

        When a change is made in the editor then the color_change_callback
        function is invoked and passed the editor's current color and alpha
        value.

        If include_alpha is True then the color editor shows controls for
        editing the color's alpha value.

        The initial_color parameter specifies a hou.Color that will appear
        in the editor when it first opens. If not set, the initial color
        will be white.

        The initial_alpha parameter specifies an alpha value to use when the
        editor first opens. If not set, the initial alpha will be 1.0. Note
        that the initial_alpha parameter only applies if include_alpha is
        set to True.

        The color_change_callback argument must be a function that accepts
        two parameters -- a hou.Color object and an alpha value.

        Here is an example:

      > def handleColorChange(color, alpha):
      >     print \"Current color in editor:\", color, \", alpha=\", alpha
      >
      > hou.ui.openColorEditor(handleColorChange)"""

def openValueLadder(*args: Any, **kwargs: Any) -> None:
    """openValueLadder(initial_value, value_changed_callback,
    type=hou.valueLadderType.Generic,
    data_type=hou.valueLadderDataType.Float)

        Displays a value ladder control, the UI that typically appears when
        you press [MMB] on a field in Houdini. This lets you display ladder
        controls on your own custom UI, such as Qt edit fields.

        The typical workflow is:

         1. You should listen for [MMB] press and release events on your
            field.

         2. When the user presses [MMB] on the field, call this function to
            show the ladder. The function returns immediately but the ladder
            stays visible.

         3. As the user moves the mouse with [MMB] pressed down, you must
            call hou.ui.updateValueLadder with the mouse pointer
            coordinates.

         4. The ladder calls the value_changed_callback function you
            supplied as the user changes the value.

         5. When the user releases [MMB], call hou.ui.closeValueLadder.

        Only one value ladder window can be open at a time. This function
        raises hou.OperationFailed if another ladder window is currently
        open.


        initial_value
            The initial numeric value the ladder is set to when it opens.

        value_changed_callback
            A function that takes a single argument. As the user edits the
            number with the ladder, the ladder calls this function with each
            new value.

        type
            One of the values in hou.valueLadderType. The available types
            are Generic and Angle. This affects the increments on the
            ladder.

        data_type
            One of the values in hou.valueLadderDataType. Integer and Float
            ladders have different increments.

        This examples demonstrates how to add value ladder window support to
        an input field class that derives from Qt's QLineEdit class:

      >
      > from PySide2 import QtWidgets
      > from PySide2.QtCore import Qt
      > import hou
      >
      >
      > class LineEditWithValueLadder(QtWidgets.QLineEdit):
      >     def __init__(self, parent=None):
      >         super(LineEditWithValueLadder, self).__init__(parent)
      >         self._pressed = False
      >
      >     def mousePressEvent(self, event):
      >         # Show the value ladder window if MMB was pressed.
      >         if event.button() == Qt.MiddleButton:
      >             try:
      >                 hou.ui.openValueLadder(
      >                     float(self.text()),
      >                     self._ladderchange,
      >                     data_type=hou.valueLadderDataType.Float
      >                 )
      >             except hou.OperationFailed:
      >                 # A ladder is already open somewhere
      >                 return
      >             else:
      >                 self._pressed = True
      >
      >     def mouseMoveEvent(self, event):
      >         if self._pressed:
      >             hou.ui.updateValueLadder(
      >                 event.globalX(),
      >                 event.globalY(),
      >                 bool(event.modifiers() & Qt.AltModifier),
      >                 bool(event.modifiers() & Qt.ShiftModifier)
      >             )
      >
      >     def mouseReleaseEvent(self, event):
      >         if event.button() == Qt.MiddleButton and self._pressed:
      >             hou.ui.closeValueLadder()
      >             self._pressed = False
      >
      >     def _ladderchange(self, new_value):
      >         self.setText(str(new_value))"""

def addEventLoopCallback(callback: Any) -> None:
    """addEventLoopCallback(callback)

      Register a Python callback to be called whenever Houdini's event
      loop is idle. This callback is called approximately every 50ms,
      unless Houdini is busy processing events.


      callback
          Any callable Python object that expects no parameters. It could
          be a Python function, a bound method, or any object implementing
          __call__.

    > def checkForAndProcessEvents():
    >     # Here is where you would check for and process any events.
    >     pass
    >
    > hou.ui.addEventLoopCallback(checkForAndProcessEvents)

      You might use this function to integrate another user interface
      toolkit into Houdini's event loop. See the PyQt and wxPython
      cookbook examples for example usages."""

def removeEventLoopCallback(callback: Any) -> None:
    """removeEventLoopCallback(callback)

    Remove a Python callback that was previously registered with
    hou.ui.addEventLoopCallback. See hou.ui.addEventLoopCallback for
    more information.

    Raises hou.OperationFailed if the callback was not previously
    registered."""

def postEventCallback(callback: Any) -> None:
    """postEventCallback(callback)

    Register a Python callback to be called next in Houdini's event
    loop. This will be called only once.


    callback
        Any callable Python object that expects no parameters. It could
        be a Python function, a bound method, or any object implementing
        __call__."""

def removePostedEventCallback(callback: Any) -> None:
    """removePostedEventCallback(callback)

    Remove a posted event callback from the queue if it is still there.

    If the callback is not present, nothing is done."""

def eventLoopCallbacks() -> list[Any]:
    """eventLoopCallbacks() -> tuple of callback

    Return a tuple of all the Python callbacks that have been registered
    with hou.ui.addEventLoopCallback."""

def waitUntil(callback: Any) -> None:
    """waitUntil(condition_callback)

      Keep calling the supplied callback until it returns True. In the
      meantime, Houdini will continue to be responsive, allowing you to
      continue to interact with it.

      For example, start a blank Houdini session and put the following in
      a shelf tool. It will wait until you create an object node before
      finishing running the tool.

    > print \"waiting until you create an object...\"
    > hou.ui.waitUntil(lambda: len(hou.node(\"/obj\").children()) > 0)
    > print \"you created\", hou.node(\"/obj\").children()

      If you find that your callback function is too slow to be run
      frequently, you can try only making it do work every so often:

    > import time
    >
    > def throttle(callback, delay=2.0):
    >     # Returns a wrapper function around `callback`, which only calls
    >     # `callback` every `delay` seconds (default 2.0), no matter
    >     # how often the wrapper function is called.
    >
    >     # This can be useful if the condition function is expensive to run,
    >     # so you want to limit how often it is called.
    >
    >     # Store in a list, since Python 2.x doesn't have full nonlocal keyword
    >     last_check = [0.0]
    >
    >     def wrapper():
    >         now = time.time()
    >         if now < last_check[0] + delay:
    >             # Since we return False when we're inside the delay, Houdini
    >             # will continue to call the condition function
    >             return False
    >         else:
    >             last_check[0] = now
    >             return callback()
    >
    >     return wrapper
    >
    >
    > # Then you could use this with hou.ui.waitUntil like this:
    >
    > def my_callback():
    >     return len(hou.node(\"/obj\").children()) > 0
    >
    > hou.ui.waitUntil(throttle(my_callback, delay=0.5))"""

def addTriggerUpdateCallback(callback: Any) -> None:
    """removeTriggerUpdateCallback(callback)

    Remove a callback previously added with the
    hou.ui.addTriggerUpdateCallback method."""

def removeTriggerUpdateCallback(callback: Any) -> None: ...
def addSelectionCallback(callback: Any) -> None:
    """addSelectionCallback(callback)

      Register a Python callback to be called whenever Houdini's global
      network item selection changes.


      callback
          Any callable Python object that expects a single parameter. This
          parameter will be a list of all selection hou.NetworkMovableItem
          objects that are now selected. It could be a Python function, a
          bound method, or any object implementing __call__.

    > def selectionCallback(selection):
    >     # Here is where you would respond to the selection change.
    >     pass
    > hou.ui.addSelectionCallback(selectionCallback)"""

def removeSelectionCallback(callback: Any) -> None:
    """removeSelectionCallback(callback)

    Remove a Python callback that was previously registered with
    hou.ui.addSelectionCallback. See hou.ui.addSelectionCallback for
    more information."""

def selectionCallbacks() -> list[Any]:
    """selectionCallbacks() -> tuple of callback

    Return a tuple of all the Python callbacks that have been registered
    with hou.ui.addSelectionCallback."""

def addResourceEventCallback(callback: Any) -> None:
    """addResourceEventCallback(self, callback)

    Register a Python callback to be called whenever a
    hou.resourceEventMessage event occurs.


    'callback'
        Any callable Python object that expects a keyworded argument.

        The keyworded argument contains the following:

      * event_type: hou.resourceEventMessage event.

      * resource_type: A resource type such as ViewerState and
        ViewerHandle.

      * type_name: The type name of the resource that triggered the
        event. If the resource is a ViewerState, the type name can be
        used for indexing the dictionary returned from
        hou.ui.viewerStateInfo."""

def removeResourceEventCallback(callback: Any) -> None:
    """removeResourceEventCallback(self,callback)

    Remove a specific Python callback previously registered with
    hou.ui.addResourceEventCallback."""

def openFileEditor(*args: Any, **kwargs: Any) -> None:
    """openFileEditor(title, file_path, action_callback=None, params=None)

      Open a window for editing and saving a text file.

      The editor buttons:

    * Apply: Save the file only if the source has changed.

    * Accept: Save the file if the source has changed and close the
      window.

    * Cancel: Close the window without saving the file and prompting the
      user.


      NOTE
          When applying unsaved changes, the editor prompts the user if
          the file being edited is not in sync with the file on disk. At
          this point the user is asked to load the new file (overriding
          its current changes) or save its current changes (overriding the
          file on disk) or cancel the operation.

      An optional callback and a dictionary of user-defined parameters can
      be specified to customize the Apply and Accept operations.


      title
          Name of the window title.

      file_path
          A string set with a full path to the file to edit. Exception is
          raised if the string is empty.

          The file extension determines the language settings used by the
          editor. The following file types are supported:

          .py

          Python

          .cmd

          hscript

          .txt/no extension

          Text document

      action_callback
          An optional callback triggered by the editor when either the
          Apply or Accept button is clicked. The callback can be used to
          perform a custom operation. The editor saves the file being
          edited, if required, before calling the callback.

          The callback name is user-defined and takes a dictionary
          argument as input:

        > def myApplyAction( **kwargs )

      params
          A dictionary mapping user-defined entries to values of type int,
          double, bool and string. The dictionary is passed as argument to
          the callback specified with action_callback.

      Example:

    >
    > def myAction(**kwargs):
    >     hou.ui.printResourceMessage(kwargs['msg'] + ' saved.', kwargs['msg_type'])
    >
    > file_path = '/var/tmp/main.py'
    > hou.ui.openFileEditor( 'My Editor Title', file_path, action_callback=myAction,
    >     params={ 'msg' : file_path, 'msg_type' : hou.severityType.Message })"""

def openViewerStateCodeGenDialog(*args: Any, **kwargs: Any) -> None:
    """openViewerStateCodeGenDialog(category, action_callback,
    operator_name=None)

        Open a modal dialog window for generating a template implementation
        and registration code for a python viewer state. The input name of
        the viewer state is mandatory for generating the code. Other fields
        such as the state label and icon name are optional.

        The dialog Sample options can be selected to generate the viewer
        state code with predefined handlers and bindings. The Handler
        options can also be selected to generate the viewer state code with
        empty handlers.

        The dialog buttons:

      * Accept: Generate the code template with the input fields and
        selected options.

      * Cancel: Close the dialog and abort the code template generation.

        This dialog is used by the Viewer State Browser panel and the
        Digital Asset Viewer State editor.


        category
            A hou.NodeTypeCategory object to specify the type of viewer
            state to register.

        action_callback
            A mandatory callback required for handling the result when the
            Accept button is clicked.

            The callback name is user-defined and takes a dictionary
            argument as input:

          > def myAcceptAction( **kwargs )

            The kwargs dictionary contains the results of the code
            generation:

          * valid: Returns True if the operation succeeded, False otherwise.

          * state_type: The name of the new state.

          * state_type_expr: Expression representing the name of the new
            state: either a python

                function call to get the HDA node's default state or a
                string literal.

          * state_label: The state label.

          * state_description: The state description which is only displayed
            in the code header.

          * state_category: The name of the state category type.

          * state_code: The generated python code.

          * state_icon_name: The name of the icon selected. The name can be
            either a single icon name, a

                file path or an opdef path to refer to an icon embedded in a
                Digital Asset.

          * state_icon_filename: The icon file path if any.

          * state_icon_section_name: The section name of the icon used by
            the Digital Asset viewer state editor.

        operator_name
            The name of the operator if the viewer state to generate is
            embedded in a Digital Asset. This argument is optional and
            mostly used by the Digital Asset viewer state editor."""

def openViewerHandleCodeGenDialog(category: hou.NodeTypeCategory, action_callback: Any) -> None:
    """openViewerHandleCodeGenDialog(categories, action_callback)

      Open a modal dialog window for generating a template implementation
      and registration code for a python viewer handle. The input name of
      the viewer handle is mandatory for generating the code. Other fields
      such as the handle label and icon name are optional.

      The dialog Sample options can be selected to generate the viewer
      handle code with predefined handlers and bindings. The Handler
      options can also be selected to generate the viewer handle code with
      empty handlers.

      The dialog buttons:

    * Accept: Generate the code template with the input fields and
      selected options.

    * Cancel: Close the dialog and abort the code template generation.

      This dialog is available from Viewer Handle Browser panel under the
      File|New... menu.


      category
          A hou.NodeTypeCategory object to specify the type of viewer
          handle to register.

      action_callback
          A mandatory callback required for handling the result when the
          Accept button is clicked.

          The callback name is user-defined and takes a dictionary
          argument as input:

        > def myAcceptAction( **kwargs )

          The kwargs dictionary contains the results of the code
          generation:

        * handle_valid: Returns True if the operation succeeded, False
          otherwise.

        * handle_type: The type name of the new handle.

        * handle_type_expr: Expression representing the name of the new
          handle.

        * handle_label: The handle label.

        * handle_description: The handle description which is only
          displayed in the code header.

        * handle_category: The name of the handle category type.

        * handle_code: The generated python code.

        * handle_icon_name: The name of the icon selected. The name can be
          either a single icon name or a file path.

        * handle_icon_filename: The icon file path if any."""
