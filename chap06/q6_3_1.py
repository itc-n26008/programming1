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

class Katsuo(Nigiri):
    top="かつお"
    topping="生姜とネギ"
    price="100"

    def show_attributes(self):
        super().show_attributes()
        print("topping={}".format(self.topping))

k1=Katsuo()
k1.show_attributes
'''実行結果
top: ねた, base: しゃり, category: にぎり
'''
