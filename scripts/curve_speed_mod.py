import math

def curve_speed_limit(wagon_count_per_curve):
    e = (13 - min(12, wagon_count_per_curve) )
    result_speed = (232 - (e ** 2))
    return result_speed

def curve_speed_mod(max_speed, wagon_count):
    speed_multiplier = max_speed / curve_speed_limit(wagon_count)
    result_speed_modifier =  math.ceil((speed_multiplier - 1) * 256)
    return result_speed_modifier

print('-'*32, 'Maglev Medium 1')
for x in range(2,14,2):
    print( x, curve_speed_mod(301, x) )
print('-'*32, 'Maglev Medium 2')
for x in range(2,14,2):
    print( x, curve_speed_mod(316, x) )
print('-'*32, 'Maglev Medium 3')
for x in range(2,14,2):
    print( x, curve_speed_mod(340, x) )
print('-'*32, 'Maglev Medium 4')
for x in range(2,14,2):
    print( x, curve_speed_mod(400, x) )