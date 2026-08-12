class Nigiri:
  category = "にぎり"
  top = "ねた"
  base = "しゃり"

  def show_attributes(self):
    print("top: {}, base: {}, category: {}".format(self.top, self.base, self.category))

# ni = Nigiri()
# ni.show_attributes()

class Maguro(Nigiri):
  pass

m1 = Maguro()
m1.show_attributes()

