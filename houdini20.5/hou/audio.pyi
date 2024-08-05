# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.audio

def __init__(*args: Any, **kwargs: Any): ...
def turnOffAudio() -> None:
    """turnOffAudio()

    Turn off the audio playback."""

def useTimeLineMode() -> None:
    """useTimeLineMode()

    Put the Audio Panel into a scrub mode.

    When the Audio Panel is in the scrub (a.k.a. timeline) mode, Houdini
    will play the audio during the animation or when scrubbing the thumb
    in the playbar."""

def useTimeSliceMode() -> None:
    """useTimeSliceMode()

    Put the Audio Panel into realtime (a.k.a. timeslice) mode."""

def useTestMode() -> None:
    """useTestMode()

    Put the Audio Panel into a mode that tests the audio playback.

    When the Audio Panel is in the test mode, it will play the entire
    audio soundtrack. The test can be stopped and resumed with stop()
    and play() functions.

    The sound will not play when scrubbing the thumb in the playbar or
    when playing the animation in the playbar. The audio must be in
    either scrub or realtime mode for playing the sound during animation
    or scrubbing."""

def setMono(on: bool) -> None:
    """setMono(on)

    Set whether the audio will play in mono or stereo mode."""

def setVolumeTied(on: bool) -> None:
    """setVolumeTied(self, on)

    Set whether changing the volume of one channel affects the volume of
    the other channel. If so, both channels will have the same volume
    set."""

def setMeter(on: bool) -> None:
    """setMeter(on)

    Ses whether the meter will show the volume levels during the audio
    playback."""

def setLeftVolume(volume: float) -> None:
    """setLeftVolume(value)

    Set the volume for the left audio channel."""

def setRightVolume(volume: float) -> None:
    """setRightVolume(value)

    Set the volume for the right channel."""

def useChops() -> None:
    """useChops()

    Set the Audio Panel to use a CHOP node for the audio."""

def useAudioFile() -> None:
    """useAudioFile()

    Set the Audio Panel to use a disk file for the audio."""

def setChopPath(node_path: str) -> None:
    """setChopPath(path)

    Set the Audio Panel to play the sound inside a CHOP node. Houdini
    plays this sound during testing, animation or scrubbing. See also
    hou.audio.useChops.


    path
        A string containing the path to the CHOP node."""

def setAudioFileName(file_name: str) -> None:
    """setAudioFileName(path)

    Set the Audio Panel to play the sound inside an audio file. Houdini
    plays this sound during testing, animation or scrubbing. See also
    hou.audio.useAudioFile."""

def setAudioOffset(time_offset: float) -> None:
    """setAudioOffset(offset)

    Set the time offset of the sound to sync the audio. This offset,
    specified in seconds, will coincide with the audio frame. See also
    hou.audio.setAudioFrame."""

def setAudioFrame(frame: float) -> None:
    """setAudioFrame(frame)

    Set the frame to sync the audio. The audio offset (in seconds) will
    coincide with this frame. See also hou.audio.setAudioOffset."""

def setScrubRepeat(on: bool) -> None:
    """setScrubRepeat(on)

    Set whether the sound chunk is repeated during scrubbing. See also
    hou.audio.useTimeSliceMode."""

def setScrubSustain(sustain: float) -> None:
    """setScrubSustain(value)

    Set the length of time the that the sound chunk is repeatedly played
    when scrubbing comes to a standstill on a particular single frame.
    In practice, when the value is zero, no sound will be played when
    scrubbing keeps hovering over one frame. But, when the value is non-
    zero, a small sound chunk will keep playing repeatedly with a
    specified frequency. See also hou.audio.useTimeSliceMode."""

def setScrubRate(scrub_rate: float) -> None:
    """setScrubRate(value)

    When the sustain period is non-zero, the small chunk of the sound
    will be repeated with this frequency when the scrubbing comes to a
    standstill at a single frame. See also hou.audio.useTimeSliceMode."""

def reverse() -> None:
    """reverse()

    When the Audio Panel is in the test mode, start playing the sound in
    reverse."""

def stop() -> None:
    """stop()

    When the Audio Panel is in the test mode, stop the test playback if
    any audio is currently playing."""

def play() -> None:
    """play()

    When the Audio Panel is in the test mode, start playing the Audio
    Panel's specified audio file or CHOP. See also
    hou.audio.setAudioFileName and hou.audio.setChopPath."""

def setLooping(on: bool) -> None:
    """setLooping(on)

    When the Audio Panel is in the test mode, set whether the test
    should start playing from the beginning once the end is reached. See
    also hou.audio.setRewind."""

def setRewind(on: bool) -> None:
    """setRewind(on)

    When the Audio Panel is in the test mode, set whether the sound
    should rewind to the beginning when the test is stopped. If not, on
    subsequent start, the sound will resume from the point at which it
    was previously stopped. See also hou.audio.setLooping."""
