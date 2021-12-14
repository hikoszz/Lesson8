class animals:
    def __init__(self,gender, name, age, height, weight): 
        self.gender = gender
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
class mammals(animals):
    def __init__(self, gender, age, name, height, weight, poroda, color): 
        
        self.gender = gender
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight
        self.poroda = poroda
        self.color = color
    

class human(mammals):
    def __init__(self, gender, age, name, height, weight, income, workstag, company, poroda=0, color=0): 
        super().__init__(gender, age, name, height, weight, poroda, color)
        self.income = income
        self.workstage = workstag
        self.company = company


class Students(human):
    def __init__(self, gender, age, name, height, weight, income, workstag, company,dz, poroda=0, color=0):
        super().__init__(gender, age, name, height, weight, income, workstag, company, poroda, color)
        self.dz = dz
    def __en__(self, other): 
        if(self.dz != other.dz): 
             return "True" 
        else: 
            return "False"

        

class cat(mammals):
    def __init__(self,eyescolor, charater, gender, age, name, height, weight, poroda, color  ): 
        super().__init__(gender, age, name, height, weight, poroda, color)
        self.eyescolor = eyescolor
        self.charater = charater


class dog(mammals):
    def __init__(self,gender, age, name, height, weight, poroda, color, teeth, foot  ):
        super().__init__(gender, age, name, height, weight, poroda, color)
        self.teeth = teeth
        self.foot = foot






tigr = animals('Male', 'Kisa',2, 40, 34)
print('Класс животных')
print(tigr.gender)
print(tigr.name)
print(tigr.age)

Pyma = mammals('Predator', 'Black', 'Female', 20, 'Zinka', 70, 30)
print('Класс млекопитающих')
print(Pyma.poroda)
print(Pyma.name)
print(Pyma.color)


Human = human('Male', 32, 'Andy', 160, 70, 200000, 10, 'Zavod' )
print('Класс человека')
print(Human.company)
print(Human.name)
print(Human.age)
print(Human.income)
print(Human.workstage)

Cat = cat('Black', 'Zloy', 'Fame', 20, 'Kesha', 20, 10, 'Domashya', 'Black')
print('Класс кот')
print(Cat.eyescolor)
print(Cat.name)
print(Cat.gender)
print(Cat.age)
print(Cat.poroda)

Dog = dog('Female', 13, 'Ignat', 66, 21, 'Domasnii', 'Black', 30, 4)
print('Класс собака')
print(Dog.gender)
print(Dog.age)
print(Dog.name)
print(Dog.weight)
print(Dog.foot)

Student = Students('Male', 19, 'Sergey',180, 90, None, 1, None, 3,None,None )
print('Студент')
print(Student.age)
print(Student.name)
print(Student.dz)

Student = Students('Male', 19, 'Sergey1',180, 90, None, 1, None, 4,None,None )
print('Студент')
print(Student.age)
print(Student.name)
print(Student.dz)
