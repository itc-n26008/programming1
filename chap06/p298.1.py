class Nigiri:
  category = "にぎり"
  top = "ねた"
  base = "しゃり"

  def show_attributes(self):
    print("top: {}, base: {}, category: {}".format(self.top, self.base, self.category))

class Maguro(Nigiri):
  top = "まぐろ"
  price = 100

  def show_attributes(self):
    super().show_attributes()
    print("price: {}円".format(self.price))

m5 = Maguro()
m5.show_attributes()
