import matplotlib.pyplot

from classes.interactor.DressFactory import DressFactory
from classes.interactor.PointFactory import PointFactory
from classes.interactor.SizeFactory import SizeFactory

from classes.presenter.DressPlotter import DressPlotter
from classes.presenter.SegmentPlotter import SegmentPlotter

# This object is responsible for plotting one segment on the figure
# It uses matplotlib library and it's figure object to plot
segment_plotter = SegmentPlotter(matplotlib)

# This object is responsible to plot the full dress
# Dress is collection of segments
# This object uses segment_plotter object to plot
# It does not access matplotlib figure directly
dress_plotter = DressPlotter(segment_plotter)

# This object contains data about size
# Size does not know about the Dress
# So the same size object can be used by other class, like Coat, if in future you'd like to plot Coat
size = SizeFactory.create("XS")

# This array describes the configuration of the dress
# Dress consists of these parts.
# Each part consists of 1..N segments
full_config = dict()
full_config["name"] = "full"
full_config["sleeve_ledge"] = 6.0
full_config["chest_increase"] = 8.0
full_config["shoulder_increase"] = 7.0
full_config["neck_increase"] = 1.0
full_config["skirt_bottom_increase"] = 12.0
full_config["skirt_rise"] = 1.5

dress_config = [
    full_config
]

# This object contains the logic that builds the specific Dress segments
# It uses data in Size object for that
# This object represents the data of the specific dress, that we would like to plot then
dress = DressFactory.create("Simple Dress", size, dress_config)

# This call creates the 2D Point, that will be used as starting point of the plot
start_point = PointFactory.create("2D", [0, 0])

# This call asks dress_plotter to plot the dress from start_point
dress_plotter.plot(dress, start_point)

# This call asks dress_plotter to show the results on the matplotlib figure
dress_plotter.show()


