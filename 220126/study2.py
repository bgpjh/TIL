class list_test:
    def append2(self,a):
        self.list = self.list + [a]

test = list_test()
test.list = [1,2,3]
print(test.list)
test.append2(4)
print(test.list)
print(type(test))
print(type(test.list))