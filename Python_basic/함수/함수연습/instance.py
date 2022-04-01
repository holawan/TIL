class Person :
    #인스턴스 메서드는 python 내부적으로 person.test(p1)    
    def test(self) :
        return 'test'
# 인스턴스 생성 (p1 )
p1 = Person()


#p1.test()
#test() takes 0 positional arguments but 1 was given

s = p1.test()
print(s)
print(s,p1)
#test <__main__.Person object at 0x000001BBFA44B670>