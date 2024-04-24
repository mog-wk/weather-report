
class InvalidParameter:
    def __init__(self, parameter):
        self.parameter = parameter
    @staticmethod
    def consume(p):
        print("Provided invalid parameter")
        exit(1)
