from enum import Enum


class SegmentType(Enum):
    LINEAR = "linear"
    ELLIPTIC_CONVEX = "elliptic_convex"
    ELLIPTIC_CONCAVE = "elliptic_concave"
