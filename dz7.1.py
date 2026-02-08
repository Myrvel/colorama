class IterableObject:
    def __iter__(self):
        for i in range(1, 6):
            yield i

obj = IterableObject()
for value in obj:
    print(value)