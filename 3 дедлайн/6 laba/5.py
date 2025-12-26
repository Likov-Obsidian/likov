class SmartList(list):
    def __getitem__(self, index):
        if isinstance(index, int) and index < 0:
            new_index = abs(index) - 1
            return super().__getitem__(new_index)
        return super().__getitem__(index)
sl = SmartList([10, 20, 30])
print(sl[0])
print(sl[-1])
print(sl[-2])