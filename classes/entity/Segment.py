class Segment(object):
    def __init__(self, relative_end, segment_type):
        self.relative_end = relative_end
        self.type = segment_type

    def __str__(self):
        return "type: {}, x: {}, y: {}".format(self.type, self.relative_end.x, self.relative_end.y)
