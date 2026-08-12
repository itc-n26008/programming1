class Reverse:
    '''シーケンスを逆順にループするイテレータ'''

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# シーケンスの一例として文字列を渡す
rev = Reverse("spam")
for char in rev:
    print(char, end=" ")
