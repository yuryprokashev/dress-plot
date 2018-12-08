from classes.entity.FullDressPart import FullDressPart
from classes.interactor.ExceptionFactory import ExceptionFactory


class PartFactory(object):
    @staticmethod
    def create(part_config, dress_size):
        if part_config["name"] == "full":
            return FullDressPart(part_config, dress_size)
        else:
            raise ExceptionFactory.create("Invalid Input", "part_config['name']", part_config["name"])
