#객체지향
a = [1,2,3]

a.sort()

a.reverse()

a.append(4)

class Person :

    def greeting(self) :
        print('안녕하세요'+self.name+'입니다.')


jimin = Person()
jimin.name = '지민'
jimin.phone ='010102341234'
jimin.greeting()

hyoeun = Person()
hyoeun.name = '효은'
hyoeun.greeting()