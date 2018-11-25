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
neck_config = dict()
neck_config["name"] = "neck"
neck_config["a_to_b_ratio"] = 3.0

sleeve_config = dict()
sleeve_config["name"] = "sleeve"
sleeve_config["length"] = 6.0

skirt_config = dict()
skirt_config["name"] = "skirt"
skirt_config["skirt_shift"] = 10.0

dress_config = [
    neck_config,
    sleeve_config,
    skirt_config
]

# This object contains the logic that builds the specific Dress segments
# It uses data in Size object for that
# This object represents the data of the specific dress, that we would like to plot then
dress = DressFactory.create("Simple Dress", size, dress_config)

# This call asks dress_plotter to plot the dress, that contains segments
start_point = PointFactory.create("2D", [0, 0])
dress_plotter.plot(dress, start_point)

# This call asks dress_plotter to show the results on the matplotlib figure
dress_plotter.show()


