# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.logging

def __init__(*args: Any, **kwargs: Any): ...
def sources() -> list[str]:
    """hou.logging.sources

    Return a tuple of all available log source names.

    USAGE
      sources() -> tuple of str

    The HDK can be used to create additional log sources, but the default
    list of sources returned by this method will be:

      * Generic Logging: Logs generated by Houdini which do not fall into
        any other category.

      * Licensing: Messages related to acquiring licenses to run Houdini.

      * Mocap Stream: Messages generated by motion capture devices.

      * Networking: Messages generated by networking components such as
        Houdini's built-in web server.

      * Node Errors: All messages, warnings, and errors generated by Houdini
        nodes.

      * Rendering: Messages generated by Karma running within the Houdini
        process. Use hou.logging.setRenderLogVerbosity to set the equivalent
        of the verbosity command line argument for external rendering
        processes.

      * Standard Error: Text sent to the stderr stream.

      * Standard Output: Text sent to the stdout stream.

      * USD Logging: Messages generated in the USD logging system."""

def setRenderLogVerbosity(verbosity: int) -> None:
    """hou.logging.setRenderLogVerbosity

    Set the Karma logging verbosity level.

    USAGE
      setRenderLogVerbosity(verbosity)

    Set the current logging verbosity level for Karma running within the
    current Houdini session. This is equivalent to the value of the -V
    values passed to the husk process for a command line render. Values
    range from 0 to 9, and high values can impact the performance of the
    render."""

def renderLogVerbosity() -> int:
    """hou.logging.renderLogVerbosity

    Return the Karma logging verbosity level.

    USAGE
      renderLogVerbosity() -> int

    Return the current logging verbosity level for Karma running within the
    current Houdini session. This is equivalent to the value of the -V
    values passed to the husk process for a command line render. Values
    range from 0 to 9, and high values can impact the performance of the
    render."""

def saveLogsToFile(logs: list[hou.logging.LogEntry], filepath: str) -> None:
    """hou.logging.saveLogsToFile

    Save a tuple of LogEntry objects to a file in JSON format.

    USAGE
      saveLogsToFile(logs, filepath)

    Creates a file containing a JSON representation of a collection of
    hou.logging.LogEntry objects. This file can be converted back to a tuple
    of hou.logging.LogEntry objects by calling hou.logging.loadLogsFromFile
    with the same filepath.


    logs
        Iterable object containing hou.Logging.LogEntry objects which are to
        be saved to disk in a JSON format the preserves all available
        information from each entry.

    filepath
        Path to the file on disk where the log entries will be written."""

def loadLogsFromFile(filepath: str) -> list[hou.logging.LogEntry]:
    """hou.logging.loadLogsFromFile

    Load a tuple of LogEntry objects saved in JSON format from a file.

    USAGE
      loadLogsFromFile(filepath) -> tuple of hou.logging.LogEntry

    Returns a tuple of log entries stored in a JSON file on disk. This file
    was most likely created with a call to hou.logging.saveLogsToFile.


    filepath
        The path to the file containing the JSON representation of an array
        of log entries."""

def createSource(source_name: str) -> None:
    """hou.logging.createSource

    Create a new logging source which can send out log entries generated in
    python.

    USAGE
      createSource(source_name)

    Creates a new logging source that can be passed as the source_name
    argument to the hou.logging.log method. That method will create new
    logging sources automatically, but it can be useful to create logging
    sources before any logs are generated by that source so the user can
    enable the source in the Log Viewer pane.


    source_name
        The name for the new logging source. If this name matches any
        existing source (as returned by hou.logging.sources), this method
        does nothing."""

def log(entry: hou.logging.LogEntry, source_name: Optional[str] = None) -> None:
    """hou.logging.log

    Send a LogEntry object to all log sinks connected to a logging source.

    USAGE
      log(entry, source_name = None)

    Sends a hou.logging.LogEntry from a source with the specified
    source_name. If no source_name is provided, or it is an empty string,
    then the source set on the log entry is used. If that source name is
    also not set, then the default source name of Python Logging is used.


    entry
        A hou.logging.LogEntry object which will be sent from the named
        logging source to all connected sinks. The source attribute of the
        log entry object will be automatically overridden to use the
        specified source_name.

    source_name
        The name of the logging source from which the log entry is sent.
        Only logging sources compatible with sending python log entries can
        be used here. If no value is specified, the value is assumed to be
        Python Logging. Other valid values are Generic Logging, or any value
        that does not match an existing logging source name. In this case a
        new logging source is automatically created as if
        hou.logging.createSource had been called."""

def defaultSink(force_create: bool = False) -> hou.logging.MemorySink:
    """hou.logging.defaultSink

    Return a shared memory sink object owned by the current Houdini session.

    USAGE
      defaultSink(force_create) -> hou.logging.MemorySink or None

    Every Houdini session can have a single shared hou.logging.MemorySink
    object which is used by all Log Viewer panes to display logs generated
    by the current Houdini session. This function provides access to this
    shared sink object.


    force_create
        If the default sink for the current Houdini session has not been
        created, this parameter controls whether the default sink should be
        created. Otherwise this method will return None. If the default sink
        has already been created, this parameter has no effect."""

class Sink(object):
    """hou.logging.Sink

    Represents a logging destination.

    This is an abstract base class for all logging sink classes. It provides
    the common methods for connecting and disconnecting sources to the sink."""

    def __init__(self, *args: Any, **kwargs: Any): ...
    def connectedSources(self) -> list[str]:
        """connectedSources() -> tuple of str

        Returns the names of sources connected to this sink."""
    def connect(self, source_name: str) -> None:
        """connect(source_name)

        Connect a source to this sink object. The source_name should be one
        of the values return by a call to hou.logging.sources."""
    def disconnect(self, source_name: str) -> None:
        """disconnect(source_name)

        Disconnect a source from this sink object. The source_name should be
        one of the values returned by the connectedSources method."""
    def setFilterCallback(self, callback: Any) -> None:
        """setFilterCallback(callback)

        Associates a callable object with this log sink which is called
        every time a log entry is generated by a source connected to this
        sink. The callback should take one argument, which is a
        hou.logging.LogEntry object. If this callback returns False, the log
        entry will not be stored or otherwise processed by this sink object."""

class FileSink(hou.logging.Sink):
    """hou.logging.FileSink

    Represents a logging destination that writes log entries to a file.

    This kind of sink can be used to send log entries to a file on disk.
    Some of the log entry details are lost in writing the data to disk, as
    each log entry is output simply as a time stamp followed by the message
    text. So for most situations, using the Log Viewer pane to investigate
    log entries will be preferable.


    Tip
        In order to ensure all logs are captured and committed to disk, this
        sink type opens the log file, writes the log entry, and closes the
        file for each log message. This can introduce noticeable performance
        issues if a large amount of information is being logged. Therefore
        it is strongly recommended that the destination file be local to the
        machine running Houdini, and preferably be kept on an SSD hard
        drive."""

    def __init__(self, filepath: str):
        """__init__(self, filepath)

        Creates a new file sink object which writes logs to the specified
        file path."""
    def filePath(self) -> str:
        """filePath() -> str

        Returns the path to the file where logs are written."""

class LogEntry(object):
    """hou.logging.LogEntry

    Represents a single log message that is sent by a source to a sink."""

    def __init__(
        self,
        message: Optional[str] = None,
        source: Optional[str] = None,
        source_context: Optional[str] = None,
        severity: Optional[hou.EnumValue] = None,
        verbosity: int = 0,
        time: float = 0.0,
        thread_id: int = 0,
        has_external_info: bool = False,
        external_host_name: Optional[str] = None,
        external_identifier: Optional[str] = None,
        external_command_line: Optional[str] = None,
        external_process_id: int = 0,
    ):
        """__init__(self, message = None, source = None, source_context = None,
        severity = None, verbosity = 0, time = 0.0, thread_id = 0,
        has_external_info = False, external_host_name = None,
        external_identifier = None, external_command_line = None,
        external_process_id = 0)

            Return a new LogEntry with the provided data members."""
    def source(self) -> str:
        """source() -> str

        Return the names of the source that generated this log entry."""
    def sourceContext(self) -> str:
        """sourceContext() -> str

        Return an optional string that identifies the context within the
        source that generated this log entry. One example is that the Node
        Errors source sets this value to the path of the specific Houdini
        node that generated the log entry."""
    def message(self) -> str:
        """message() -> str

        Return the main log entry message text."""
    def severity(self) -> hou.EnumValue:
        """severity() -> hou.severityType

        Return an optional severity value for the log entry. This value will
        be set for node error logs, USD logs, and other sources with a well
        defined set of logging severity levels."""
    def verbosity(self) -> int:
        """verbosity() -> int

        Return an optional verbosity value for the log entry. This value
        will be set for rendering logs, and indicates the minimum
        hou.logging.renderLogVerbosity level required for Karma to generate
        this log entry."""
    def time(self) -> float:
        """time() -> float

        Return the time at which this log entry was generated. This value is
        expressed as the number of seconds since January 1, 1970, 00:00:00
        (UTC). This value can be converted to a local time using the python
        time module using code such as time.strftime(\"%H:%M:%S\",
        time.localtime(log.time())). Although log entries from a single
        source should always arrive in chronological order, some sources may
        delay their log reporting, and so log entries may arrive at a sink
        out of order."""
    def threadId(self) -> int:
        """threadId() -> int

        Return a number that uniquely identifies within a given Houdini
        session which thread in the process generated the log entry. This
        can be useful to establish a chronology of log entries when multiple
        threads are generating logs simultaneously."""
    def hasExternalInfo(self) -> bool:
        """hasExternalInfo() -> bool

        Return True if this log entry was generated by a process other than
        the current Houdini session. In this case, the various methods
        starting with external will return meaningful information. If this
        method returns False, the external methods should not be called on
        this object."""
    def externalHostName(self) -> str:
        """externalHostName() -> str

        If the external process was running on a different machine, return
        the name of the machine running the process. Otherwise return an
        empty string."""
    def externalIdentifier(self) -> str:
        """externalIdentifier() -> str

        Return an optional string to help identify the machine or process
        which generated the log entry. The meaning of this value varies
        depending on the logging source."""
    def externalCommandLine(self) -> str:
        """externalCommandLine() -> str

        Return the full command line used to launch the external process
        that generated this log entry."""
    def externalProcessId(self) -> int:
        """externalProcessId() -> int

        Return the process identifier (pid) of the process that generated
        the log entry."""
    def _asVoidPointer(self) -> None: ...

class MemorySink(hou.logging.Sink):
    """hou.logging.MemorySink

    Represents a logging destination that stores log entries in memory.

    All log entries sent to this sink are held in memory forever unless
    stealLogEntries is called. Depending on the frequency of logging, this
    can eventually result in a very large amount of memory being consumed by
    these logs, however in most normal operating circumstances this is very
    unlikely to be a problem."""

    def __init__(self):
        """hou.logging.MemorySink

        Represents a logging destination that stores log entries in memory.

        All log entries sent to this sink are held in memory forever unless
        stealLogEntries is called. Depending on the frequency of logging, this
        can eventually result in a very large amount of memory being consumed by
        these logs, however in most normal operating circumstances this is very
        unlikely to be a problem."""
    def logEntries(self) -> list[hou.logging.LogEntry]:
        """logEntries() -> iterable of hou.logging.LogEntry

        Return an iterable object that represents all the log entries held
        in memory by this sink object."""
    def stealLogEntries(self) -> list[hou.logging.LogEntry]:
        """stealLogEntries() -> tuple of hou.logging.LogEntry

        Returns a tuple of all log entries that were held in memory by this
        sink object. In addition, all log entries owned by this sink object
        are cleared from memory. Thus subsequent calls to logEntries or
        stealLogEntries will not return any of these log entries again."""
