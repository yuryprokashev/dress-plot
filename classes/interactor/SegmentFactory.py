from classes.entity.Point2D import Point2D
from classes.entity.Segment import Segment


class SegmentFactory(object):
    @staticmethod
    def create(segment_config):
        segment_type = segment_config["type"]
        relative_end = Point2D(segment_config["relative_end_x"], segment_config["relative_end_y"])
        return Segment(relative_end, segment_type)
