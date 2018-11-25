from classes.entity.SimpleDress import SimpleDress
from classes.interactor.ExceptionFactory import ExceptionFactory


class DressFactory(object):
    @staticmethod
    def create(dress_model, size, dress_config):
        if dress_model == "Simple Dress":
            return SimpleDress(size, dress_config)
        else:
            raise ExceptionFactory.create("Invalid Input", "dress_model", dress_model)
