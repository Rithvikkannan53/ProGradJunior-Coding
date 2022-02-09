class JustCount:
    __secretcount = 0
    def count(self):
        self.__secretcount += 1
        print(self.__secretcount)

counter = JustCount()
counter.count()
counter.count()
print(counter._JustCount__secretcount)
