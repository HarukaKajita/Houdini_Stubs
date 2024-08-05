# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.hotkeys

def __init__(*args: Any, **kwargs: Any): ...
def assignments(*args: Any) -> list[str]: ...
def hotkeyDescription(hotkey_symbol: str) -> str:
    """hotkeyDescription(hotkey_symbol) -> str

      Returns the long description/help for a the given symbol string.

    > desc = hou.hotkeys.hotkeyDescription(\"h.open\")
    > # \"Open a file\" """

def hotkeyLabel(hotkey_symbol: str) -> str:
    """hotkeyLabel(hotkey_symbol) -> str

      Return the human-readable label for a symbol string.


      hotkey_symbol
          The target hotkey symbol name.

    > label = hou.hotkeys.hotkeyLabel(\"h.open\")
    > # \"Open\" """

def isKeyMatch(key: str, hotkey_symbol: str) -> bool:
    """isKeyMatch(key, hotkey_symbol) -> bool

    Return True is key is a match for the given hotkey symbol. If key is
    a keyvoard shortcut string then it must match one of the keyboard
    shortcuts assigned to the hotkey. If key is a hotkey symbol then it
    must be a string match to hotkey_symbol.


    key
        Either a keyboard sequence string or a hotkey symbol. This is
        typically something given to us by an event processing system
        which would either know the hotkey invoked (like when a button
        is clicked) or just the key sequence pressed.

    hotkey_symbol
        The hotkey to check for a match against."""

def isKeycodeMatch(key_code: int, hotkey_symbol: str) -> bool:
    """isKeycodeMatch(key_code, hotkey_symbol) -> bool

    Return True is keycode is a match for the given hotkey symbol.


    key_code
        A keycode from a keyboard event.

    hotkey_symbol
        The hotkey to check for a match against."""

def findConflicts(*args: Any) -> list[str]:
    """findConflicts(context, symbol, key) -> tuple of str

      Returns a sequence of symbol strings in ancestor and/or descendant
      contexts relative to the given context (including the symbol you
      passed in itself) that use the given key. This lets you see existing
      or potential conflicts. The returned strings are encoded as
      <context>?<symbol>.

      This function also has a deprecated signature without the context
      argument. The deprecated signature should not be used unless use of
      the old hotkey system has been forced with an environment variable.
      Under the old hotkey system, the returned strings are simply the
      symbols.

      An example of a conflict would be if a high level action (for
      example, h.copy, in the h context) has hotkey [Ctrl + C], and a
      lower-level action (for example,
      h.panes.gview.state.sop.demo.duplicate in the
      h.panes.gview.state.sop.demo context) also uses [Ctrl + C], then
      where you're in that state, the higher-level Copy key won't be
      available because it's overridden by the lower-level key.

    > # Find potential conflicts with K on the top-level Add Keyframe command
    > symbols = hou.hotkeys.findConflicts(\"h\", \"h.add_key\", \"k\")
    > # Returns ('h.pane.gview.state.sop.topobuild?h.pane.gview.state.sop.topobuild.bridge', 'h?h.add_key'),
    > # meaning K is assigned to both h.add_key and
    > # h.pane.gview.state.sop.topobuild.bridge
    > # in the same hierarchy
    >
    > # Find potential conflicts with Ctrl + C on the top-level Copy command
    > symbols = hou.hotkeys.findConflicts(\"h.copy\", \"ctrl+c\")  # (Use cmd+c on Mac)
    > # Returns (\"h.copy\",) meaning there are no conflicts (the symbol
    > # you checked is the only symbol in that hierarchy using that key)"""

def resolveAssignments(contexts: tuple[str], hotkey_symbols: tuple[str]) -> list[list[str]]:
    """resolveAssignments(self, contexts, hotkey_symbols) -> tuple of tuple of
    str

        Return a tuple of strings that represent the hotkeys that will
        invoke each action from a tuple of hotkey symbols when resolved
        against a specific list of hotkey contexts. The key strings are of
        the form returned by the hou.ui.hotkeys method, which is a
        combination of the symbol on the key, and any modifier keys
        involved, such as \"Ctrl+Shift+G\"."""

def changeIndex() -> int:
    """changeIndex() -> int

    Return the monotonically increasing change index from the hotkey
    manager. This number increases by one whenever any change is made to
    the hotkey manager. If a module is caching any information from the
    hotkey manager it should check this change index to see if any
    changes have been made and thus the cache should be refreshed."""

def commandsInContext(context: str) -> list[dict[str, str]]:
    """commandsInContext(context) -> tuple of dict

    This method is deprecated under the new hotkey system. Use either
    hou.hotkeys.commandsInCategory or
    hou.hotkeys.commandBindingsInContext instead.

    Return all hotkey commands at the given parent hotkey context.

    Each command is a dict with the following keys: symbol, label, and
    help.


    context
        The hotkey symbol of the context."""

def contextsInContext(context: str) -> list[dict[str, str]]:
    """contextsInContext(context) -> tuple of dict

    Return all hotkey contexts at the given parent hotkey context.

    Each command is a dict with the following keys: symbol, label, and
    help.


    context
        The hotkey symbol of the context."""

def commandCategoriesInCategory(category: str) -> list[dict[str, str]]:
    """commandCategoriesInCategory(category) -> tuple of dict

    Return all hotkey command categories under the given parent hotkey
    category.

    Each category is a dict with the following keys: symbol, label, and
    help.


    category
        The symbol of the command category."""

def commandsInCategory(category: str) -> list[dict[str, str]]:
    """commandsInCategory(category) -> tuple of dict

    Return all hotkey commands under the given parent category.

    Each command is a dict with the following keys: symbol, label, and
    help.


    category
        The symbol of the command category."""

def commandBindingsInContext(context: str) -> list[dict[str, str]]:
    """commandBindingsInContext(context) -> tuple of dict

    Return all commands bound in the given hotkey context.

    Each command is a dict with the following keys: symbol, label, and
    help.


    context
        The hotkey symbol of the context."""

def addCommand(*args: Any) -> bool:
    """addCommand(hotkey_symbol, label, description, assignments) -> bool

      This method is deprecated. Use hou.hotkeys.installDefinitions
      instead.

      Registers a new configurable hotkey command with Houdini. The
      context it belongs to should already exist, see
      hou.hotkeys.addContext.

      A hotkey symbol represents an action, for example deleting the
      selected geometry when a certain tool is active. The user can change
      the actual key assigned to the action using the hotkey editor. After
      registering the symbol you can programmatically assign a default key
      using hou.hotkeys.addAssignment.

      To add a delete action to the demo python state, you would do
      something like this:

    > # Add a hotkey context for the demo python state
    > demo_context = \"h.pane.gview.state.sop.demo\"
    > hou.hotkeys.addContext(demo_context, \"demo Operation\", \"These keys apply to the demo operations\")
    >
    > # Add hotkeys to the \"demo\" state
    > delete_symbol = demo_context + \".delete\"
    > hou.hotkeys.addCommand(
    >     delete_symbol,
    >     \"Delete Selected\",
    >     \"Delete the selected geometry\"
    > )
    > commit_symbol = demo_context + \".commit\"
    > hou.hotkeys.addCommand(
    >     commit_symbol,
    >     \"Commit Changes\",
    >     \"Save changes to parameters and start a new cache\"
    > )
    > cancel_symbol = demo_context + \".cancel\"
    > hou.hotkeys.addCommand(
    >     cancel_symbol,
    >     \"Cancel Changes\",
    >     \"Discard any  changes and return to an empty cache\"
    > )

      hotkey_symbol
          A string containing a full dotted hotkey symbol.

      label
          A human readable title for the action. For example, Delete
          Selected.

      description
          A human readable description of the action. This should
          generally be one to three sentences of help text for the action.

      assignments
          An optional list of shortcut strings to be used as the default
          assignments for this command."""

def addContext(hotkey_symbol: str, label: str, description: str) -> bool:
    """addContext(hotkey_symbol, label, long_description ) -> bool

    This method is deprecated. Use hou.hotkeys.installDefinitions
    instead.

    Registers a new hotkey context with Houdini. A context should be
    created before creating contexts or commands within that context.

    Currently this is only useful for adding hotkeys to Python states.


    hotkey_symbol
        A string containing a full dotted hotkey symbol representing the
        context. Currently the only useful value for hotkey_symbol is:

      > h.pane.gview.state.sop

    label
        A human readable title for the context. For example, Demo State
        Operation.

    description
        A human readable description of the context. This should
        generally be one to three sentences of help text for the action."""

def installDefinitions(definitions: hou.PluginHotkeyDefinitions) -> None:
    """uninstallDefinitions(definitions)

    Uninstalls any command categories, commands, binding contexts and
    default bindings used by a plugin.


    definitions
        A populated hou.PluginHotkeyDefinitions object that was
        previously used to install the definitions with
        hou.hotkeys.installDefinitions()."""

def uninstallDefinitions(definitions: hou.PluginHotkeyDefinitions) -> None: ...
def addCommandBinding(context: str, command: str) -> bool:
    """addCommandBinding(context, command) -> bool

    Adds a binding for command in context so that it appears in the
    hotkey manager for key assignment if one does not already exist.
    Keys can then be assigned to this binding via
    hou.hotkeys.addAssignment. It is not necessary to do this prior to
    adding assignments, but if you want to create an empty binding
    without any assigned keys, use this.


    context
        The hotkey context in which to create the binding.

    command
        The hotkey command to bind in the given context."""

def removeCommandBinding(context: str, command: str) -> bool:
    """removeCommandBinding(context, command) -> bool

    Removes the binding for command from context. Note that in most
    cases you probably want remove all key assignments from the binding,
    leaving the binding itself in place. See
    hou.hotkeys.clearAssignments.


    context
        The hotkey context from which to remove the binding.

    command
        The hotkey command to unbind from the given context."""

def removeHotkeySymbol(hotkey_symbol: str) -> None:
    """removeHotkeySymbol(hotkey_symbol)

      This method is deprecated. Use hou.hotkeys.uninstallDefinitions
      instead.

      Removes an existing hotkey previously created with .


      hotkey_symbol
          A string containing a full dotted hotkey symbol.

          Currently this is only useful for removing hotkeys of Python SOP
          states, so symbol will be in the form:

          h.pane.gview.state.sop.<state_name>.<action_name>

    > hou.hotkeys.removeHotkeySymbol(\"h.pane.gview.state.sop.demo.delete\")"""

def hotkeySymbol(english_context: str, english_command: Optional[str] = None) -> str:
    """hotkeySymbol(context_label_path, command_label=None) -> str or None

      Does a reverse-lookup to retrieve the hotkey symbol given the human-
      readable context label(s). If you supply only a context label, the
      function returns the context's prefix symbol. If you also supply a
      command label, the function returns the command's hotkey symbol.


      context_label_path
          A string containing a path through the hierarchy of human-
          readable context labels, starting with and separated by slashes.
          For example, \"/Houdini/Panes/Geometry Viewers\".

      command_label
          An optional human-readable command label, for example \"Box
          Selection\".

    > hou.hotkeys.hotkeySymbol(\"/Houdini/Panes/Geometry Viewers\", \"Box Selection\")
    > # \"h.pane.gview.selectstylebox\" """

def clearAssignments(*args: Any) -> bool:
    """clearAssignments(context, hotkey_symbol) -> bool

      Removes any keys assigned to a hotkey symbol in the given context.

    > hou.hotkeys.clearAssignments(\"h.pane.gview.state.sop.demo\", \"h.pane.gview.state.sop.demo.delete\")

      context
          The hotkey context in which to clear the asssignments.

      hotkey_symbol
          The symbol string for the action you want to remove hotkeys
          from.

      This function also has a deprecated signature without the context
      argument. The deprecated signature should not be used unless use of
      the old hotkey system has been forced with an environment variable.

      RELATED

          hou.hotkeys.addCommand"""

def addAssignment(*args: Any) -> bool:
    """addAssignment(context, hotkey_symbol, key) -> bool

      Assigns a key (or key combination) to a hotkey symbol in the given
      context.

    > hou.hotkeys.addAssignment(\"h.pane.gview.state.sop.demo\", \"h.pane.gview.state.sop.demo.delete\", \"alt+k\")
    > hou.hotkeys.addAssignment(\"h.pane.gview.state.sop.demo\", \"h.pane.gview.state.sop.demo.delete\", \"shift+del\")

      Returns True if the assignment succeeds, or False if the symbol is
      unknown or the key string is not valid.


      context
          The hotkey context in which to add the asssignment.

      hotkey_symbol
          The symbol string for the action you want to assign a hotkey to.

      key
          A string specifying the key (or key combination) to assign to
          the action. For example, \"shift+del\".

      This function also has a deprecated signature without the context
      argument. The deprecated signature should not be used unless use of
      the old hotkey system has been forced with an environment variable."""

def removeAssignment(*args: Any) -> bool:
    """removeAssignment(context, hotkey_symbol, key) -> bool

      Removes a key (or key combination) from a hotkey symbol in a given
      context.

    > hou.hotkeys.removeAssignment(\"h.pane.gview.state.sop.demo\", \"h.pane.gview.state.sop.demo.delete\", \"alt+k\")

      context
          The target context name.

      hotkey_symbol
          The target hotkey symbol name.

      key
          The key string identifier to remove. For example, \"shift+del\".

      This function also has a deprecated signature without the context
      argument. The deprecated signature should not be used unless use of
      the old hotkey system has been forced with an environment variable."""

def _getHotkeysStatus(hotkey_symbol: str, layout_keys: tuple[str], modifier_mask: int = 0) -> dict[str, list[str]]: ...
def availableKeycodes(*args: Any) -> list[int]:
    """availableKeycodes(context, hotkey_symbol, layout_keys, modifiers=0) ->
    tuple of int

        Return all available shortcut keycodes with their conflict status
        bits set w.r.t. the specified hotkey symbol. A keycode is considered
        available if it isn't assigned to another hotkey within the given
        context.


        context
            The context to check for availability.

        hotkey_symbol
            The target hotkey symbol name.

        layout_keys
            A list of unmodified keycodes to check. If empty, the unmodified
            keycodes from a standard US keyboard will be checked.

        modifiers
            UI_KeyBindings modifier key bits to be applied. Only keycodes
            with these modifier bits are returned.

        This function also has a deprecated signature without the context
        argument. The deprecated signature should not be used unless use of
        the old hotkey system has been forced with an environment variable."""

def keycodeToString(keycode: int, modifiers: int = 0) -> str:
    """keycodeToString(keycode, modifiers=0) -> str

    Convert a hotkeymanager keycode to a key string.


    modifiers
        UI_KeyBindings modifier key bits to be applied."""

def stringToKeycode(key: str, modifiers: int = 0) -> int:
    """stringToKeycode(key, modifiers=0) -> int

    Convert a keystring to a hotkeymanager keycode.


    modifiers
        UI_KeyBindings modifier key bits to be applied."""

def _createBackupTables() -> None: ...
def _restoreBackupTables() -> None: ...
def revertToDefaults(hotkey_symbol: str, one_level_only: bool) -> None:
    """revertToDefaults(hotkey_symbol, one_level_only)

    Revert the specified hotkey to its defaults from the keymap.


    hotkey_symbol
        The hotkey symbol (command or context) to reset.

    one_level_only
        When False, this item and its children are all set to their
        default. When True, only this context or command is reset. This
        only has an effect for contexts since commands have no children."""

def saveOverrides() -> bool:
    """saveOverrides() -> bool

    Save changes to the hotkeys as overrides to the current keymap.
    Changes are things that are different from their default value e.g.
    modifying a shortcut key assignment. Note that adding a new hotkey
    command with addHotkey will treat it as a new default so that it
    won't be saved unless a change is made to it after it is added."""

def saveAsKeymap(name: str, path: Optional[str] = None) -> bool:
    """saveAsKeymap(name, path=None) -> bool

    Save the currently defined hotkeys as a keymap. This combines the
    loaded keymap with all of the defined overrides into a single new
    keymap. Returns True upon successful save.


    name
        The name of the new keymap.

    path
        Optional save path for the new keymap. If None then it will be
        saved into the user prefs dir with a filename derived from the
        keymap name."""

def loadKeymap(name: str, path: Optional[str] = None) -> bool:
    """loadKeymap(name, path=None) -> bool

    Save the currently defined hotkeys as a keymap. This combines the
    loaded keymap with all of the defined overrides into a single new
    keymap. Returns True upon successful load.


    name
        The name of the keymap to load.

    path
        Optional path for the keymap to load. If None then it will be
        searched in the search path."""

def importKeymap(name: str, path: str) -> bool:
    """importKeymap(name, path=None) -> bool

    Copy the specified keymap into the user preferences directory and
    save it with an appropriate name. Returns True upon successful
    import.


    name
        The new name of the keymap.

    path
        The path of the keymap to import."""

def keymaps() -> list[tuple[str, str]]:
    """keymaps() -> tuple or str

    Return a list of tuples of all the keymaps found. The tuple has the
    keymap's name and path."""

def currentKeymap() -> str:
    """currentKeymap() -> str

    Return the name of the currently loaded keymap."""
