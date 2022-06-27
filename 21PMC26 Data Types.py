#Numeric Data Types
a = 2
print("Type of a: ", type(a)) 

b = 2.0 
print("\nType of b: ", type(b))

c = 3 + 4j 
print("\nType of c: ", type(c))

#Sequence Data Type
String1 = '''I'm a
"Homo sapiens"''' 
print(String1) 
print(type(String1))

List = [['Human', 'Dog'], ['Alien']] 
print(List)

list1 = [1, 2, 3, 4, 5, 6] 
Tuple1 = tuple(list1)
Tuple2 = ('Electron', 'Proton') 
Tuple3 = (Tuple1, Tuple2) 
print(Tuple3)

#Boolean Data Type
print(3 > 2)
print(3 == 2)
print(3 < 2)

#Set Data Type
set1 = set([1, 2, 'My', 3, 'name', 4, 'is'])
print(set1)

#Dictionary Data Type
Dict1 = dict([(1, 'Priyanuj'), (2, 'Kashyap')])
Dict2 = dict({1: "I'm", 2: 'a', 3:'Boy'})
print(Dict1,Dict2)