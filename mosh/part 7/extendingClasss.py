class Text(str):
    def duplicate(self):
        return self + self


text = Text('PYthon')

print(text.duplicate())
