# A Dictionary Maps Keys to Values Like a real - World Dictionary Maps Words to meanings



student={
 "name":"alice",
 "age":"21",
 "grade":"A"
}
print(student.get(1))
print(student.values()) # this line print to the key value of Dictionary
print(student.keys()) # this line print to the key of the Dictionary
print(student.items()) # this line print to the items of Dictionary
print(type(student))



map={1:["one",[1,2]],2:'two'}
print(type(map[1]))
print(type(map))
print(map[1])
print(map[2])



#Dictionary Functions


map={1:["one",(1,2)],2:'Two'}
print(type(map))
print(map.get(1))
print(map.get(2))
#Element Access World of Print:

#Comment Funition's comment funition's 

#length
print(len(map))

#key get to the keys value 
print(map.get(2))

#values


print(map.values())
print(map.items())
print(map.keys())
map[4]="Four"
print(map)


#remove 

map.pop(1)
print(map)

#clear 
map.clear()
print(map)

#dict
map=dict()
print(type(map))
print(type(dict))

#there store with key and value store with the program languge.
#Quiz Dictionary


#Dictionary and list comination 


set1={1,2,3,4}
print(set1)
print(type(set1))


#Dupat not to be allowed 


#add the element in set add

set1.add(67)

#under set so do not get the order to the set value 

#remove 
print(set1)
set1.remove((3))
print(set1)


set01={1,2,3,4}
set02={1,4,5,6}
print(set01)
print(set02)
print(set01.union(set02))
print(set02.union(set01))
print(set01.intersection(set02))
print(set01.difference(set02))
print()
print(set01.difference(set02))
print(set01)
print(set02)

set12={1,2,3,4}
set13={4,5}
set14={2,3,4,5,7,8}   


print(set12.union(set13).intersection(set14)) # 2,3,4,5 this a output  frist is add differnt of number set and add for a commun number a set  
print(set12.union(set13)) # add for a set12 and set13 values in the set different number in the number 
print(set13.intersection(set14)) # it a output for a same of the set in the set13 and set14 in the value of the output 
print(set13.difference(set14))   # this line of the function in the set of the element of the value set13 output id differnet of the element 



# list of the Comprehension 

arr=[1,2,3,4,5,6,7,8]

odd=[1,3,5]

for i in arr:
    if i%2==1:
        odd.append(i)
    elif i%2==0:
        odd.append(i)
odd=[i for i in arr if i%2!=1]
print(odd)

even=[i for i in arr if i%2!=0]
print(even)


