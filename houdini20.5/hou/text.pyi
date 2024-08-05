# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.text

def __init__(*args: Any, **kwargs: Any): ...
def expandString(str: str, expand_tilde: bool = True) -> str:
    """expandString(str, expand_tilde=True) -> str

      Expands global variables in the expression. For example, when
      Houdini is at frame 10:

    > >>> hou.text.expandStringAtFrame('$F')
    > '10'

      Also expands HScript expressions in backticks, such as the channel
      reference in this example. This returns the value of the translate X
      parameter for geo1 at the current frame as a string:

    > hou.text.expandStringAtFrame('`ch(\"/obj/geo1/tx\")`')

      The expand_tilde parameter can be set to False to prevent the
      expansion of ~ to your home directory path.

      This function evaluates the string as if it were the contents of a
      non-animated text parameter. To evaluate a straight HScript
      expression (without needing backticks), use hou.hscriptExpression.

      Raises hou.OperationFailed exception if the first argument is None.

    > >>> hou.text.expandString(\"$HIP/file.geo\")
    > '/dir/containing/hip/file/file.geo'
    > >>> hou.text.expandString(\"file`$F+1`.pic\")
    > 'file2.pic'"""

def expandStringAtFrame(str: str, frame: float, expand_tilde: bool = True) -> str:
    """expandStringAtFrame(str, frame_number, expand_tilde=True) -> str

      Expands global variables in the expression. For example:

    > >>> hou.text.expandStringAtFrame('$F', 10)
    > '10'

      Also expands HScript expressions in back-ticks, such as the channel
      reference in this example. This returns the value of the translate X
      parameter for geo1 at the current frame as a string:

    > hou.text.expandStringAtFrame('`ch(\"/obj/geo1/tx\")`', hou.frame())

      The expand_tilde parameter can be set to False to prevent the
      expansion of ~ to your home directory path.

      This function evaluates the string as if it were the contents of a
      non-animated text parameter. To evaluate a straight HScript
      expression (without needing back-ticks), use hou.hscriptExpression.

      Raises hou.OperationFailed exception if the first argument is None."""

def expandHuskFilePath(str: str, frame_start: float = 1.0, frame_inc: float = 1.0, frame_idx: int = 0) -> str:
    """expandHuskFilePath(str, frame_start = 1.0, frame_inc = 1.0, frame_idx =
    0) -> str

        Expands global variables in the expression using the same formatting
        supported by husk to evaluate time varying file paths. The current
        frame number used for substitutions is calculated as frame_start +
        (frame_inc * frame_idx).

      > >>> hou.text.expandHuskFilePath('~/renders/output.<F4>.exr', 1, 1, 0)
      > 'D:/cygwin/home/mtucker/renders/output.0001.exr'

        Unlike the other string expansion functions, this method does not
        expand hscript expressions enclosed in backticks, because husk does
        not support this capability.

        Returns an empty string if the first argument is None."""

def incrementNumberedString(str: str) -> str:
    """incrementNumberedString(str) -> str

      If the string ends with a number, that number is incremented, and
      the resulting new string is returned. If the string does not end
      with a number, a number is appended to the string. This is the
      algorithm used by Houdini to generate uniquely named child nodes
      inside a network.

    > >>> hou.text.incrementNumberedString('name1')
    > 'name2'
    > >>> hou.text.incrementNumberedString('name199')
    > 'name200'
    > >>> hou.text.incrementNumberedString('name')
    > 'name2'
    > >>> hou.text.incrementNumberedString('')
    > '2'"""

def encode(varname: str) -> str:
    """encode(str) -> str

      Houdini VEX variable names are only allowed to contain letters,
      numbers, and underscores, and must not begin with a number. This
      method takes any string, and encodes it into a string that obeys
      these restrictions. The original string can be recovered using the
      decode method. A string that already obeys the rules is returned
      unmodified.

      One exception to this rule is that a string starting with xn__ will
      be encoded even if it is already a valid attribute name. This is
      because xn__ is the prefix used to identify an encoded string. In
      this case, an additional xn__ prefix will be added. This means a
      string can be encoded any number of times, then decoded the same
      number of times to always return to the original string, regardless
      of its contents.

    > >>> hou.text.encode('foo:bar')
    > 'xn__foobar_rla'
    > >>> hou.text.encode('safe_name')
    > 'safe_name'"""

def decode(varname: str) -> str:
    """decode(str) -> str

      Houdini VEX variable names are only allowed to contain letters,
      numbers, and underscores, and must not begin with a number.
      Arbitrary strings can be passed through the encode method to
      generate a string that obeys these restriction. This method takes
      one of these encoded strings, and returns the original string. A
      string that has not been encoded will be returned unmodified.

    > >>> hou.text.decode('xn__foobar_rla')
    > 'foo:bar'
    > >>> hou.text.decode('safe_name')
    > 'safe_name'"""

def encodeAttrib(attribname: str) -> str:
    """encodeAttrib(str) -> str

      Houdini geometry attributes and group names are only allowed to
      contain letters, numbers, and underscores, and must not begin with a
      number. This method takes any string, and encodes it into a string
      that obeys these restrictions. The original string can be recovered
      using the decodeAttrib method. A string that already obeys the rules
      is returned unmodified.

      One exception to this rule is that a string starting with xn__ will
      be encoded even if it is already a valid attribute name. This is
      because xn__ is the prefix used to identify an encoded string. In
      this case, an additional xn__ prefix will be added. This means a
      string can be encoded any number of times, then decoded the same
      number of times to always return to the original string, regardless
      of its contents.

    > >>> hou.text.encodeAttrib('foo:bar')
    > 'xn__foobar_rla'
    > >>> hou.text.encodeAttrib('safe_name')
    > 'safe_name'"""

def decodeAttrib(attribname: str) -> str:
    """decodeAttrib(str) -> str

      Houdini geometry attributes and group names are only allowed to
      contain letters, numbers, and underscores, and must not begin with a
      number. Arbitrary strings can be passed through the encodeAttrib
      method to generate a string that obeys these restriction. This
      method takes one of these encoded strings, and returns the original
      string. A string that has not been encoded will be returned
      unmodified.

    > >>> hou.text.decodeAttrib('xn__foobar_rla')
    > 'foo:bar'
    > >>> hou.text.decodeAttrib('safe_name')
    > 'safe_name'"""

def encodeParm(parmname: str) -> str:
    """encodeParm(str) -> str

      Houdini parameter names are only allowed to contain letters,
      numbers, hash characters (for multiparms), and underscores, and must
      not begin with a number. This method takes any string, and encodes
      it into a string that obeys these restrictions. The original string
      can be recovered using the decodeParm method. A string that already
      obeys the rules is returned unmodified.

      One exception to this rule is that a string starting with xn__ will
      be encoded even if it is already a valid attribute name. This is
      because xn__ is the prefix used to identify an encoded string. In
      this case, an additional xn__ prefix will be added. This means a
      string can be encoded any number of times, then decoded the same
      number of times to always return to the original string, regardless
      of its contents.

    > >>> hou.text.encodeParm('foo:bar')
    > 'xn__foobar_rla'
    > >>> hou.text.encodeParm('safe_name')
    > 'safe_name'"""

def decodeParm(parmname: str) -> str:
    """decodeParm(str) -> str

      Houdini parameter names are only allowed to contain letters,
      numbers, hash characters (for multiparms), and underscores, and must
      not begin with a number. Arbitrary strings can be passed through the
      encodeParm method to generate a string that obeys these restriction.
      This method takes one of these encoded strings, and returns the
      original string. A string that has not been encoded will be returned
      unmodified.

    > >>> hou.text.decodeParm('xn__foobar_rla')
    > 'foo:bar'
    > >>> hou.text.decodeParm('safe_name')
    > 'safe_name'"""

def _obfuscate(text: str) -> str: ...
def _deobfuscate(text: str) -> str: ...
def alphaNumeric(str: str) -> str:
    """alphaNumeric(str) -> str

    Return a string that consists of only numbers, letters, and
    underscores. Any other character in the string is replaced with an
    underscore. This provides an easy way to create strings that are
    safe for use as file names, and almost safe to use as node or
    variable names (variable names usually have the additional condition
    that they are not allowed to start with a number).
    hou.text.variableName can be used to produce a valid variable name.

    Unlike the encode method, the original string cannot be recovered
    from the result of this method. However the results of this method
    are more easily human readable than the result of an encode
    operation."""

def variableName(str: str, safe_chars: Optional[str] = None) -> str:
    """variableName(str, safe_chars=\"\") -> str

      Returns a string that is valid to use as a variable or node name.
      This behaves the same as hou.text.alphaNumeric, but also adds an
      underscore at the beginning of strings that begin with a number. The
      optional safe_chars argument specifies a string with any extra
      characters that should not be converted to underscores.

    > >>> hou.text.variableName('foo:bar')
    > 'foo_bar'
    > >>> hou.text.variableName('123')
    > '_123'
    > >>> hou.text.variableName('foo:?bar', safe_chars=\":\")
    > 'foo:_bar'"""

def abspath(path: str, anchor_path: Optional[str] = None) -> str:
    """abspath(path, base_path = None) -> str

    Returns the supplied path converted to an absolute path. Relative
    paths are treated as relative to the directory specified by
    base_path. If the supplied path is already absolute, the path is
    returned unchanged. If the base_path is not provided, Houdini's
    current working directory is used for this value. The file does not
    need to exist."""

def relpath(path: str, anchor_path: Optional[str] = None) -> str:
    """relpath(path, base_path = None) -> str

    Returns the supplied path converted to a relative path, expressed as
    relative to the directory specified by base_path. If the base_path
    is not provided, Houdini's current working directory is used for
    this value. The file does not need to exist."""

def normpath(path: str) -> str:
    """normpath(path) -> str

      Returns a normalized version of the supplied path. This means that
      all path separators are expressed as forward slashes (even on
      Windows). Any redundant slashes are replaced by a single slash. And
      any relative path components appearing in the middle of the path are
      collapsed.

    > >>> hou.text.normpath('http://foo/bar/..//something')
    > 'http://foo/something'
    > >>> hou.text.normpath('\foo\bar\something\')
    > '/foo/bar/something'
    > >>> hou.text.normpath('../../foo/../bar/../something')
    > '../../something'"""

def collapseCommonVars(*args: Any, **kwargs: Any) -> str:
    """collapseCommonVars(path, vars = ['$HIP', '$JOB']) -> str

    Tests if the path starts with the expanded form of any variable
    passed in through the provided vars list. If it does, that prefix is
    replaced with the corresponding unexpanded variable. For example, if
    $HIP is /home/user/hips, and path is /home/user/hips/file.hip, the
    returned string will be $HIP/file.hip."""

def oclExtractBindings(code: str) -> list[dict[str, Any]]:
    """oclExtractBindings(code) -> tuple of dict

    Parses provided OpenCL code for @BIND commands and returns the set
    of bindings specified."""

def patternRename(str: str, find: str, replace: str) -> str:
    """patternRename(input_string, pattern_find, pattern_replace) -> str

      This function finds the pattern given in pattern_find and replaces
      any occurrences with the pattern given in pattern_replace. For
      example:

    > >>> hou.patternRename(\"foo_bar_baz\", \"*bar*\", \"*blah*\")
    > foo_blah_baz
    > >>> hou.patternRename(\"left_hand_01\", \"left*\", \"right*\")
    > right_hand_01"""

def patternMatch(pattern: str, str: str, ignore_case: bool = False, path_match: bool = False) -> bool:
    """patternMatch(pattern_string, input_string, ignore_case = False,
    path_match = False) -> bool

        This function is case-sensitive. Set ignore_case to True for case-
        insensitive pattern matching.

        This function does not treat path separator characters specially.
        Set path_match to True for path-aware matching, where the multi-
        level wildcard () is required to cover multiple path components.

        Returns 1 if any patterns in the pattern string matches the input
        string, or 0 if no patterns match.

        In order to match, a pattern must match the input string from
        beginning to end. Use wildcards (*) to match substrings, e.g.

      > >>> hou.patternMatch(\"bar\", \"foobarbaz\")
      > False
      > >>> hou.patternMatch(\"*bar*\", \"foobarbaz\")
      > True

        pattern is a space-separated list of one or more patterns. This can
        cause unintuitive behavior of this function. For example:

      > >>> hou.patternMatch(\"foo bar\", \"foo bar\")
      > False

        ...will return 0, because the first argument consists of two
        patterns, foo and bar, and neither of those patterns match foo bar
        (since the pattern must match from beginning to end).

        Similarly,

      > >>> hou.patternMatch(\"foo bar\", \"foo\")
      > True

        ...will return 1, because the string matches the first of the two
        arguments in the pattern (foo and bar).

      > >>> hou.patternMatch(\"/foo/*\", \"/foo/bar/blah\", path_match = True)
      > False

        ...will return 0, because the wildcard only matches against the
        first path component (/bar), leaving the last path component (/blah)
        unmatched.

      > >>> hou.patternMatch(\"/foo/**\", \"/foo/bar/blah\", path_match = True)
      > True

        ...will return 1, because the multi-level wildcard will matches
        against any number of path components."""
