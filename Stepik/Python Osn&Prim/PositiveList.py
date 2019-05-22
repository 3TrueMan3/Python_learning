class NonPositiveError(BaseException):
    Exception('NonPositiveError')


class PositiveList(list):
    def append(self, x):
        if x >= 0:
            self.extend([x])
        else:
            raise NonPositiveError
