
print (format('*','*<15'),'ENTRY SECTOIN', format('*','*<15'))

m1=float(input("marks in  examination 1 (out of 100) => "))
m2=float(input("marks in  examination 2 (out of 100) => "))
m3= float(input("mark in sports activity (out of 50) => "))
m4= float(input("mark in activity 1 (out of 20) => "))
m5= float(input("mark in activity 2 (out of 20) => "))
m6= float(input("mark in activity 3 (out of 20) => "))

em=m1+m2
am=m4+m5+m6
#examination percentage is 50%
#activity percentage is 30%
#sports activity is 20%

ep=float(em*0.5/200)
sp=float(m3*0.2/50)
ap=float(am*0.3/60)

print (format('*','*<15'),'RESULT', format('*','*<15'))
print ("marks in firt examination(out of 100) is =>", m1)
print ("marks in second examination (out of 100) is => ",m2)
print (format ('*','*<30'))
print ("total marks of examinations is => ", em)
print (format ('*','*<30'))
print ("marks in sports activity (out of 50) is => ",m3)
print (format ('*','*<30'))
print ("total marks of sports activity is => ", em)
print (format ('*','*<30'))
print ("marks in activity 1 (out of 20) is => ",m4)
print ("marks in activity 2 (out of 20) is =>",m5)
print ("marks in activity 3 (out of 20) is =>", m6)
print (format ('*','*<30'))
print ("marks in activity is => ",am)
print (format ('*','*<30'),'\n \n')

print (format ('*','*<30'),'\n \n')
print ("the percentage marks of examinations is =>" , ep)
print ("the percentage marks of acticity is =>" , ap, format(ap,'0.2f'))
print ("the percentage marks of sports activity is =>" , sp)
print (format ('*','*<30'),'\n \n')

