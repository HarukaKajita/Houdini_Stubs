# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.galleries

def __init__(*args: Any, **kwargs: Any): ...
def galleries() -> list[hou.Gallery]:
    """galleries() -> tuple of hou.Gallery

    Return a tuple containing all the galleries currently installed in
    the Houdini session."""

def galleryEntries(
    name_pattern: Optional[str] = None,
    label_pattern: Optional[str] = None,
    keyword_pattern: Optional[str] = None,
    category: Optional[str] = None,
    node_type: Optional[hou.NodeType] = None,
) -> list[hou.GalleryEntry]:
    """galleryEntries(name_pattern=None, label_pattern=None,
    keyword_pattern=None, category=None, node_type=None) -> tuple of
    hou.GalleryEntry

        Return a tuple of hou.GalleryEntry objects matching the search
        criteria. The result is the intersection of the matches against all
        the parameters. If you call this function with no parameters, it
        returns all the gallery entries. See also
        hou.Gallery.galleryEntries.

        Unless a parameter is None, the results are filtered by the
        following:


        name_pattern
            gallery entry names matching this pattern

        label_pattern
            gallery entry label names matching this pattern

        keyword_pattern
            gallery entries that have a keyword matching this pattern

        category
            gallery entries in a category matching this pattern

        node_type
            gallery entries that can be applied to this node type

        This example prints all the gallery entries starting with a b that
        have the Material keyword.

      > >>> hou.galleries.galleryEntries(\"b*\", keyword_pattern=\"Material\")
      > (<hou.GalleryEntry \"basic_surface\">, <hou.GalleryEntry \"bumpy_glass\">, ...)

        This example prints the name and description of all the entries in
        the Metals category:

      > >>> for entry in hou.galleries.galleryEntries(category=\"Metals\"):
      > ...     print \"%s: %s\" % (entry.name(), entry.description())
      > chrome: Very bright metal with mirror reflections
      > aged_metal: Aged metal material with ray traced or environment mapped reflections
      > ...

        This example prints the gallery entry names for the Lsystem SOP.

      > >>> node_type = hou.nodeType(hou.sopNodeTypeCategory(), \"lsystem\")
      > >>> for entry in hou.galleries.galleryEntries(node_type=node_type):
      > ...     print entry.name()
      > planta
      > plantb
      > plantc
      > ...
      > sympodial_tree
      > ternary_tree
      > wheel"""

def installGallery(gallery_path: str) -> hou.Gallery:
    """installGallery(gallery_path) -> hou.Gallery or None

    Load a gallery into the current Houdini session.


    gallery_path
        The file path of the gallery to be installed."""

def removeGallery(gallery_path: str) -> bool:
    """removeGallery(gallery_path) -> bool

    Remove a gallery from the current Houdini session. Returns False if
    the specified gallery file was not installed.


    gallery_path
        The file path of the gallery to be removed."""

def createGalleryEntry(gallery_path: str, entry_name: str, node: Optional[hou.Node] = None) -> hou.GalleryEntry:
    """createGalleryEntry(gallery_path, entry_name, node) -> hou.GalleryEntry
    or None

        Create and return a new gallery entry.


        gallery_path
            The path of the gallery file in which the new element should be
            stored.

        entry_name
            The name of the new gallery entry.

        node
            The operator node from which the new gallery entry should copy
            the settings. The settings include parameter values, channels,
            spare parameters etc, and also the children nodes if the node is
            a subnetwork."""
