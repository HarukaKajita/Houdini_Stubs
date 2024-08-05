# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.ik

def __init__(*args: Any, **kwargs: Any): ...
def solveFBIK(*args: Any, **kwargs: Any) -> None:
    """hou.ik.solveFBIK

    Applies a full-body inverse kinematics algorithm to a skeleton.

    USAGE
      solveFBIK(skeleton, targets, iters=30, tolerance=1e-5, pin_root=False)

    This solver is equivalent to the solvefbik() VEX function.


    skeleton
        The hou.ik.Skeleton to solve. The joints' transforms will be updated
        with the solution.

    targets
        A list of hou.ik.Target specifying the goal transforms for
        particular joints. Raises hou.ValueError if any of the targets are
        not attached to a joint, or if multiple targets are attached to the
        same joint.

    iters
        The maximum number of iterations to perform. The solver may
        terminate early if the tolerance parameter is used.

    tolerance
        The tolerance to use when checking for convergence, defaults to
        1e-5. If positions converge to within this tolerance, the algorithm
        will stop. If 0, the solver will always perform exactly iters
        iterations.

    pin_root
        Specifies whether the root joint is allowed to translate."""

def solvePhysFBIK(*args: Any, **kwargs: Any) -> None:
    """hou.ik.solvePhysFBIK

    Applies a full-body inverse kinematics algorithm to a skeleton, with
    optional control over the center of mass.

    USAGE
      solvePhysFBIK(skeleton, targets, com_target=None, iters=30,
      damping=0.5, tolerance=1e-5)

    This solver is equivalent to the solvephysfbik() VEX function.


    skeleton
        The hou.ik.Skeleton to solve. The joints' transforms will be updated
        with the solution.

    targets
        A list of hou.ik.Target specifying the goal transforms for
        particular joints. Raises hou.ValueError if any of the targets are
        not attached to a joint, or if multiple targets are attached to the
        same joint.

    com_target
        An optional hou.ik.Target which specifies the goal position of the
        skeleton's center of mass.

    iters
        The maximum number of iterations to perform. The solver may
        terminate early if the tolerance parameter is used.

    damping
        Damping factor for the solver. Larger values will produce more
        stable results when, for example, a target is unreachable. A value
        that is too large, however, will require more iterations to
        converge. Around 0.5 is typically a suitable initial value.

    tolerance
        The tolerance to use when checking for convergence, defaults to
        1e-5. If positions converge to within this tolerance, the algorithm
        will stop. If 0, the solver will always perform exactly iters
        iterations."""

def _newSkeleton() -> hou.ik.Skeleton: ...
def _newTarget(
    joint: Joint,
    goal_transform: hou.Matrix4,
    joint_offset: hou.Matrix4,
    target_type: hou.EnumValue,
    weight: float,
    priority: int,
    depth: int,
) -> hou.ik.Target: ...

class targetType(object):
    def __init__(self, *args: Any, **kwargs: Any): ...

class Joint(object):
    """hou.ik.Joint

    Represents a joint in an inverse kinematics skeleton.

    Joints can be created using hou.ik.Skeleton.addJoint.

    RELATED

      * hou.ik.Skeleton

      * hou.ik.Target"""

    def __init__(self, *args: Any, **kwargs: Any): ...
    def worldTransform(self) -> hou.Matrix4:
        """worldTransform() -> hou.Matrix4

        Returns the joint's world space transform."""
    def setWorldTransform(self, xform: hou.Matrix4) -> None:
        """setWorldTransform(xform)

        Sets the joint's world space transform (a hou.Matrix4)."""
    def parent(self) -> hou.ik.Joint:
        """parent() -> hou.ik.Joint

        Returns the joint's parent, or None for a root joint."""
    def setParent(self, parent: Joint) -> None: ...
    def rotationOrder(self) -> str:
        """rotationOrder() -> str

        Returns the joint's rotation order. See
        hou.ik.Joint.setRotationOrder."""
    def setRotationOrder(self, rotate_order: str) -> None:
        """setRotationOrder(rotate_order)

        Sets the joint's rotation order.


        rotate_order
            A string containing a permutation of the letters x, y, and z
            that determines the order in which rotations are performed about
            the coordinate axes."""
    def rotationWeights(self) -> hou.Vector3:
        """rotationWeights() -> hou.Vector3

        Returns the weights for the joint's rotation axes. See
        hou.ik.Joint.setRotationWeights."""
    def setRotationWeights(self, weights: hou.Vector3) -> None:
        """setRotationWeights(weights)

        Sets a hou.Vector3 specifying the weight of each rotation axis.
        Given a larger relative weight, the solution will tend to be
        achieved by rotating around that axis. A weight of zero will disable
        the rotation axis."""
    def translationWeights(self) -> hou.Vector3:
        """translationWeights() -> hou.Vector3

        Returns the weights for the joint's translation axes. See
        hou.ik.Joint.setTranslationWeights."""
    def setTranslationWeights(self, weights: hou.Vector3) -> None:
        """setTranslationWeights(weights)

        Sets a hou.Vector3 specifying the weight of each translation axis.
        Given a larger relative weight, the solution will tend to be
        achieved by translating along that axis. A weight of zero will
        disable the translation axis. To set up an unpinned root joint, the
        root's translation weight should be non-zero (e.g. hou.Vector3(1, 1,
        1))."""
    def mass(self) -> float:
        """mass() -> float

        Returns the mass of the body attached to this joint. See
        hou.ik.Joint.setMass."""
    def setMass(self, mass: float) -> None:
        """setMass(mass)

        Sets the mass of the body attached to this joint. This is only used
        by solvers that support center of mass targets, such as
        hou.ik.solvePhysFBIK."""
    def localCenterOfMass(self) -> hou.Vector3:
        """localCenterOfMass() -> hou.Vector3

        Returns the local space position of the body attached to this joint.
        See hou.ik.Joint.setLocalCenterOfMass."""
    def setLocalCenterOfMass(self, com: hou.Vector3) -> None:
        """setLocalCenterOfMass(position)

        Sets the local space position of the body attached to this joint. A
        position of hou.Vector3(0, 0, 0) will position the center of mass at
        the joint's world space position. This is only used by solvers that
        support center of mass targets, such as hou.ik.solvePhysFBIK."""
    def rotationLimits(self) -> tuple[hou.Vector3, hou.Vector3]:
        """rotationLimits() -> (hou.Vector3, hou.Vector3)

        Returns the lower and upper rotation limits (in radians) for the
        joint, relative to the rest transform. If
        hou.ik.Joint.hasRotationLimits() is False, (None, None) is returned."""
    def setRotationLimits(self, lower: hou.Vector3, upper: hou.Vector3) -> None:
        """setRotationLimits(lower, upper)

        Sets the lower and upper rotation limits (a hou.Vector3 in radians)
        for the joint."""
    def translationLimits(self) -> tuple[hou.Vector3, hou.Vector3]:
        """translationLimits() -> (hou.Vector3, hou.Vector3)

        Returns the lower and upper translation limits for the joint,
        relative to the rest transform."""
    def setTranslationLimits(self, lower: hou.Vector3, upper: hou.Vector3) -> None:
        """setTranslationLimits(lower, upper)

        Sets the lower and upper translation limits for the joint."""
    def restTransform(self) -> hou.Matrix4:
        """restTransform() -> hou.Matrix4

        Returns the joint's rest pose, or None if it has not been set."""
    def setRestTransform(self, xform: hou.Matrix4) -> None:
        """setRestTransform(xform)

        Sets a local space hou.Matrix4 specifying the joint's rest pose. If
        not specified, the identity transform is used.

        The solver will attempt to maintain this local transform based on
        the rest rotation weights and rest translation weights. This has a
        priority lower than any of the end effector targets.

        Additionally, joint limits are enforced relative to this rest
        transform."""
    def restRotationWeights(self) -> hou.Vector3:
        """restRotationWeights() -> hou.Vector3

        Returns the rest weights for the joint's rotation axes. See
        hou.ik.Joint.setRestRotationWeights."""
    def setRestRotationWeights(self, weights: hou.Vector3) -> None:
        """setRestRotationWeights(weights)

        Sets a hou.Vector3 specifying how strongly the solver attempts to
        match the rest transform for the rotation axes. A value of 0.1 is
        typically a suitable value when enabling this behavior, and a value
        of 0 will disable the constraint. The default value is {0,0,0}."""
    def restTranslationWeights(self) -> hou.Vector3:
        """restTranslationWeights() -> hou.Vector3

        Returns the rest weights for the joint's translation axes. See
        hou.ik.Joint.setRestTranslationWeights."""
    def setRestTranslationWeights(self, weights: hou.Vector3) -> None:
        """setRestTranslationWeights(weights)

        Sets a hou.Vector3 specifying how strongly the solver attempts to
        match the rest transform for the translation axes. A value of 0.1 is
        typically a suitable value when enabling this behavior, and a value
        of 0 will disable the constraint. The default value is {0,0,0}."""

class Skeleton(object):
    """hou.ik.Skeleton

    Represents a skeleton for use with inverse kinematics solvers.

    RELATED

      * hou.ik.Joint"""

    def __init__(self):
        """hou.ik.Skeleton

        Represents a skeleton for use with inverse kinematics solvers.

        RELATED

          * hou.ik.Joint"""
    def addJoint(self, *args: Any, **kwargs: Any) -> hou.ik.Joint:
        """addJoint(self, world_transform=hou.Matrix4(1.0), parent=None,
        rotation_weights=hou.Vector3(1,1,1),
        translation_weights=hou.Vector3(0,0,0), mass=1.0,
        local_com=hou.Vector3(0,0,0)) -> hou.ik.Joint

            Appends a new joint to the skeleton.


            world_transform
                See hou.ik.Joint.setWorldTransform

            parent
                See hou.ik.Joint.setParent

            rotation_weights
                See hou.ik.Joint.setRotationWeights

            translation_weights
                See hou.ik.Joint.setTranslationWeights

            mass
                See hou.ik.Joint.setMass

            local_com
                See hou.ik.Joint.setLocalCenterOfMass"""
    def joints(self) -> list[hou.ik.Joint]:
        """joints(self) -> tuple of hou.ik.Joint

        Returns a list of the joints in the skeleton. The list follows the
        order in which the joints were added to the skeleton."""
    def centerOfMass(self) -> hou.Vector3:
        """centerOfMass() -> hou.Vector3

        Returns the world space position of the skeleton's center of mass.
        This is computed from the mass, center of mass, and world transform
        of each joint."""

class Target(object):
    """hou.ik.Target

    Represents a position or orientation target for inverse kinematics
    solvers.

    RELATED

      * hou.ik.Joint

      * hou.ik.targetType"""

    def __init__(self, *args: Any, **kwargs: Any):
        """__init__(joint=None, goal_transform=hou.Matrix4(1.0),
        joint_offset=hou.Matrix4(1.0), target_type=hou.ik.targetType.Position,
        weight=1.0, priority=0, depth=-1)

            Creates a new target.


            joint
                See hou.ik.Target.setJoint.

            goal_transform
                See hou.ik.Target.setGoalTransform.

            joint_offset
                See hou.ik.Target.setJointOffset.

            target_type
                See hou.ik.Target.setTargetType.

            weight
                See hou.ik.Target.setWeight.

            priority
                See hou.ik.Target.setPriority.

            depth
                See hou.ik.Target.setDepth."""
    def joint(self) -> hou.ik.Joint:
        """joint() -> hou.ik.Joint

        Returns the joint that the target is attached to, or None."""
    def setJoint(self, joint: Joint) -> None:
        """setJoint(joint)

        Sets the hou.ik.Joint that the target is attached to. This may be
        None if, for example, the target defines a goal position for the
        skeleton's center of mass."""
    def goalTransform(self) -> hou.Matrix4:
        """goalTransform() -> hou.Matrix4

        Returns the world space goal transform."""
    def setGoalTransform(self, xform: hou.Matrix4) -> None:
        """setGoalTransform(xform)

        Sets the target world space transform (a hou.Matrix4) for the joint."""
    def jointOffset(self) -> hou.Matrix4:
        """jointOffset() -> hou.Matrix4

        Returns the local space joint offset transform. See
        hou.ik.Target.setJointOffset."""
    def setJointOffset(self, offset: hou.Matrix4) -> None:
        """setJointOffset(xform)

        Sets a local space transform (a hou.Matrix4) that is combined with
        the joint transform to produce the transform that the solver
        attempts to align with the goal transform. This can be used to place
        the target at an offset from the joint (for example, at the end of a
        bone)."""
    def targetType(self) -> hou.EnumValue:
        """targetType() -> hou.ik.targetType

        Returns the target's type. See hou.ik.Target.setTargetType."""
    def setTargetType(self, target_type: hou.EnumValue) -> None:
        """setTargetType(target_type)

        Sets a hou.ik.targetType, which specifies whether the target affects
        position, orientation, or both."""
    def weight(self) -> float:
        """weight() -> float

        Returns the target's weight. See hou.ik.Target.setWeight."""
    def setWeight(self, weight: float) -> None:
        """setWeight(weight)

        Sets a float specifying the importance of the target. When multiple
        targets have the same priority level, targets with a higher relative
        weight are more likely to be reached."""
    def priority(self) -> int:
        """priority() -> int

        Returns the target's priority level. See hou.ik.Target.setPriority."""
    def setPriority(self, level: int) -> None:
        """setPriority(priority)

        Sets an int specifying the target's priority level. Targets from a
        lower priority level cannot interfere with targets from a higher
        priority level. For example, priority levels can be used to ensure
        that the feet remain planted when manipulating the upper body of a
        skeleton."""
    def depth(self) -> int:
        """depth() -> int

        Returns the target's depth. See hou.ik.Target.setDepth."""
    def setDepth(self, depth: int) -> None:
        """setDepth(depth)

        Specifies the number of parent joints that can be adjusted to
        achieve the goal transform. A negative depth indicates that the
        entire chain can be affected."""
