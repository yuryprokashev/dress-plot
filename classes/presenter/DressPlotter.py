from classes.interactor.PartPlotFactory import PartPlotFactory


class DressPlotter(object):
    def __init__(self, segment_plotter):
        self.segment_plotter = segment_plotter

    def plot(self, dress, start_point):
        for part_index, part in enumerate(dress.parts):
            part_plot = PartPlotFactory.create(part, start_point)
            for segment_plot_index, segment_plot in enumerate(part_plot.segment_plots):
                self.segment_plotter.plot(segment_plot)
            start_point = part_plot.end_point

    def show(self):
        self.segment_plotter.show()
