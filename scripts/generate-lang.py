n = '{}'
BLACK = '{BLACK}'
GOLD = '{GOLD}'
SILVER = '{SILVER}'
LTBLUE = '{LTBLUE}'
GREEN = '{GREEN}'
DKGREEN = '{DKGREEN}'
PURPLE = '{PURPLE}'
RED = '{RED}'
YELLOW = '{YELLOW}'
WHITE = '{WHITE}'

veh_class = BLACK + 'Vehicle class: '
INTERCITY = veh_class + SILVER  + 'INTERCITY'
LOCAL     = veh_class + YELLOW  + 'LOCAL'
STRONG    = veh_class + LTBLUE  + 'STRONG'
MEDIUM    = veh_class + GREEN   + 'MEDIUM'
FAST      = veh_class + RED     + 'FAST'
CHAMELEON = veh_class + DKGREEN + 'CHAMELEON'

connecting_1 = BLACK + 'Can attach only '
connecting_2 = BLACK + 'wagons'
connecting_3 = BLACK + 'or engines of the same type.'

def attach_1(what1, colour):
  return n + connecting_1 + colour + what1 + connecting_2 + n + connecting_3 + n

print( attach_1('Rail Express', LTBLUE))


#error_attach_rail_express   :{}Can attach only {LTBLUE}Rail Express wagons{WHITE},{}or engines of the same type.{}