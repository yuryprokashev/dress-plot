from classes.entity.SegmentType import SegmentType
from classes.entity.CurveDirection import CurveDirection
from classes.interactor.CurveDirectionFactory import CurveDirectionFactory


class SegmentPlotter(object):
    def __init__(self, plotlib):
        self.plotlib = plotlib
        fig, ax = self.plotlib.pyplot.subplots()
        self.plotlib.pyplot.gca().set_aspect("equal", adjustable="box")
        self.fig = fig
        self.ax = ax
        self.Path = self.plotlib.path.Path

    def plot(self, segment_plot):
        path_points = self.get_path_points(segment_plot)
        path_codes = self.get_path_codes(segment_plot)

        path = self.Path(path_points, path_codes)

        patch = self.plotlib.patches.PathPatch(path, fc="none", transform= self.ax.transData)
        self.ax.add_patch(patch)

    def get_path_points(self, segment_plot):
        result = list()
        result.append((segment_plot.start.x, segment_plot.start.y))
        curve_direction = CurveDirectionFactory.create(segment_plot)
        if segment_plot.type == SegmentType.ELLIPTIC_CONVEX:
            if curve_direction == CurveDirection.UP_RIGHT or curve_direction == CurveDirection.UP_LEFT:
                result.append((segment_plot.end.x, segment_plot.start.y))
            elif curve_direction == CurveDirection.DOWN_RIGHT or CurveDirection.DOWN_LEFT:
                result.append((segment_plot.start.x, segment_plot.end.y))
            result.append((segment_plot.end.x, segment_plot.end.y))
        elif segment_plot.type == SegmentType.ELLIPTIC_CONCAVE:
            if curve_direction == CurveDirection.UP_RIGHT or curve_direction == CurveDirection.UP_LEFT:
                result.append((segment_plot.start.x, segment_plot.end.y))
            elif curve_direction == CurveDirection.DOWN_RIGHT or CurveDirection.DOWN_LEFT:
                result.append((segment_plot.end.x, segment_plot.start.y))
            result.append((segment_plot.end.x, segment_plot.end.y))
        elif segment_plot.type == SegmentType.LINEAR:
            result.append((segment_plot.end.x, segment_plot.end.y))
        return result

    def get_path_codes(self, segment_plot):
        result = list()
        result.append(self.Path.MOVETO)
        if segment_plot.type == SegmentType.ELLIPTIC_CONCAVE or segment_plot.type == SegmentType.ELLIPTIC_CONVEX:
            result.append(self.Path.CURVE3)
            result.append(self.Path.CURVE3)
        elif segment_plot.type == SegmentType.LINEAR:
            result.append(self.Path.LINETO)
        return result

    def show(self):
        self.ax.plot()
        self.plotlib.pyplot.show()
