# this is the simple way to create a class and create a __init__ function as a constructor to initilize the variable

class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city


    def __repr__(self):
        return (f'Person(Name={self.name}, Age={self.age}, City={self.city})')


    def __eq__(self,other):
        if (self.name,self.age,self.city) == (other.name,other.age,other.city):
            return True
        else:
            return False  

p1 = Person('Krishna Verma',23,'Varanasi')

p2 = Person('Krishna Verma',23,'Varanasi')

print(f'Name = {p1.name} Age = {p1.age} City = {p1.city}')
print(f'Name = {p2.name} Age = {p2.age} City = {p2.city}')

print(p1,p2)
print(p1==p2)


# Using data class we can initilize the variable without creating the constructor 

print('-------------------Using data class to initilize the variable----------------')
from dataclasses import dataclass 

@dataclass(order = True,frozen= False,unsafe_hash = True)  #init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False parameter of the dataclass
class NewPerson:
    name: str
    age: int   
    city: str 
    isActive: bool 

p1 = NewPerson('Krishna Verma',23,'Varanasi',True)
p2 = NewPerson('Krishna Verma',23,'Varanasi',True)
print(f'Name = {p1.name} Age = {p1.age} City = {p1.city} IsActive = {p1.isActive}')
print(p1)
print(p1==p2)



# @dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False) , match_args=True, kw_only=False, slots=False, weakref_slot=False
print('########################################')
# if order == True then it runs these magic function  by defaut order == False
# __lt__ <
# __le__ <=
# __gt__ >
# __ge__ >=

p3 = NewPerson('Krishna Verma',23,'Varanasi',True)
p4 = NewPerson('Krishna Verma',22,'Varanasi',True)

print(p3>p4)
print(p3>=p4)
print(p3<=p4)
print(p3<p4)

print('#######################################')

# for frozen if you want to ristrict the propertise can not be updated after once you declear the object 

print(p3.name)
p3.name = 'KRISHNA VERMA' 
# here the interpretor give the error like this 
# dataclasses.FrozenInstanceError: cannot assign to field 'name' if frozen = True 
print(p3.name)



print('###########################################')
# hash is used to generate the unique identification for the object but it used only for unmutable datastructre 
# but you want to generate the unique identification for the object which is mutable then you just write 
# unsafe_hash =True by defaut it is false and the value of hash is change after every time when you run the program 
print(f'p3 hash = {hash(p3)} and p4 hash = {hash(p4)}')