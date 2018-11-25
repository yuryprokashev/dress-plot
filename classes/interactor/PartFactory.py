from classes.entity.NeckPart import NeckPart
from classes.entity.SkirtPart import SkirtPart
from classes.entity.SleevePart import SleevePart
from classes.interactor.ExceptionFactory import ExceptionFactory


class PartFactory(object):
    @staticmethod
    def create(part_config, dress_size):
        if part_config["name"] == "neck":
            return NeckPart(part_config, dress_size)
        elif part_config["name"] == "sleeve":
            return SleevePart(part_config, dress_size)
        elif part_config["name"] == "skirt":
            return SkirtPart(part_config, dress_size)
        else:
            raise ExceptionFactory.create("Invalid Input", "part_config['name']", part_config["name"])
