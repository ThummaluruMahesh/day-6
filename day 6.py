# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]
'''
s1 = "how are you"
print(s1.replace("h","H"))
print(s1.replace("u","U"))
How are you
how are you
'''
'''
s1 = "how are you"
fst = s1[0].upper()
lst = s1[-1].upper()

print(fst+s1[1:len(s1)-1]+lst)

How are yoU
'''

# 2.)
'''

n = 128
tem = n
f1 = 0
while n!=0:
    rem = n%10
    check = tem%rem
    if check !=0:
         f1 = 1
    n=n//10
if f1==0:
    print("yes")
else:
    print("no")

yes
'''

l1 = [8,9,0,7]
l2 = [7,6,5,4]
l3=[]
'''

print(l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3])

for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)


15 15 5 11
[15, 15, 5, 11]

'''

# 1 -----> set
# characteristics of set
#1.) set can be created using{}
#2.) The element inside set are not indexed
#3.) Does not allow duplicate values
#4.) it unordered
#5.) heterogenous
#6.) mutable or changable



# Eg : 1
'''
s1 = {9,89,7.76,8+7j,(8,7,5), "truck","e"}
print(s1)
{89, (8, 7, 5), 'truck', 7.76, 9, 'e', (8+7j)}
'''

# Eg : 2
'''
s2 = {5,8,98,[9,0]}
print(s2) ---> error
'''

#Eg : 3
#min(),max(),len()

# * Eg
# ? to add element inside set
'''
s1 = {8,78,67,'u'}

#add()
s1.add(43)
print(s1)
{67, 8, 'u', 43, 78}

'''

#update()
#s1.update(9,0)
#print(s1)

# ? To delete element inside set
'''
s1 = {8,78,67,'u'}
'''
'''
#pop() ---> to delete one element randomly
s1.pop()
print(s1)
{67, 'u', 78}
'''
# discard()
'''
s1.discard(8967)
print(s1)

{8, 67, 'u', 78}
'''
# clear ()
'''
l1= {}
print(type(l1)) 
<class 'dict'>
'''

#s1 = set() # to create empty set
#print(type(s1)) 
'''
s1 = {8,9,0}
s1.clear()
print(s1)

 set()
  
'''

# del s1
# print(s1)


# * join the sets
'''
s1 = {9,0,8}
s1 = {9.90,"card",'t',56}
#union()
s3 = s1.union(s2)
print(s3)
'''
# * intersection() --> to get common elements inside set
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))

{5, 6}
'''
# * difference()
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

{4}
{8, 7}
{4, 7, 8}
'''

# isdsjoit(), issubset(), issuperset()
'''

s1 = {8,9,0}
s2 = {6,7,5,8,9,0}
print(s1.issubset(s2))
print(s2.issuperset(s1))

True
True
'''
# ! ---> problem:1
'''
s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

for val in s1:
    if val in s2:
        str1 = "Its join set"
print(str1)
    
Its join set
'''

# ? o/p --> Its a joinset
# ! -----> dictionary
# Eg: 1
'''
d1 = {1:100,'a':200,4.5:"hello"}
print(d1)
print(len(d1))
{1: 100, 'a': 200, 4.5: 'hello'}
3

'''
# Eg:2
'''
d1 = {1:100,'a':200,4.5:"hello"}
marks_stud1 = {"english": 79, "maths":20, "physics":60}
print(d1)
print(len(d1))
'''


# ? char of dictionary
#1.) have to be surrounded by {}
#2.) It have to be in the form of key, va;lue pair
#3.) It is mutable
#4.) duplicate keys are not allowed ,duplicate values are allowed
#5.) It is unindexed
#6.) It is ordered
#7.) key does not allow mutable datatype, values allow mutable datatype

'''d1 = {1:100,2:200,3:300,4:400}'''
# * to access element in dictionary

#print(d1)
#or
#to access the values, have to use key
#print(1[1]) # ---> 100

# ? some common functions
#len(),min(),max()
#print(min(d1))
#print(max(d1))

# ? To find min, max based on values
#print(min(d1.values()))
#print(max(d1.values()))


# ? dictionary based functions
# to add element (key and value pair) in dict
'''
d1 = {1:100,2:200,3:300,4:400}
d1[5] = 500
print(d1)

{1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
'''

# ? To replace a value in dictionary
'''
d1 = {1:100,2:200,3:300,4:400}
d1[2]="mango"
print(d1)
{1: 100, 2: 'mango', 3: 300, 4: 400}
'''

# ? delete element from dictionary
'''d1 = {1:100,2:200,3:300,4:400}'''
#popitem() # ---> to delete last key value pair in dict
'''
d1.popitem()
print(d1)
{1: 100, 2: 200, 3: 300}
'''

# pop()
'''
d1.pop(2) # 2 is the bkey in dictionary
print(d1)
{1: 100, 3: 300, 4: 400}
'''

# clear(), del

# * join 2 dictionary
'''
d1 = {1:100,2:200,3:300,4:400}
d2 = {"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)

{1: 100, 2: 200, 3: 300, 4: 400, 'a': 'apple', 'b': 'boy', 'g': 'game'}

'''

# get() ---> used to get the value from a key
'''
d1 = {1:100,2:200,3:300,4:400}
print(d1[90])
print(d1.get(90))
      '''

# to print the all keys
'''
print(d1.keys())
print(type(d1.keys()))
      
dict_keys([1, 2, 3, 4])
<class 'dict_keys'>
'''

# to print all the values
#print(d1.values())

# * Iterate dictionary
'''
for val in d1 : # to iterate keys alone
    print(val)
1
2
3
4

'''
'''
for val in d1.values(): # to iterate values alone
    print(val)

100
200
300
400
'''

# to get both key and values
'''
for key, val in d1.items():
    print(key,val)
1 100
2 200
3 300
4 400
'''
# ! problem: 1

'''
n = int(input(" enter the number  of times: "))
integer = []
float_value =[]
string=[]

for val in range(n):
    value =eval(input("enter the value"))
    if type(val)==int:
        integer.append(val)
    elif type(val)==float:
        float_value.append(val)
    elif type (value)==str:
        string.append(val)
    else:
        print("pls provide data in int, float,string")
print(integer)
print(float_value)
print(string)
   '''

# Return a set of elements present in Set A or B, but not both
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3=set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
    print(set3)
    '''

# ! ------> problem 3
'''
l1 = [1,2,3,4]
l2 = ["a","b","c","d"]

d1 = {}

d1[l1[0]] =l2[0]
d1[l1[1]] =l2[1]
d1[l1[2]] =l2[2]
d1[l1[3]] =l2[3]
print(d1)

{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
'''
'''
d1 = {}
for val in range(len(l1)):
    d1[l1[val]] = l2[val]
    print(d1)
{8: 7}
{8: 7, 9: 6}
{8: 7, 9: 6, 0: 5}
{8: 7, 9: 6, 0: 5, 7: 4}
'''





# ! or
'''
c = 0
for val in set1,set2:
    c=c+1
    if c==1:
        for element in val:
            if element not in set1:
                set3.add(element)
    elif c==2:      
          for element in val:
            if element not in set1:
                set3.add(element)
                
print(set3)
'''
'''
set1  = (10, 20, 30, 40, 50)
set2 = (30, 40, 50, 60, 70)
print(set1[1],set2[4],set1[0],set2[3])
'''
dict={"joey":1,"rachel":2}
dict.update({"phoebe":2})
print(dict)





# o/p
# {20, 70, 10, 60}










#1.) swap elemwnts in string list
# The original list is :["Gfg", "best", "for", "Geeks"]
# List after performing character swaps:]"efg", "is", "bGst", "for", "eGGks"]
















'''
mech_name = ["name","name2","name3"]
mech_age = [23,24,22]
mech_mark = [89,78,60]
mech_email = ["name2@gmail.com","name3@gmail.com"]


mech = {
    "student1":{
        "name":"name1"
        "age":24,
        "mark":89,
  },
   "student2":{
        "name":"name2"
        "age":24,
        "mark":89,

  },
   "student3":{
        "name":"name3"
        "age":24,
        "mark":89,

'''




