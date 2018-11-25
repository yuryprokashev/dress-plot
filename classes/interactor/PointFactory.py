from classes.entity.Point2D import Point2D
from classes.interactor.ExceptionFactory import ExceptionFactory


class PointFactory(object):
    @staticmethod
    def create(point_dim, point_coordinates):
        if point_dim == "2D":
            x = point_coordinates[0]
            y = point_coordinates[1]
            return Point2D(x, y)
        else:
            raise ExceptionFactory.create("Invalid Input", "point_dim", point_dim)
