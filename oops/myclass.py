class Mylist:

    def __init__(self,l=[]):
        self.l = l

    def append(self,value):
        self.l.append(value)
    
    def insert(self,index,value):
        self.l.insert(index,value)

    def pop(self):
        self.l.pop()

    def getvalue(self):
        print("Data : ",self.l)

    def __str__(self):
        return f"{self.l}"

obj = Mylist([2,3,4])
obj.append(10)
obj.insert(1,20)
obj.getvalue()
print(obj)
