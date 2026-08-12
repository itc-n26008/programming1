class Programmer:
  def __init__(self):
    self.skill = "プログラミング"
    print('Programmer', self.skill)

  def make_code(self):
    print("コードを書く")

class Musician:
  def __init__(self):
    self.skill = "リズム・メロディ・ハーモニー"
    print('Musician', self.skill)

  def play_instrument(self):
    print("楽器を演奏する")

class MusicianProgrammer(Programmer, Musician):
  pass

mp1 = MusicianProgrammer()
mp1.make_code()
mp1.play_instrument()
