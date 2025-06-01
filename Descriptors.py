class Positivenumbers:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        # print("Ma'lumot chiqarish")
        print(obj.__dict__)
        return obj.__dict__.get(self.name, 0)
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Siz manfiy son kiritishingiz mkn emas!")
        obj.__dict__[self.name] = value

class Persons:
    age = Positivenumbers('age')

p = Persons()
p.age = 20
print(p.age)


class Valyuta_kurslari_som:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        print(obj.__dict__)
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Siz manfiy son kiritishingiz mkn emas!")
        obj.__dict__[self.name] = value * 12790

class Valyuta_kurslari_dollar:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        print(obj.__dict__)
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Siz manfiy son kiritishingiz mkn emas!")
        obj.__dict__[self.name] = value / 12790

class Valyuta_kurslari_yevro:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        print(obj.__dict__)
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Siz manfiy son kiritishingiz mkn emas!")
        obj.__dict__[self.name] = value * 14486

class Kurslar:
    som = Valyuta_kurslari_som('Som')
    dollar = Valyuta_kurslari_dollar('Dollar')
    yevro = Valyuta_kurslari_yevro('Yevro')

VK = Kurslar()
VK.som = 100
VK.dollar = 10000000
VK.yevro = 100

print(VK.som)
print(VK.dollar)
print(VK.yevro)

class Bank_card:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        print(obj.__dict__)
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if not value.isdigit():
            raise ValueError("Faqat sonlardan tashkil topishi kerak")
        if len(value) != 16:
            raise ValueError("Karta raqamlari soni 16 ta bo'lishi kerak")
        obj.__dict__[self.name] = value

class Test:
    karta = Bank_card('Bank_Kartasi')

T = Test()
T.karta = '8600572880082562'
print(T.karta)













