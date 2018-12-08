from classes.entity.CurveDirection import CurveDirection


class CurveDirectionFactory(object):
    @staticmethod
    def create(segment_plot):
        if (segment_plot.start.x < segment_plot.end.x) & (segment_plot.start.y < segment_plot.end.y):
            return CurveDirection.UP_RIGHT
        elif (segment_plot.start.x < segment_plot.end.x) & (segment_plot.start.y > segment_plot.end.y):
            return CurveDirection.DOWN_RIGHT
        elif (segment_plot.start.x > segment_plot.end.x) & (segment_plot.start.y > segment_plot.end.y):
            return CurveDirection.DOWN_LEFT
        elif (segment_plot.start.x > segment_plot.end.x) & (segment_plot.start.y < segment_plot.end.y):
            return CurveDirection.UP_LEFT
