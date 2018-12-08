from classes.interactor.SegmentFactory import SegmentFactory
from classes.entity.SegmentType import SegmentType
import numpy as np


class FullDressPart(object):
    def __init__(self, part_config, dress_size):
        self.segments = []

        h1b1 = dress_size.full_length
        hh1 = (dress_size.half_chest + part_config["chest_increase"]) / 2
        bb2 = (dress_size.half_neck / 3.0) + 1.0
        bb3 = bb2 / 3.0
        bb4 = bb2 + 1.0
        b1g = (dress_size.full_shoulder / 2.0) + part_config["shoulder_increase"]
        b1b5 = part_config["sleeve_ledge"]
        h1h2 = part_config["skirt_bottom_increase"]
        hh2 = hh1 + h1h2
        g2h1 = dress_size.full_length - b1g - b1b5
        g2h2 = np.sqrt(g2h1 ** 2 + h1h2 ** 2)
        g2h3 = g2h2 - part_config["skirt_rise"]
        k = g2h3 / g2h2
        b2b1 = hh1 - bb2
        b2b5 = b1b5 + b2b1

        segment1_rel_end_x = bb2
        segment1_rel_end_y = bb4

        segment2_rel_end_x = - bb2
        segment2_rel_end_y = - bb3

        segment3_rel_end_x = 0
        segment3_rel_end_y = - h1b1 + bb3

        segment4_rel_end_x = hh2 / 2.0
        segment4_rel_end_y = 0

        segment5_rel_end_x = hh2 / 2.0
        segment5_rel_end_y = g2h1 * (1 - k)

        segment6_rel_end_x = - k * h1h2
        segment6_rel_end_y = k * g2h1

        segment7_rel_end_x = b1b5
        segment7_rel_end_y = b1b5

        segment8_rel_end_x = 0
        segment8_rel_end_y = b1g

        segment9_rel_end_x = - b2b5
        segment9_rel_end_y = 0

        self.segments.append(SegmentFactory.create(SegmentType.ELLIPTIC_CONVEX, segment1_rel_end_x, segment1_rel_end_y))
        self.segments.append(SegmentFactory.create(SegmentType.ELLIPTIC_CONVEX, segment2_rel_end_x, segment2_rel_end_y))
        self.segments.append(SegmentFactory.create(SegmentType.LINEAR, segment3_rel_end_x, segment3_rel_end_y))
        self.segments.append(SegmentFactory.create(SegmentType.LINEAR, segment4_rel_end_x, segment4_rel_end_y))
        self.segments.append(SegmentFactory.create(SegmentType.ELLIPTIC_CONVEX, segment5_rel_end_x, segment5_rel_end_y))
        self.segments.append(SegmentFactory.create(SegmentType.LINEAR, segment6_rel_end_x, segment6_rel_end_y))
        self.segments.append(SegmentFactory.create(SegmentType.ELLIPTIC_CONCAVE, segment7_rel_end_x, segment7_rel_end_y))
        self.segments.append(SegmentFactory.create(SegmentType.LINEAR, segment8_rel_end_x, segment8_rel_end_y))
        self.segments.append(SegmentFactory.create(SegmentType.LINEAR, segment9_rel_end_x, segment9_rel_end_y))
