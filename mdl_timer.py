class Timer:
    @staticmethod
    def Start(updateFunc):
        i = 1000000
        while i >= 0:
            updateFunc(str(i))
            i -= 1
