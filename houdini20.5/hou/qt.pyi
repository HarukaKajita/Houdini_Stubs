# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.qt

def __init__(*args: Any, **kwargs: Any): ...
def _mainWindow() -> None: ...
def _floatingPanelWindow(panel: hou.FloatingPanel) -> None:
    """hou.qt.floatingPanelWindow

    Return a QWidget instance representing the window for the specified
    floating panel.

    USAGE
      floatingPanelWindow(self, panel) -> QWidget

    Return a QWidget instance representing the window for the provided
    hou.FloatingPanel. If the provided panel is None, this method returns
    the mainWindow. This method is helpful for parenting a PySide or PyQt
    dialog to a particular floating panel. Parenting to a panel keeps the
    dialog alive for the lifetime of the panel so that the dialog is not
    destroyed prematurely by Python. Parenting also causes the dialog to
    inherit the Houdini style sheet set on the main window, and depending on
    the dialog configuration, can keep the dialog on top of the floating
    panel.

    Here is an example of parenting a dialog to the panel that contains a
    particular pane tab:

    > from hutil.Qt import QtCore
    >
    > panetab = hou.ui.findPaneTab('panetab1')
    > panel = panetab.pane().floatingPanel()
    > dialog = MyDialog()
    > dialog.setParent(hou.qt.floatingPanelWindow(panel), QtCore.Qt.Window)
    > dialog.show()"""

def _createWindow() -> None: ...
def _createDialog() -> None: ...
def _createMenu() -> None: ...
def _createIcon(icon_name: str, width: int, height: int) -> None: ...
def canCreateIcon(icon_name: str) -> bool:
    """hou.qt.canCreateIcon

    Return true if a valid (non-empty) icon can be created from the supplied
    icon name.

    USAGE
      canCreateIcon(name) -> bool

    This functon can be used before using hou.qt.Icon to create a new icon.
    If this function returns False, the generated icon, while valid, will be
    blank because no source data will be found using the given name."""

def _createParmDialog(hom_node: hou.Node, showTitleBar: bool, compact: bool, labelsize: float) -> None: ...
def _setParmDialogNode(widget: None, hom_node: hou.Node) -> None: ...
def _parmDialogNode(widget: None) -> hou.Node: ...
def _getParmDialogValueNames(widget: None) -> list[str]: ...
def _getParmDialogValue(widget: None, name: str) -> str: ...
def _setParmDialogValue(widget: None, name: str, value: str) -> bool: ...
def _pressParmDialogButton(widget: None, name: str) -> bool: ...
def _getParmDialogVisibleParms(widget: None) -> list[hou.ParmTuple]: ...
def _getColor(color_name: str) -> None: ...
def _getCursor(cursor_name: str) -> None: ...
def _getBrush(color_name: str) -> None: ...
def styleSheet(file_path: Optional[str] = None) -> str:
    """hou.qt.styleSheet

    Return the Houdini style sheet.

    USAGE
      styleSheet(file_path=None) -> str

    If file_path is not None, then return the style sheet stored in the
    given file rather than the Houdini style sheet. Style placeholders, such
    as color placeholders (i.e. @MenuBG@) and scaled size placeholders (i.e.
    @14px@), are evaluated and expanded in the returned style sheet.

    Return an empty string if the specified file path does not exist or if
    there is a syntax error in the style sheet.

    The returned style sheet can be applied to Qt widgets. Note that child
    widgets automatically inherit the parent widget's style sheet.

    > import Qt.QtWidgets as QtWidgets
    >
    > # Get the Houdini style sheet.
    > stylesheet = hou.qt.styleSheet()
    >
    > # Apply the Houdini style to a widget.
    > parent_widget = QtWidgets.QWidget()
    > parent_widget.setStyleSheet(stylesheet)
    >
    > child_button = QtWidgets.QPushButton()
    > child_button.setText(\"Hello World\")
    >
    > # Parenting the child button inherits the parent's Houdini style sheet.
    > child_button.setParent(parent_widget)"""

def _qtKeyToUIKey(qtKey: int, qtKeymodifiers: int) -> dict[str, int]: ...
def _qtKeyToString(qtKey: int, qtKeymodifiers: int, qtkeystring: str) -> str: ...
def _nativeModifierIndependentKeyCode(native_scan_code: int, native_virtual_key: int) -> hou.OptionalInt: ...
def _hasExtendedKeyEventInfo(native_key_code: int) -> bool: ...
def _eventKeyIfNoModifiers(native_key_code: int) -> int: ...
def _eventTextIfNoModifiers(native_key_code: int) -> str: ...
def _registerKeyResolveInfoCallback(widget: int, callback: Any) -> None: ...
def _unregisterKeyResolveInfoCallback(widget: int) -> None: ...
def _hotkeyAssignments(widget: int, hotkey_symbols: tuple[str]) -> list[list[str]]: ...
def _resolveKeyToCommand(key: str, override_contexts: tuple[str]) -> str: ...
def inchesToPixels(inches: float) -> float:
    """hou.qt.inchesToPixels

    Converts inches to pixels, accounting for both Qt and Houdini's dpi
    settings.

    USAGE
      inchesToPixels(inches) -> float"""

def pixelsToInches(pixels: float) -> float:
    """hou.qt.pixelsToInches

    Converts pixels to inches, accounting for both Qt and Houdini's dpi
    settings.

    USAGE
      pixelsToInches(pixels) -> float"""

def skipClosingMenusForCurrentButtonPress() -> None:
    """hou.qt.skipClosingMenusForCurrentButtonPress

    Disable automatic closing of menus for the current mouse button event.

    USAGE
      skipClosingMenusForCurrentButtonPress()

    Normally a mouse button event sent to any Qt widget in the Houdini
    process will cause all open Houdini menus to close. However if a mouse
    button event to a Qt widget is what causes a Houdini menu to open (such
    as through a call to hou.NetworkEditor.openNodeMenu), it is necessary to
    disable this automatic menu closing temporarily. Otherwise the menu that
    was just opened would be immediately closed. This method does exactly
    this, disabling the automatic menu closing until the next mouse button
    release event, at which time the automatic menu closing is re-enabled."""

def _launchRenderGalleryBackgroundRender(
    delegate: str,
    usd_filepath: str,
    rendersettings_prim: str,
    override_camera: str,
    override_res_x: int,
    override_res_y: int,
    lopnet_path: str,
    item_id: str,
) -> bool: ...
def _renderGalleryBackgroundRenderMouseClick(x: int, y: int, lopnet_path: str, item_id: str) -> None: ...
def _stopRenderGalleryBackgroundRender(lopnet_path: str, item_id: str) -> None: ...
def _channelPathMimeType() -> str: ...
def _chopTrackPathMimeType() -> str: ...
def _galleryEntryMimeType() -> str: ...
def _galleryEntryNameMimeType() -> str: ...
def _itemPathMimeType() -> str: ...
def _nodeFlagPathMimeType() -> str: ...
def _nodePathMimeType() -> str: ...
def _orboltNodeTypeNameMimeType() -> str: ...
def _paneTabNameMimeType() -> str: ...
def _parmPathMimeType() -> str: ...
def _persistentHandleNameMimeType() -> str: ...
def _primitivePathMimeType() -> str: ...
def _shelfNameMimeType() -> str: ...
def _shelfToolNameMimeType() -> str: ...
def _takeNameMimeType() -> str: ...
def _usdPrimitivePathMimeType() -> str: ...
def _usdPrimitivePythonMimeType() -> str: ...
def _usdPropertyPathMimeType() -> str: ...
def _usdPropertyPythonMimeType() -> str: ...
def _assetGalleryEntryMimeType() -> str: ...
def _galleryNameRole() -> int: ...
def _galleryThumbRole() -> int: ...
def _galleryCreationDateRole() -> int: ...
def _galleryStarRole() -> int: ...
def _galleryDiffMarkerRole() -> int: ...
def _galleryColorRole() -> int: ...
def _galleryTagsRole() -> int: ...
def _galleryThumbValidRole() -> int: ...
def _galleryMetadataRole() -> int: ...
def _gallerySnapshotFileRole() -> int: ...
def _gallerySnapshotRole() -> int: ...
def _galleryRenderingRole() -> int: ...
def _galleryCloneIdRole() -> int: ...
