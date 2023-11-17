
from random import randint


dico = {0:' ',1:'#'}
m = [[0,0,0,1,1],
       [0,0,0,0,1],
       [1,1,0,0,0],
       [0,0,0,0,0]]



def display_map(m,d):
    
    for i in range(len(m)):
        for j in range(len(m[i])):      # Si on veut faire une carte pas en carre (rectangle, autres...)
            # print('indice',i,j)
            for c,v in d.items():
                #print(m[i][j])
                if c==m[i][j]:                   
                    m[i][j]=v
    #                 print(m)
            print(m[i][j],end="")
        print("")
        
    

print(display_map(m,dico))        
    











