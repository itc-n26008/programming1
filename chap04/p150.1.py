def house_for_rent(bedrooms = 2, walk_min = 6, house_type = 'アパート', rent_yen = 50):
    return house_for_rent
    #return {'bedrooms': bedrooms, 'walk_min': walk_min,
            #'house_type': house_type, 'rent_yen': rent_yen}
    #↑　関数を外でも使うようにするために使うそうです
    
# print(house_for_rent(2, 15, 'アパート', 50))
# print(house_for_rent(bedrooms = 2, house_type = 'マンション', walk_min = 2, rent_yen = 100))
# print(house_for_rent(walk_min = 15))
# print(house_for_rent(5, house_type='マンション'))
print(house_for_rent(house_type='マンション', bedrooms = 5))
#↑　こいつで指定したとこだけかわって、上のやつが表示される
"""
{'bedrooms': 5, 'walk_min': 6, 'house_type': 'マンション', 'rent_yen': 50}

"""
