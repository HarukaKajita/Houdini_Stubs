# pyright: reportMissingModuleSource=false
from __future__ import annotations

import enum
from typing import *

if TYPE_CHECKING:
    # fix some namespace issues for submodules
    import hou
    import hou.hmath

def __init__(*args: Any, **kwargs: Any): ...
def identityTransform() -> hou.Matrix4:
    """identityTransform() -> hou.Matrix4

      Returns the identity matrix. This is the same as hou.Matrix4(1) but
      may make your code more understandable.

    > >>> hou.hmath.identityTransform()
    > <hou.Matrix4 [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]>

      See hou.Matrix4."""

def buildTranslate(*args: Any) -> hou.Matrix4:
    """buildTranslate(tx, ty, tz) -> hou.Matrix4

      Returns a transformation matrix containing only a translation. You
      can build more complex transformations by multiplying this with
      another transform matrix.

      You can supply three float values for x, y, and z, or a sequence of
      three floats, or a hou.Vector3.

    > forward_z = hou.hmath.buildTranslate(0, 0, 1)
    > forward_x = hou.hmath.buildTranslate(hou.Vector3(1, 0, 0))"""

def buildScale(*args: Any) -> hou.Matrix4:
    """buildScale(sx, sy, sz) -> hou.Matrix4

      Returns a transformation matrix containing only a scale. You can
      build more complex transformations by multiplying this with another
      transform matrix.

      You can supply three float values for x, y, and z, or a sequence of
      three floats, or a hou.Vector3. To apply a uniform scale, use the
      same value for x, y, and z.

    > stretch = hou.hmath.buildScale(2, 1, 1)
    > uniform = hou.hmath.buildScale(hou.Vector3(2, 2, 2))

      See hou.Geometry.createNURBSSurface for an example."""

def buildShear(*args: Any) -> hou.Matrix4:
    """buildShear(shearx, sheary, shearz) -> hou.Matrix4

    Returns a transformation matrix containing only a shear. You can
    build more complex transformations by multiplying this with another
    transform matrix.

    You can supply three float values for x, y, and z, or a sequence of
    three floats, or a hou.Vector3.

    See Wikipedia's shear matrix page for more information."""

def buildRotate(*args: Any) -> hou.Matrix4:
    """buildRotate(rx, ry, rz, order=\"xyz\") -> hou.Matrix4

      Returns a transformation matrix containing only a rotation, given
      Euler angles in degrees. You can build more complex transformations
      by multiplying this with another transform matrix.

      You can supply three float values for x, y, and z, or a sequence of
      three floats, or a hou.Vector3.

    > xform1 = hou.hmath.buildRotate(45, 45, 0)
    > xform2 = hou.hmath.buildRotate(hou.Vector3(90, 0, 90))

      order
          A string containing a permutation of the letters x, y, and z
          that controls the order of rotations.

      See Wikipedia's Euler angles page for more information."""

def buildRotateAboutAxis(axis: tuple[float], angle_in_deg: float) -> hou.Matrix4:
    """buildRotateAboutAxis(axis, angle_in_deg) -> hou.Matrix4

      Returns a transformation matrix containing only a rotation computed
      from an axis and a rotation amount. You can build more complex
      transformations by multiplying this with another transform matrix.


      axis
          A hou.Vector3 normal defining an axis to rotate around. For
          example, hou.Vector3(0, 1, 1) would rotate around a diagonal
          pointed along positive Y and Z.

      angle_in_deg
          Number of degrees of rotation around the axis to store in the
          matrix.

    > turn_45_around_yz = hou.hmath.buildRotateAboutAxis(hou.Vector3(0, 1, 1), 45)

      If you want to convert Euler angles into a corresponding axis and
      angle, you can use the following code:

    > def extractAxisAndAngleFromRotateMatrix(m):
    >     '''
    >     Given a matrix, return an (Vector3, float) tuple containing the
    >     axis and angle.  See Wikipedia's rotation representation page for
    >     more details.
    >     '''
    >
    >     import math
    >
    >     acos_input = (m.at(0, 0) + m.at(1, 1) + m.at(2, 2) - 1.0) * 0.5
    >     if acos_input < -1.0 or acos_input > 1.0:
    >         return None
    >
    >     angle = math.acos(acos_input)
    >     if angle >= -1e-6 and angle <= 1e-6:
    >         # There is no rotation.  Choose an arbitrary axis and a rotation of 0.
    >         return hou.Vector3(1, 0, 0), 0.0
    >
    >     inv_sin = 1.0 / (2.0 * math.sin(angle))
    >     axis = hou.Vector3(
    >         (m.at(1, 2) - m.at(2, 1)) * inv_sin,
    >         (m.at(2, 0) - m.at(0, 2)) * inv_sin,
    >         (m.at(0, 1) - m.at(1, 0)) * inv_sin)
    >     return axis, hou.hmath.radToDeg(angle)
    >
    > def eulerToAxisAndAngle(angles):
    >     return extractAxisAndAngleFromRotateMatrix(hou.hmath.buildRotate(angles))

      See Wikipedia's axis angle page and rotation representation page for
      more information."""

def buildRotateZToAxis(axis: tuple[float]) -> hou.Matrix4:
    """buildRotateZToAxis(axis) -> hou.Matrix4

      Returns a transformation matrix rotating the z-axis onto the given
      axis. You can build more complex transformations by multiplying this
      with another transform matrix.


      axis
          A hou.Vector3 defining an axis to rotate the z-axis to.

    > rotate_z_to_x = hou.hmath.buildRotateZToAxis(hou.Vector3(1, 0, 0))

      The rotation picked is the shortest rotation. If the goal vector is
      pointed the opposite direction of the z-axis, an arbitrary but
      consistent rotation that maps to the negative z-axis will be picked."""

def buildRotateLookAt(_from: hou.Vector3, to: hou.Vector3, up: hou.Vector3) -> hou.Matrix4:
    """buildRotateLookAt(__from, to, up) -> hou.Matrix4

      Returns a rotation matrix to orient negative z-axis point along the
      vector (_from-to). up is an up vector that defines the roll and
      orienting the positive y-axis.


      _from
          A hou.Vector3 defining the origin position of the lookat.

      to
          A hou.Vector3 defining the target position of the lookat.

      up
          A hou.Vector3 defining the up vector.

    > p0 = hou.Vector3(1, 2, 3)
    > p1 = hou.Vector3(1, 1, 0)
    > up = hou.Vector3(0, 1, 0)
    > lookat_m = hou.hmath.buildRotateLookAt(p0, p1, up)
    >
    > # You can change which axis is the target by using another lookat
    > # and multiplying by the inverse matrix.
    > lookaxis = hou.Vector3(1, 0, 0)
    > upaxis = hou.Vector3(0, 0, 1)
    > fix_m = hou.hmath.buildRotateLookAt(hou.Vector3(0,0,0), lookaxis, upaxis)
    > lookat_m1 = fix_m.inverted() * lookat_m"""

def buildTransform(*args: Any, **kwargs: Any) -> hou.Matrix4:
    """buildTransform(values_dict, transform_order=\"srt\", rotate_order=\"xyz\")
    -> hou.Matrix4

        Takes a dictionary containing mapping strings to vectors (such as
        produced by hou.Matrix4.explode), and returns a hou.Matrix4
        transformation. You can use this to explode a matrix, modify one or
        a few components, and then recompose into a matrix, or to generate a
        matrix from scratch from a few components.

        The dictionary can contain any of the following keys: translate,
        rotate, scale, shear, pivot, pivot_rotate. The values can be
        hou.Vector3 objects or 3-tuples of floats.


        transform_order
            A string containing a permutation of the letters s, r, and t.
            The rotate, scale, and translate results are dependent on the
            order in which you perform those operations, and this string
            specifies that order.

        rotate_order
            A string containing a permutation of the letters x, y, and z
            that determines the order in which rotations are performed about
            the coordinate axes. This does not apply to the pivot_rotate

            angles, which are always applied in \"xyz\" order.

        This function could be re-implemented like this:

      > def buildTransform(values_dict, transform_order=\"srt\", rotate_order=\"xyz\"):
      >     # Take the return value from explode, along with the transform and
      >     # rotate order, and rebuild the original matrix.
      >     result = hou.hmath.identityTransform()
      >     for operation_type in transform_order:
      >         if operation_type == \"t\":
      >             result *= hou.hmath.buildTranslate(values_dict[\"translate\"])
      >         elif operation_type == \"s\":
      >             result *= hou.hmath.buildScale(values_dict[\"scale\"])
      >             if \"shear\" in values_dict:
      >                 result *= hou.hmath.buildShear(values_dict[\"shear\"])
      >         elif operation_type == \"r\":
      >             result *= hou.hmath.buildRotate(values_dict[\"rotate\"], rotate_order)
      >         else:
      >             raise ValueError(\"Invalid transform order\")
      >     return result"""

def _buildTransformTRS(*args: Any) -> hou.Matrix4: ...
def _buildTransformTRSS(*args: Any) -> hou.Matrix4: ...
def _buildTransformTR(*args: Any) -> hou.Matrix4: ...
def _buildTransform(*args: Any) -> hou.Matrix4: ...
def degToRad(degrees: float) -> float:
    """degToRad(degrees) -> float

    Given a value in degrees, return the corresponding value in radians.

    This function is equivalent to degrees * math.pi / 180.0."""

def radToDeg(radians: float) -> float:
    """radToDeg(radians) -> double

    Given a value in radians, return the corresponding value in degrees.

    This function is equivalent to radians * 180.0 / math.pi."""

def noise1d(pos: tuple[float]) -> float:
    """noise1d(self, pos) -> float

    Given a sequence of 1 to 4 floats representing a position in
    N-dimensional space, return a single float corresponding to 1
    dimensional noise.

    This function matches the output of the noise() function from VEX."""

def noise3d(pos: tuple[float]) -> hou.Vector3:
    """noise3d(self, pos) -> hou.Vector3

    Given a sequence of 1 to 4 floats representing a position in
    N-dimensional space, return a hou.Vector3 object representing the
    vector noise at the given position.

    This function matches the output of the noise() function from VEX."""

def fit(value: float, oldmin: float, oldmax: float, newmin: float, newmax: float) -> float:
    """fit(value, old_min, old_max, new_min, new_max) -> float

      Returns a number between new_min and new_max that is relative to the
      value between the range old_min and old_max. If the value is outside
      the old_min to old_max range, it will be clamped to the new range.

    > >>> hou.hmath.fit(3, 1, 4, 5, 20)
    > 15.0"""

def fit01(value: float, newmin: float, newmax: float) -> float:
    """fit01(value, new_min, new_max) -> float

    Returns a number between new_min and new_max that is relative to the
    value between the range 0 and 1. If the value is outside the 0 to 1
    range, it will be clamped to the new range.

    This function is a shortcut for hou.hmath.fit(value, 0.0, 1.0,
    new_min, new_max)."""

def fit10(value: float, newmin: float, newmax: float) -> float:
    """fit10(value, new_min, new_max) -> float

    Returns a number between new_min and new_max that is relative to the
    value between the range 1 to 0. If the value is outside the 1 to 0
    range, it will be clamped to the new range.

    This function is a shortcut for hou.hmath.fit(value, 1.0, 0.0,
    new_min, new_max)."""

def fit11(value: float, newmin: float, newmax: float) -> float:
    """fit11(value, new_min, new_max) -> float

    Returns a number between new_min and new_max that is relative to the
    value between the range -1 to 1. If the value is outside the -1 to 1
    range, it will be clamped to the new range.

    This function is a shortcut for hou.hmath.fit(value, -1.0, 1.0,
    new_min, new_max)."""

def sign(value: float) -> float:
    """sign(value) -> int

    Returns 1.0 if value is positive, -1.0 if negative and 0.0 if value
    is zero.

    Note that you can achieve the same effect with Python's built-in cmp
    function: float(cmp(value, 0))."""

def clamp(value: float, min: float, max: float) -> float:
    """clamp(value, min, max) -> float

    Returns the value clamped to the range min to max. See also
    hou.hmath.wrap. This function is useful in expressions to prevent a
    value from going outside the specified range."""

def smooth(value: float, min: float, max: float) -> float:
    """smooth(value, min, max) -> float

      Takes a value and range and returns a smooth interpolation between 0
      and 1.

      When value is less than min, the return value is 0. If value is
      greater than max, the return value is 1.

    > >>> hou.hmath.smooth(5, 0, 20)
    > 0.15625
    > >>> hou.hmath.smooth(10, 0, 20)
    > 0.5
    > >>> hou.hmath.smooth(15, 0, 20)
    > 0.84375
    > # Visualize the output of this function by positioning geometry objects at  various locations.
    > def createSpheres(num_spheres=40):
    >     for i in range(num_spheres):
    >         sphere = hou.node(\"/obj\").createNode(\"geo\").createNode(\"sphere\")
    >         sphere.parmTuple(\"rad\").set((0.1, 0.1, 0.1))
    >         sphere.setDisplayFlag(True)
    >
    >         # Given a value between 0 and 5, we'll call smooth with a range
    >         # of 0 to 3, and the resulting y value will be between 0 and 1.
    >         x = 5.0 * i / num_spheres
    >         y = hou.hmath.smooth(x, 0, 3)
    >         sphere.parent().setParmTransform(hou.hmath.buildTranslate((x, y, 0)))"""

def wrap(value: float, min: float, max: float) -> float:
    """wrap(value, min, max)

    Similar to the hou.hmath.clamp function in that the resulting value
    will always fall between the specified minimum and maximum value.
    However, it will create a saw-tooth wave for continuously increasing
    or decreasing parameter values."""

def rand(seed: float) -> float:
    """rand(seed) -> float

    Returns a pseudo-random number from 0 to 1. Using the same seed will
    always give the same result."""

def orient2d(pa: tuple[float], pb: tuple[float], point: tuple[float]) -> float:
    """orient2d(pa, pb, point) -> float

    Performs an adaptive exact sidedness test of the 2d point against
    the line defined by pa and pb.

    See http://www.cs.cmu.edu/~quake/robust.html for details of the
    implementation."""

def orient3d(pa: tuple[float], pb: tuple[float], pc: tuple[float], point: tuple[float]) -> float:
    """orient3d(pa, pb, pc, point) -> float

    Performs an adaptive exact sidedness test of the 3d point against
    the plane defined by pa, pb, and pc.

    See http://www.cs.cmu.edu/~quake/robust.html for details of the
    implementation."""

def inCircle(pa: tuple[float], pb: tuple[float], pc: tuple[float], point: tuple[float]) -> float:
    """inCircle(pa, pb, pc, point) -> float

    Performs an adaptive exact inside test of the 2d point against the
    circle defined by pa, pb, and pc. pa, pb, and pc must be in counter-
    clockwise order to get a positive value for interior points.

    See http://www.cs.cmu.edu/~quake/robust.html for details of the
    implementation."""

def inSphere(pa: tuple[float], pb: tuple[float], pc: tuple[float], pd: tuple[float], point: tuple[float]) -> float:
    """inSphere(pa, pb, pc, pd, point) -> float

    Performs an adaptive exact inside test of the 3d point against the
    sphere defined by pa, pb, pc, and pd. Note that inconsistent
    orientation of the four sphere defining points will reverse the sign
    of the result.

    See http://www.cs.cmu.edu/~quake/robust.html for details of the
    implementation."""

def intersectPlane(
    plane_point: hou.Vector3, plane_dir: hou.Vector3, line_origin: hou.Vector3, line_dir: hou.Vector3
) -> hou.Vector3:
    """intersectPlane(plane_point, plane_normal, line_origin, line_dir) ->
    hou.Vector3

        Takes a plane defined by an origin point and normal vector
        (plane_point and plane_normal) and a line defined by an origin and
        direction (line_origin and line_dir) and returns a hou.Vector3 value
        representing the XYZ coordinates of the intersection point between
        the line and plane. All arguments must be hou.Vector3.

      > hou.hmath.intersectPlane(
      >     hou.Vector3(0, 0, 0), hou.Vector3(0, 1, 0),
      >     hou.Vector3(0.212, 1.56, 0), hou.Vector3(0, 0.62, -0.34)
      > )  # -> hou.Vector3(0.212, -1.19209e-07, 0.855484)

        (Note that line runs forward and backward along the line_dir from
        the origin. That is, even if line_dir points away from the plane,
        you will get the intersection behind the origin.)

      > hou.hmath.intersectPlane(
      >     hou.Vector3(0, 0, 0), hou.Vector3(0, 1, 0),  # Ground plane
      >     hou.Vector3(0, 1, 0), hou.Vector3(0, 1, 0)  # Line up from 1u above ground
      > )  # -> hou.Vector3(0, 0, 0)

        This function raises an exception if the line is parallel to the
        plane, or if the line_dir has no length, or even if the line is not
        mathematically parallel but parallel enough that the answer would be
        outside roughly a -100000, -100000 to 100000, 100000 square."""

def combineLocalTransform(*args: Any, **kwargs: Any) -> hou.Matrix4:
    """combineLocalTransform(local, world, parent_local=None,
    mode=hou.scaleInheritanceMode.Default) -> hou.Matrix4

        Returns a new world transform given its local and parent world
        transforms."""

def extractLocalTransform(*args: Any, **kwargs: Any) -> hou.Matrix4:
    """extractLocalTransform(world, parent_world, parent_local,
    mode=hou.scaleInheritanceMode.Default, effective_local=None) ->
    hou.Matrix4

        Returns a new local transform given its world and new parent
        transforms. If effective_local is given, then it is a hou.Matrix4
        modified to be the effective local transform taking into account
        mode."""

def slerpTransforms(
    xforms: list[hou.Matrix4],
    input_weights: tuple[float],
    normalize_weigths: bool = True,
    slerp_method: int = 1,
    slerp_flip_mehtod: int = 1,
) -> hou.Matrix4:
    """slerpTransforms( xforms, input_weights, normalize_weights, slerp_method,
    slerp_flip_method) -> hou.Matrix4

        Spherically blend transforms by decomposing into separate
        quaternions. xforms is the array of hou.Matrix4 transforms to blend.
        input_weights is an array of floats with the same size as the
        xforms. Set normalize_weights to True to normalize the input
        weights. slerp_method can be 0 to blend using normalized linear
        interpolation of quaternions or 1 to use an iterative method.
        slerp_flip_method defines a flip methid for slerp to ensure
        consistency during blending. It can be 0 to use the hemisphere of
        the first quaternion, or 1 to compare each adjacent quaternions when
        using NLERP."""
