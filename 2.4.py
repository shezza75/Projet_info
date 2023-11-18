
import random

def create_perso(depart):
    #print (depart[0])
    return {"score":0,"char" : "o", "x" : depart[0], "y" : depart[1]}

#print(create_perso((0,0)))


d = {0:' ',1:'#',2:" ",3:"X"}

m =   [[0,0,0,1,1],
       [0,0,0,0,1],
       [1,1,0,0,0],
       [0,0,0,0,0]]

p = create_perso((0,0))

def display_map_and_char(m,d,p):
    #m [p["x"]][p["y"]]=p["char"]
    for i in range(len(m)):
        for j in range(len(m[i])):      # Si on veut faire une carte pas en carre (rectangle, autres...)
        
            if i==p["x"] and j==p["y"]:
                print(p["char"],end="")
                continue
        
        # print('indice',i,j)
            for c,v in d.items():
                #print(m[i][j])
                if c==m[i][j]:                   
                    print(v , end="")
    #                 print(m)
    
            #print(m[i][j],end="")
        print("")
    # print(m)




############## 2.3

def updat_p(letter):
    if letter=="z":
        p["x"]= p["x"] -1
    elif letter=="s":
        p["x"]= p["x"] +1
        
    elif letter=="d":
        p["y"]= p["y"]+1
    else:
        p["y"]= p["y"]-1


###  2.4
# while True:    
#     a = input("Entrer direction  : ")
#     updat_p(a)

#     display_map_and_char(m, d, p)


## 3.1  - 3.2

def updat_p2(letter,m):
    # print(len(m), len(m[0]))
    # print(p["x"] ,p["y"])
    if letter=="z" and not (p["x"] -1<0  or m[p["x"] -1][p["y"]]==1 ):
        p["x"]= p["x"] -1
        
    elif letter=="s" and not (p["x"] +1>=len(m) or m[p["x"] +1][p["y"]]==1):
        p["x"]= p["x"] +1
        
        
    elif letter=="d" and not (p["y"] +1>=len(m[0]) or m[p["x"]][p["y"]+1]==1):
        p["y"]= p["y"]+1
        
    elif letter=="q" and not (p["y"] -1<0 or m[p["x"]][p["y"]-1]==1):
        p["y"]= p["y"]-1
    
   
# 3.4 

 
def create_objects(nb_objects,m):
    r=set()
    for i in range(nb_objects):
        
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
        #print(a,b , m[a][b]!=0 or (a==p["x"] and b==p["y"]),'1er' )
        while m[a][b]!=0 or (a==p["x"] and b==p["y"]):
         #   print(a,b , m[a][b]!=0 and not (a==p["x"] and b==p["y"]) )
            a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
        r.add((a,b))
    return r
objects = create_objects(3, m)
print(objects)
    

def display_map_char_and_objects(m,d,p,o):
    for i in range(len(m)):
        for j in range(len(m[i])):      # Si on veut faire une carte pas en carre (rectangle, autres...)
        
            if i==p["x"] and j==p["y"]:
                print(p["char"],end="")
                continue
            elif (i,j) in o:
                print("$",end="")
        # print('indice',i,j)
            for c,v in d.items():
                #print(m[i][j])
                if c==m[i][j]:                   
                    print(v , end="")
    #                 print(m)
    
            #print(m[i][j],end="")
        print("")
    print("Votre score est de " + str(p["score"]))
    # print(m)
   
#### 3.5

def update_objects(p,objects):
    if (p["x"],p["y"]) in objects:
        objects.remove((p["x"],p["y"]))
        p["score"]+=1


def generate_random_map(size_map,proportion_wall):
    m=[]
    for i in range(size_map[0]):
        m.append([])
        for j in range(size_map[1]):
            m[i].append(0)
    proportion_wall*=100    # on obtient le pourcentage de mur
    nb_mur = int( (proportion_wall * (size_map[0]*size_map[1])) /100 )
    
    for _ in range(nb_mur):
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)        
        while m[a][b]!=0:
        
            a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
        m[a][b]=1
    a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    while m[a][b]!=0:
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    m[a][b]=2
    a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    while m[a][b]!=0:
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    m[a][b]=3
    
    return m


print(generate_random_map((10,10), 0.33))
    
   
    
   
    
   
print(display_map_char_and_objects(m, d, p, objects))
while True:    
    a = input("Entrer direction  : ")
    updat_p2(a,m)
    update_objects(p, objects)
    display_map_char_and_objects(m, d, p, objects) 

     










