from classes.entity.Point2D import Point2D
from classes.entity.Segment import Segment


class SegmentFactory(object):
    @staticmethod
    def create(segment_type, relative_end_x, relative_end_y):
        relative_end = Point2D(relative_end_x, relative_end_y)
        return Segment(relative_end, segment_type)
