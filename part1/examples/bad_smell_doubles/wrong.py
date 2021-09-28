class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted(self):
        self.lst.sort()
        return self.lst

    def sorting(self):
        return sorted(self.lst)

    def asc_sorting(self):
        return sorted(self.lst, reverse=False)
