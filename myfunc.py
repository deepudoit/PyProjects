import random


#Class to demostrate __call__
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(5))


#Return factorial of a number
def fact(n):
    '''
  Funtion to retrun factorial of a given num
  '''
    return 1 if n < 2 else n * fact(n - 1)


#Store func/class obj attributes. Retrieve it using __dict__
def upper_case_name(obj):
    return ('%s %s' % (obj.first_name, obj.last_name)).upper()


upper_case_name.short_description = 'Customer name'


class C:
    pass


obj = C()


def func():
    pass


sorted(set(dir(func)) - set(dir(obj)))


# Code to generate HTML by passing tags, class and others
def tag(name, *content, cls=None, **attrs):
    '''Generate one or more HTML tags'''
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name)
                         for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


my_tag = {
    'name': 'img',
    'title': 'Sunset Boulevard',
    'src': 'sunset.jpg',
    'cls': 'framed'
}

# for name, value in bound_args.arguments.items():
#     print(name, '=', value)