class Person:
    def __init__(self,
                name = '',
                nationality = '',
                birth = '',
                address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:",self.name)
        print("国籍:", self.nationality)
        print("生まれたとし:",self.birth)
        print("住んでいるところ:", self.address)

heroine = Person('かぐや姫','日本','685','静岡県富士市')
print(heroine.show_attributes())
"""実行結果
名前: かぐや姫
国籍: 日本
生まれたとし: 685
住んでいるところ: 静岡県富士市
None
"""
