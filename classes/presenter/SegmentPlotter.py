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
        if segment_plot.type == "elliptic":
            # The order of the points for CURVE3 determines the convexity of the line
            # if you move from start.x < end.x (curve goes left), then you:
            # 1) move x left
            # 2) move y up
            # => you will get the convex curve, going up
            # if you instead do
            # 1) move x left
            # 2) move y down
            # => you will get the concave curve, going down
            # Now if you move from start.x > end.x (curve goes right), then you:
            # 1) move x right
            # 2) move y down
            # => you get concave curve going right
            # if instead you do:
            # 1) move y down
            # 2) move x right
            # => you get convex curve going right
            # TODO NOW THIS CODE WORKS ONLY FOR THE SIMPLE DRESS CASE!
            # TODO Make this part of the code support all possible variations of the curves
            if segment_plot.start.x < segment_plot.end.x:
                result.append((segment_plot.end.x, segment_plot.start.y))
                result.append((segment_plot.end.x, segment_plot.end.y))
            elif segment_plot.start.x > segment_plot.end.x:
                result.append((segment_plot.start.x, segment_plot.end.y))
                result.append((segment_plot.end.x, segment_plot.end.y))
        elif segment_plot.type == "linear":
            result.append((segment_plot.end.x, segment_plot.end.y))
        return result

    def get_path_codes(self, segment_plot):
        result = list()
        result.append(self.Path.MOVETO)
        if segment_plot.type == "elliptic":
            result.append(self.Path.CURVE3)
            result.append(self.Path.CURVE3)
        elif segment_plot.type == "linear":
            result.append(self.Path.LINETO)
        return result

    def show(self):
        self.ax.plot()
        self.plotlib.pyplot.show()