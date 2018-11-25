from classes.entity.Point2D import Point2D
from classes.entity.SegmentPlot import SegmentPlot


class SegmentPlotFactory(object):
    @staticmethod
    def create(segment, start_point):
        start = start_point
        end = Point2D(start_point.x + segment.relative_end.x, start_point.y + segment.relative_end.y)
        segment_type = segment.type
        return SegmentPlot(start, end, segment_type)
