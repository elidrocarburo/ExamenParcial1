
a=["Alicia", "Benny", "Carlos", "Daniel", "Eloise", "Felipe", "Francisco", "Gregory", "Maria", "Ofelia"]
b= ["Alicia", "Bianca", "Carlos", "Daniel", "Eliza", "Ferdinand", "Francisco", "Jesus", "Noemi", "Ofelia"]

def addTo (a):
    x= input("Input name on alphabetical order")
    a.append(x)
    print(a)
    i=input("Continue? Y/N")
    if i=="Y":
        addTo(a)
    else:
        print(a)
    return a

def compare(arrayA, arrayB):
    uniqueA =[]
    uniqueB =[]
    common =[]
    if len(arrayA) > len(arrayB):
       x= len(arrayA)
    elif len(arrayB) <= len(arrayA):
       x =len(arrayB)
    for i in range(len(arrayB)):
      if (arrayA[i] != arrayB[i]):
        uniqueA.append(arrayA[i])
      elif (arrayB[i] != arrayA[i]):
        uniqueB.append(arrayB[i]) 
      elif (arrayB[i] ==arrayA[i]):
        common.append(arrayB[i])   
    print(uniqueA)
    print(uniqueB)
    print(common)

addTo(a)
addTo(b)
compare(a, b)