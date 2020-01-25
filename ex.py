# print('Hello world')
#
# print('in master and in branch test1')
#
# print('Hello word again')
#
# print('1234567890')
#
#
# class A:
#     y = 0
#     _x = None
#     _abc = None
#     ccc = None
#
#     def __init__(self, x, y=None):
#         self.x = x
#         if y is not None:
#             self.y = y
#
#     @classmethod
#     def foo(cls):
#         pass
#
#     @staticmethod
#     def foo2():
#         pass
#
#     def foo(self, other):
#         print('in setter x')
#         if isinstance(other, int):
#             self._x = other
#
#     def x_getter(self):
#         return self._x
#
#     x = property(x_getter, foo)
#
#     def abc_setter(self, other):
#         print('in setter x')
#         if isinstance(other, int):
#             self._abc = other
#
#     def abc_getter(self):
#         return self._abc
#
#     abc = property(abc_getter, abc_setter)
#
# a = A(10, abc=20)
# a.abc_setter(10)
#
# A.abc_setter(a, 10)
#
# A.foo()
#
#
# a.abc = 20
#
#



class B:
    a = None
    b = None
    c = None
    d = None

    def __init__(self, one=None, two=None):
        if one is not None:
            if one == '123':
                self.c = 123
            self.a = one
        if two is not None:
            self.b = two

        self.foo()

    def foo(self):
        pass

bb = B()

getattr()