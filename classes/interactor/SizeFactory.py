from classes.entity.Size import Size
from classes.interactor.ExceptionFactory import ExceptionFactory


class SizeFactory(object):
    @staticmethod
    def create(size_name):
        if size_name == "XS":
            return Size(half_chest=47.6,
                        half_hip=48.0,
                        half_neck=18.1,
                        half_waist=34.0,
                        back_till_waist=38.8,
                        full_length=80.0,
                        full_shoulder=28.5)
        else:
            raise ExceptionFactory.create("Invalid Input", "size_name", size_name)
