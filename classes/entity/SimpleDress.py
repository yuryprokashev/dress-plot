from classes.interactor.PartFactory import PartFactory


class SimpleDress(object):
    def __init__(self, size, config):
        self.parts = []
        # We first create parts separately, they do not have any x, y points
        for index, part_config in enumerate(config):
            self.parts.append(PartFactory.create(part_config, size))
