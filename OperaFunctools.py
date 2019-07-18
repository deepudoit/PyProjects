from functools import reduce

# def fact(n):
#     return reduce(mul, range(1, n + 1))

# Operator itemgetter
from operator import itemgetter

metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(0, 3)
for cc in metro_data:
    print(cc_name(cc))

# Operatoe attrgetter
from operator import attrgetter
from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [
    Metropolis(name, cc, pop, LatLong(lat, long))
    for name, cc, pop, (lat, long) in metro_data
]

metro_areas[0]
metro_areas[0].coord.long

for city in sorted(metro_areas, key=attrgetter('pop')):
    print(cc_lat(city))

# Functions under opeartormodule
[name for name in dir(operator) if not name.startswith('_')]

from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')

from functools import partial
from operator import mul
triple = partial(mul, 3)

s1 = 'café'
s2 = 'cafe\u0301'

picture = partial(tag, 'img', cls='pic-frame')
