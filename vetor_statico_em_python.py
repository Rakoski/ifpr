class StaticIntArray:
    def __init__(self, size: int, default_value: int = 0):
        self.array = [default_value] * size

    def __getitem__(self, index: int) -> int:
        return self.array[index]

    def __setitem__(self, index: int, value: int):
        self.array[index] = value

    def __len__(self) -> int:
        return len(self.array)


static_arr = StaticIntArray(5)
static_arr[2] = 42
print(static_arr[2])  # Output: 42
print(len(static_arr))  # Output: 5
# Eu esperava que desse pra fazer isso com tuplas, mas pelo jeito não é possível
