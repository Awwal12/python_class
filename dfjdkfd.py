from collections import namedtuple
# a = "vkdfjdvjfkvodndknmnmskdfnxxm"
# pri = Counter(a)
# print(pri.most_common(19))
# print(list(pri.elements()))
Point = namedtuple('Point', 'x,y')
pt = Point(5, -5)
print(pt.x, pt.y)
