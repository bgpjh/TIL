class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    # 매직 메소드 활용해보자!
    def __gt__(self, other):
        return self.age > other.age
    def __len__(self):
        return self.height
    def __str__(self):
        return f'<{self.name}> : {self.age}살'
        #<main.Person object at 0x0000014A79EE5DC0> => <재영> : 100살
        # map처럼 더럽게 출력되는 부분을 개발자가 보기 편하게 str형태로 확인가능

p1 = Person('재영',100,190)
p2 = Person('지선',10,185)
print(p1 > p2)
print(len(p1))
print(len(p2))
print(p1)
#print(dir(p1))