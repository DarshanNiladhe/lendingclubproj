print('hello world')
emp_list=[1,2,3,"name","darshan","kanchan"]
print(type(emp_list))
print(emp_list)
print(emp_list[3])
print(emp_list[0:4])
print(emp_list[::2])
for item in emp_list:
    print(item)

print(emp_list[-1])
print("no of item in list is:",len(emp_list))

for i in range(2,101,2):
    print(i)

for i in range(len(emp_list)):
    print(emp_list[i])

print("pop--------------")
for i in range(len(emp_list)):
    print(emp_list.pop(-1))
print(emp_list)

def sum(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return a+b
    else:
        print("please pass valid datatype")
sum(1,"abc")
sum(1, 3)


f=lambda a:a*a
result=f(5)
print(result)


mylist=[1,2,3,4,5,6]
newlist=list(filter(lambda a:(a/3==2),mylist))
print(newlist)

mylist=[1,2,3,4,5,6]
newlist=list(map(lambda a:(a/3!=2),mylist))
print(newlist)

s=lambda a:a*a
s(4)






