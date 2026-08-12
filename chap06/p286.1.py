class MyClass1:
  def __init__(self, text="abc"):
    self.text = text

a = MyClass1()
b = MyClass1(text="ggg")
c = MyClass1("uds")

print(a.text)
print(b.text)
print(c.text)

a.new_text = "another text"
print(a.new_text)
