class test:
    def __init__(self,val=[1,2,3,4]):
        self.val = val
    def __str__(self):
        return str(self.val)

what = test()
what.aab = 5
print(what)
print(what.aab)

what2 = test(1)
print(what2)
print(what2.val)