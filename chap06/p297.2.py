class Nigiri:
  category = "にぎり"
  top = "ねた"
  base = "しゃり"

  def show_attributes(self):
    print("top: {}, base: {}, category: {}".format(self.top, self.base, self.category))

class Maguro(Nigiri):
  top = "まぐろ"
  price = 100

m3 = Maguro()
m3.show_attributes()
