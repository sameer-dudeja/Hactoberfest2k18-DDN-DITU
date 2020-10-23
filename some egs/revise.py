print(format('*','*<15'), 'ENTERIES SECTION', format('*','*<15'))
print(format('*','*<15'), 'ENTERIES SECTION for EXAMS (out of 100)', format('*','*<15'))
m1 = float(input("ENTER THE MARKS IN EXAM 1 => "))
m2 = float(input("ENTER THE MARKS IN EXAM 2 => "))

print(format('*','*<15'), 'ENTERIES SECTION fro ACTIVITY (OUT of 20)', format('*','*<15'))

a1 = float(input("ENTER THE MARKS IN ACTIVITY 1 => "))
a2 = float(input("ENTER THE MARKS IN ACTIVITY 2 => "))
a3 = float(input("ENTER THE MARKS IN ACTIVITY 3 => "))

print(format('*','*<15'), 'ENTERIES SECTION for SPORTS EVENT (out of 50)', format('*','*<15'))

s1=float (input("enetr the marks in Sports event => "))

#calculatios

et = m1+m2
at=a1+a2+a3
st=s1

eavg= (et*50)/200
aavg= (at*30)/60
savg= (st*20)/50

print(format('*','*<15'), 'RESULT', format('*','*<15'))

print('the marks in first exam is => ', m1)
print('\n the marks in second exam is => ', m2)

print('\n \n  the marks in first  activity is => ', a1)
print('\n  the marks in second  activity is => ', a2)
print('\n  the marks in third  activity is => ', a3)

print('\n \n   the marks in sports activity is => ', s1)


print('\n  the total marks in exams  is => ', et)
print('\n  the total marks in  activity is => ', at)
print('\n  the total marks in sports activity is => ', st)

print('\n ***********************************************')
print('\n  the total marks average in exams  is => ', eavg)
print('\n  the total marks average in  activity is => ', aavg)
print('\n  the total marks average in sports activity is => ', savg)

print("total average marks is ", eavg+aavg+savg)

print('*************************************************')

