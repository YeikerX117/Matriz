#Yeimer Serrano Navarro
#20181020060
#Modelos de programación II

matriz=[[1,2,3,],[4,5,6,],[7,8,9]]

for i in range(3):
    for j in range(3):
        if(i==0):
            print(matriz[i][j])
        if(j==2 and i!=0):
            print(matriz[i][j])

for i in range(3):
    for j in range(2, -1, -1):
        if(i==2 and j!=2):
            print(matriz[i][j])
            
for i in range(3):
    for j in range(3):
        if(i==1 and j!=2):
            print(matriz[i][j])
