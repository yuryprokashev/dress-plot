from classes.entity.PartPlot import PartPlot
from classes.entity.Point2D import Point2D
from classes.interactor.SegmentPlotFactory import SegmentPlotFactory


class PartPlotFactory(object):
    @staticmethod
    def create(part, start_point):
        segment_plots = []
        end_point = Point2D(0, 0)
        for segment_index, segment in enumerate(part.segments):
            segment_plot = SegmentPlotFactory.create(segment, start_point)
            segment_plots.append(segment_plot)
            end_point = segment_plot.end
            start_point = segment_plot.end

        return PartPlot(start_point, end_point, segment_plots)
