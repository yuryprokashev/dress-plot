from classes.interactor.SegmentFactory import SegmentFactory


class SkirtPart(object):
    def __init__(self, part_config, dress_size):
        self.segments = []
        self.name = "skirt"

        segment1_config = dict()
        segment1_config["type"] = "linear"
        # TODO It is not exactly skirt_shift. Need adjustment on H2-H3 y
        segment1_config["relative_end_x"] = part_config["skirt_shift"]
        # TODO It does not account for G1-G3 length
        segment1_config["relative_end_y"] = -(dress_size.full_length - dress_size.full_shoulder - 6)
        self.segments.append(SegmentFactory.create(segment1_config))

        segment2_config = dict()
        segment2_config["type"] = "elliptic"
        segment2_config["relative_end_x"] = - (dress_size.half_waist + part_config["skirt_shift"])
        segment2_config["relative_end_y"] = - 10
        self.segments.append(SegmentFactory.create(segment2_config))

        segment3_config = dict()
        segment3_config["type"] = "linear"
        segment3_config["relative_end_x"] = - (dress_size.half_chest - part_config["skirt_shift"])
        segment3_config["relative_end_y"] = 0
        self.segments.append(SegmentFactory.create(segment3_config))
