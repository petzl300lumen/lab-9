class LenError(BaseException):
    pass
class ZeroError(BaseException):
    pass
class IsInstanceError(BaseException):
    pass

class A:
    def namelen(self,name):
        if len(name)<3:
            raise LenError("Имя слишком короткое")

    def valuezero(self, value):
        if value <=0:
            raise ZeroError("Значение не может быть равно нулю")
    
    def typeexp(self, value):
        if isinstance (value, str):
            raise IsInstanceError("Введенное значение не может быть строковым типом")

class Handler:
    def __init__(self, obj):
        self.obj = obj

    def process_1(self):
        try:
            self.obj.namelen("D")
        except LenError as e:
            print("Сработало исключение LenError:", e)

    def process_2(self):
        try:
            self.obj.valuezero(0)
        except ZeroError as e:
            print("Сработало исключение ZeroError:", e)

    def process_3(self):
        try:
            self.obj.typeexp("sdsd")
        except IsInstanceError as e:
            print("Сработало исключение IsInstanceError:", e)

a = A()
b = Handler(a)

b.process_1()
b.process_2()
b.process_3()