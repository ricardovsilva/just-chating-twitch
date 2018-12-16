import re

class ChronalCalibrator:
    def calibrate(self, input):
        if not input:
            raise Exception('input cannot be null')
        if not self.__has_numbers_only(input):
            raise Exception("input should contains only valid numbers, for example '+7, -2, +3'")

        return sum([int(number) for number in input.split(",")])

    #BAAAAAAAAAD SMEEEEEEEEEEEEEEEELLL
    def __has_numbers_only(self, input):
        pattern = "(\+|-)\d+,?"
        return re.match(pattern, input)
        

        