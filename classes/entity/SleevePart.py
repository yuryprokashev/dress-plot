from classes.interactor.SegmentFactory import SegmentFactory


class SleevePart(object):
    def __init__(self, part_config, dress_size):
        self.name = "sleeve"
        self.segments = []

        segment1_config = dict()
        segment1_config["type"] = "linear"
        segment1_config["relative_end_x"] = dress_size.half_chest - dress_size.half_neck
        segment1_config["relative_end_y"] = 0
        self.segments.append(SegmentFactory.create(segment1_config))

        segment2_config = dict()
        segment2_config["type"] = "linear"
        segment2_config["relative_end_x"] = 0
        segment2_config["relative_end_y"] = - dress_size.full_shoulder
        self.segments.append(SegmentFactory.create(segment2_config))

        segment3_config = dict()
        segment3_config["type"] = "linear"
        segment3_config["relative_end_x"] = - part_config["length"]
        segment3_config["relative_end_y"] = - part_config["length"]
        self.segments.append(SegmentFactory.create(segment3_config))
