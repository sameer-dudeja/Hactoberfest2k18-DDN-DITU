def pattern(n):
      k=2*n-2
      for i in range(0,n):
            for (j) in range (0,k):
                  print (end=" ")
            k=k-1
            for j in range (0, i+1):
                  print("*", end=" ")
            print ('\r')

pattern(10)



def pattern2(n):
      k=2*n-2
      for i in range(n,-1,-1):
            for (j) in range (k,0,-1):
                  print (end=" ")
            k=k+1
            for j in range (0, i+1):
                  print("*", end=" ")
            print ('\r')

pattern2(10)

def pattern3(n):
      for i in range(0,n):
            for (j) in range (0,i+1):
                  print ('*',end=" ")
            print('\r')
            for i in range (n,-1,-1):
                  for j in range (0, i+1):
                        print("*", end=" ")
                  print ('\r')
      
pattern3(10)
