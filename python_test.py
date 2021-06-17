x=[100,110,120,130,140,150]
another_list=[]
for number in x:
    mul=number*5
    another_list.append(mul)
print(another_list)



def divisible_by_three(n):
    numbers=range(1,n+1)
    for number in numbers:
        if(number%3==0):
            print(number)
divisible_by_three(20)


nested_listx=[[1,2],[3,4],[5,6]]
def flat_list(nested):
    flat_list=[]
    for sublist in nested:
        for numbers in sublist:
            flat_list.append(numbers)
    print(flat_list)
flat_list(nested_listx)


unsorted_numbers=[3,6,8,2,4,1,5,7]
def smallest(unsorted_numbers):
    sorted=unsorted_numbers.sort()
    print(sorted)
smallest(unsorted_numbers)

list_x=['a','b','a','d','b','c','e','f','g','h']

def remove_duplicate(list):
    change_to_set=set(list)
    return change_to_set
    
print(remove_duplicate(list_x))

def divisible_by_seven():
    list_div_by_7=[]
    for number in range(100,200):
        if number%7==0:
            list_div_by_7.append(number)
    print(list_div_by_7)
divisible_by_seven()


students=[
    {"age":19,"name":"Eunice"},
    {"age":18,"name":"Agnes"},
    {"age":19,"name":"Teresa"},
    {"age":19,"name":"Asha"}

]
def greetings(students):
    for student in students:
        name=student["name"]
        age=student["age"]
        print(f"Hello {name} your born in {2021-age}")
greetings(students)


class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        A=self.length*self.width
        return A
    def perimeter(self):
        add=self.length+self.width
        P=add*2
        return P
"""
instance of the object rectangle
"""
rectangle=Rectangle(23,40)
print(rectangle.area())
print(rectangle.perimeter())



        






    



    