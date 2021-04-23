import chalk


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [99, 77, 55, 33, 22, 11]
bubblesort(arr)
print(chalk.red("Sorted Array is"))
for i in range(len(arr)):
    print("%d" % arr[i])

class Employee:
    def __init__(self,id):
        self.id=id

    def setname(self,name):
        self.name=name

    def getname(self):
        return self.name

    def getid(self):
        return self.id

class Student:
    def __init__(self,col_name):
        self.col_name=col_name

    def setbranch(self,branch):
        self.branch = branch

        def getcolname(self):
            return self.col_name

        def getbranch(self):
            return self.branch

class Intern(Employee, Student):
    def __init__(self, id, col_name, period):
        Employee.__init__(self, id)

        Student.__init__(self, col_name)
        self.period = period

    def setdetails(self, name, branch):
        super().setname(name)
        super().setbranch(branch)

    def getdetails(self):
        print("ID : ", super().getid())
        print("NAME : ", super().getname())
        print("COLLEGE NAME : ", super().getcolname())
        print("BRANCH : ", super().getbranch())
        print("PERIOD : ", self.period)

i = Intern(21, "RIZVI", 7)
i.setdetails('M.Kaif', 'Computer')
i.getdetails()

