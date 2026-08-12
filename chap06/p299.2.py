class Nigiri:
  category = "にぎり"
  top = "ねた"
  base = "しゃり"

  def show_attributes(self):
    print("top: {}, base: {}, category: {}".format(self.top, self.base, self.category))

class NigiriNew(Nigiri):

  def __init__(self, wasabi="わさび抜き"):
    self.wasabi = wasabi

  def show_attributes(self):
    super().show_attributes()
    print("wasabi: {}".format(self.wasabi))

class Maguro(NigiriNew):
  top = "まぐろ"
  price = 100

  def show_attributes(self):
    super().show_attributes()
    print("price: {}円".format(self.price))

m6 = Maguro("わさび入り")
m6.show_attributes()
