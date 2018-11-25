from classes.interactor.SegmentFactory import SegmentFactory


class NeckPart(object):
    def __init__(self, part_config, dress_size):
        self.name = "neck"
        self.segments = []

        segment1_config = dict()
        segment1_config["type"] = "linear"
        segment1_config["relative_end_x"] = 0
        segment1_config["relative_end_y"] = dress_size.full_length - dress_size.half_neck/part_config["a_to_b_ratio"]
        self.segments.append(SegmentFactory.create(segment1_config))

        segment2_config = dict()
        segment2_config["type"] = "elliptic"
        segment2_config["relative_end_x"] = dress_size.half_neck
        segment2_config["relative_end_y"] = dress_size.half_neck / part_config["a_to_b_ratio"]
        self.segments.append(SegmentFactory.create(segment2_config))
