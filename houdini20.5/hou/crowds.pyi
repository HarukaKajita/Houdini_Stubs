# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.crowds

from hou import AgentShape, AgentDefinition, AgentClip

def __init__(*args: Any, **kwargs: Any): ...
def addBlendshapeInputs(base_shape_geo: hou.Geometry, shapes: tuple[AgentShape], channel_names: tuple[str]) -> None:
    """addBlendshapeInputs(self, base_shape_geo, shapes, channel_names)

    Adds blendshape inputs to a shape's geometry. This sets up the
    required detail attributes (blendshape_shapenames and
    blendshape_channels) on the base shape's geometry. For an existing
    agent shape, blendshape inputs can also be added using
    hou.AgentShape.addBlendshapeInputs.


    base_shape_geo
        A modifiable hou.Geometry for the base shape.

    shapes
        A hou.AgentShape sequence to add as blendshape inputs.
        hou.AgentShapeLibrary.addShape should be called separately to
        add these shapes to the shape library.

    channel_names
        A str sequence specifying the channel name to use for each
        shape. Raises hou.InvalidSize if the length does not match the
        shapes list."""

def addInBetweenShapes(primary_shape_geo: hou.Geometry, shapes: tuple[AgentShape], weights: tuple[float]) -> None:
    """addInBetweenShapes(self, primary_shape_geo, shapes, weights)

    Adds in-between shapes to a blendshape input. This sets up the
    required detail attributes (blendshape_shapenames and
    blendshape_inbetweenweights) on the primary shape's geometry. For an
    existing agent shape, in-between shapes can also be added using
    hou.AgentShape.addInBetweenShapes.


    primary_shape_geo
        A modifiable hou.Geometry for the primary shape.

    shapes
        A hou.AgentShape sequence to add as in-between shapes.
        hou.AgentShapeLibrary.addShape should be called separately to
        add these shapes to the shape library.

    weights
        A float sequence specifying the weight that each in-between
        shape is applied at. Raises hou.InvalidSize if the length does
        not match the shapes list."""

def setBlendshapeDeformerParms(*args: Any, **kwargs: Any) -> None:
    """setBlendshapeDeformerParms(self, base_shape_geo, attribs=\"P N\",
    point_id_attrib=\"id\", prim_id_attrib=\"id\")

        Adds attributes to the geometry to specify parameters for the
        blendshapes deformer. This creates the following detail attributes:
        blendshape_attribs, blendshape_ptidattr, and blendshape_primidattr.
        For an existing agent shape, the deformer parameters can be set
        using hou.AgentShape.setBlendshapeDeformerParms.


        attribs
            Specifies a list or pattern of attributes to be blended by the
            deformer.

        point_id_attrib
            Specifies the name of a point attribute used to match up points
            between the different blendshape inputs.

        prim_id_attrib
            Specifies the name of a primitive attribute used to match up
            points between the different blendshape inputs."""

def findAgentDefinitions(*args: Any, **kwargs: Any) -> list[hou.AgentDefinition]:
    """findAgentDefinitions(geometry, group = \"\",
    group_type=hou.geometryType.Primitives) -> tuple of hou.AgentDefinition

        Returns a list of the unique agent definitions in the geometry.

        This is equivalent to the following code, but is significantly
        faster.

      > definitions = set()
      > for prim in geometry.globPrims(group):
      >     if prim.type() == hou.primType.Agent:
      >         definitions.add(prim.definition())
      >
      > return definitions

        geometry
            A hou.Geometry.

        group
            An optional group string to filter which primitives are
            inspected. The pattern format is the same as the format used for
            group parameters on SOP nodes.

        group_type
            A hou.geometryType indicating whether to parse the group string
            as a point or primitive group. If the value is None, the group
            will be guessed by parsing it as a point group if it fails to
            parse as a primitive group."""

def replaceAgentDefinitions(*args: Any, **kwargs: Any) -> None:
    """replaceAgentDefinitions(geometry, new_definition_map, group = \"\",
    group_type=hou.geometryType.Primitives)

        Replaces agent definitions in the geometry with new versions. This
        is a useful convenience function when modifying each agent
        definition in the geometry, particularly when also using
        hou.crowds.findAgentDefinitions.

        For example:

      > defns = hou.crowds.findAgentDefinitions(geo, group)
      > new_defn_map = {}
      > for defn in defns:
      >     new_defn = defn.freeze()
      >     new_defn_map[defn] = new_defn
      >
      >     # Add a clip to the new agent definition.
      >     new_defn.addClip(...)
      >
      > # Switch all agents in the group to their respective new agent definition.
      > hou.crowds.replaceAgentDefinitions(geo, new_defn_map, group)

        geometry
            A modifiable hou.Geometry.

        new_definition_map
            A dictionary mapping each hou.AgentDefinition to a
            hou.AgentDefinition that it should be replaced by.

        group
            An optional group string to filter which primitives are
            modified. The pattern format is the same as the format used for
            group parameters on SOP nodes.

        group_type
            A hou.geometryType indicating whether to parse the group string
            as a point or primitive group. If the value is None, the group
            will be guessed by parsing it as a point group if it fails to
            parse as a primitive group."""

def computeLocalTransforms(rig: hou.AgentRig, world_xforms: list[hou.Matrix4]) -> list[hou.Matrix4]:
    """computeLocalTransforms(self, rig, xforms) -> tuple of hou.Matrix4

    Converts transforms from world space to local space using the
    provided rig.


    rig
        A hou.AgentRig, which specifies the transform hierarchy.

    xforms
        A sequence of hou.Matrix4, with a world space transform for each
        joint in the rig. Raises hou.InvalidSize if the length does not
        match hou.AgentRig.transformCount."""

def computeWorldTransforms(rig: hou.AgentRig, local_xforms: list[hou.Matrix4]) -> list[hou.Matrix4]:
    """computeWorldTransforms(self, rig, xforms) -> tuple of hou.Matrix4

    Converts transforms from local space to world space using the
    provided rig.


    rig
        A hou.AgentRig, which specifies the transform hierarchy.

    xforms
        A sequence of hou.Matrix4, with a local space transform for each
        joint in the rig. Raises hou.InvalidSize if the length does not
        match hou.AgentRig.transformCount."""

def computeRotationLimits(
    rig: hou.AgentRig, clips: tuple[AgentClip], xform_idx: int, parent_xform_idx: int
) -> dict[str, Any]:
    """computeRotationLimits(rig, clips, transform, parent_transform) -> dict
    of str to values

        Computes rotation limits for the specified joint based on the range
        of motion in the provided clips.

        The return value is a dictionary with the following keys:

      * anchor_pos: A hou.Vector3 containing the cone's anchor position.

      * rotation: A hou.Vector3 containing the cone's orientation.

      * child_rotation: A hou.Vector3 containing the child's orientation.

      * twist_limits: A hou.Vector2 containing the rotation limits for the
        twist axis.

      * up_limits: A hou.Vector2 containing the rotation limits for the up
        axis.

      * out_limits: A hou.Vector2 containing the rotation limits for the out
        axis.


        rig
            A hou.AgentRig.

        clips
            A list of hou.AgentClip.

        transform
            Index of a transform in the agent's rig.

        parent_transform
            Index of the parent transform in the agent's rig."""

def shapeDeformers() -> list[hou.AgentShapeDeformer]:
    """shapeDeformers() -> tuple of hou.AgentShapeDeformer

    Returns a list of the available shape deformers."""

def findShapeDeformer(name: str) -> hou.AgentShapeDeformer:
    """findShapeDeformer(name) -> hou.AgentShapeDeformer

    Finds the shape deformer with the specified name, or None if no such
    deformer exists."""

def applyUsdProcedural(
    stage: Any,
    selection_rule: hou.LopSelectionRule,
    camera_path: str,
    resolution: tuple[int, int],
    lod_threshold: float,
    optimize_identical_poses: bool,
    frame: float,
    prototype_material: str,
    instance_material: str,
    default_material: str,
) -> None:
    """applyUsdProcedural(self, stage, selection_rule, camera_path, resolution,
    lod_threshold, frame, optimize_identical_poses, prototype_material,
    instance_material, default_material)

        Applies the crowd procedural to a USD stage.

        Raises hou.OperationFailed if an error occurred when applying the
        procedural.


        stage
            The USD stage to modify.

        selection_rule
            A hou.LopSelectionRule specifying the SkelRoot instances the
            procedural should be applied to.

        camera_path
            A path to a Camera primitive in the stage to use for evaluating
            LOD.

        resolution
            A pair of integers specifying the output image's resolution.

        lod_threshold
            The threshold at which the LOD optimization will be used. The
            default value of 1.0 means that the optimization will be used
            when tolerance between the agent poses is less than
            approximately 1 pixel. Lower values can eliminate deformed
            geometry differences which might still be noticeable depending
            on the scene, but make it less likely for the LOD optimization
            to trigger and may increase the render's memory footprint.

        optimize_identical_poses
            A boolean value indicating whether to instance the deformed
            geometry for agents with exactly the same pose (including
            foreground agents). In most scenarios it is rare for agents to
            have identical poses (due to randomizing clip speeds, time
            offsets, etc) so this can typically be disabled to eliminate
            unnecessary computation.

        frame
            The time sample to apply the procedural at.

        prototype_material
            The path to a material to apply to SkelRoot primitives whose
            deformed geometry became a prototype for background instances.

        instance_material
            The path to a material to apply to SkelRoot primitives which
            became an instance of another SkelRoot's deformed geometry.

        default_material
            The path to a material to apply to SkelRoot primitives which
            were not modified by the crowd procedural."""
