class ExceptionFactory(object):
    @staticmethod
    def create(exception_type, parameter_key, parameter_value):
        if exception_type == "Invalid Input":
            return Exception("The provided {} = {} is not supported.".format(parameter_key, parameter_value))
