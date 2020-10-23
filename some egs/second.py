import array as arr;
a=arr.array('i',[1,2,3,4,5,6])
print(a)
a.append(2225)
a.extend([555,987,36])
print(a)
a.pop()
print(a)
a.remove(987)
print (a)
print (a[0:3])
print(a[::-1])
print('all values')
for x in a:
  print(x)

b=0
while b<len(a):
  print(a[b])
  b=b+1

temp=0
while (temp<a[3]):
 print(a[temp])
 temp=temp+1

emp_details ={'EMPLOYEE': {'DAVE':{'ID':'001','SALARY':'2000','DESIGNATION':'TEAM LEAD'},'AVA':{'ID':'002','SALARY':'20000','DESIGNATION':'ASSOCIATES'}, 'UTSAV JAIN': {'ID':'000','SALARY':'321000','DASIGNATION':'CEO'}}}
print(emp_details)

mydict = {'dave':'001','ava':'002','joe':'003'}
print(mydict['dave'])
print (mydict.keys())
print (mydict.values())
print (mydict.get('dave'))

for x in mydict:
    print(x)

for x in mydict.values():
    print(x)
y=0
for x,y in mydict.items():
    print(x,y)

mydict['dave']='0005'
mydict['kris']='009'
print(mydict)

 
mydict.pop('kris')
print(mydict)

mydict['utsav']='0003'
mydict['abc']='00332'
print(mydict)
mydict.popitem()
print(mydict)

del mydict['dave']
print(mydict)

print(emp_details)

