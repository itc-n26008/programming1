class Car:
    wheight = 4000
    mum_wheels = 4

    def calc_weight_per_wheel(self):
        return 1000.0

my_car = Car()
print(my_car.calc_weight_per_wheel())
'''実行結果
1000.0
'''
