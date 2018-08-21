
#一個學生類，用來形容學

# 定義一個空的類
class Student():
    # 一個孔磊，pass代表直接跳過
    # 此處必須由pass
    pass

# 定義一個對象

mingyue = Student()


# 在定義一個類，用來描述聽python的學生

class PythonStudent():
      # 用NONE給不確定的值賦值
      name = None
      age = 18
      course = "python"

      def dohomework(self):
          print("I 在做作業")

          return None

# 實例化一個名爲yueyue的學生


yueyue = PythonStudent()

print(yueyue.name)
print(yueyue.age)

yueyue.name
yueyue.age
# 注意成員函數的調用沒有傳遞進入參數
yueyue.dohomework()


class Student():
    name = "adad"
    age = 18

Meow = Student
print(Meow.name)


class A():
    name = "ada"
    age = 18

    # 注意say的寫法，參數由一個self
    def say(self):
        self.name = "aaa"
        self.age = 200


print(A.name)
print(A.age)

print("*" *20)
a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.(age)))

Teacher.sayAgain()


class Fish():
    def _init_(self, name):
        self.name = name

    def swim(self):
        print("i am swimming....")


class Bird():
    def _init_(self, name):
        self.name = name

    def fly(self):
        print("i am fly..")


class person():
    def _init_(self, name):
        self.name = name

    def worked(self):
        print('working....')


class SuperMan(Person, Bird, Fish):


s = SuperMan()
s.fly()
s.swim()
