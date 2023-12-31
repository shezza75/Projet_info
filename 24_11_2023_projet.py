
import random
import time      # Pour faire la contrainte du temps
import msvcrt    # Pour mieux gerer l'entree input




def create_perso(depart):
    #print (depart[0])
    return {"score":0,"char" : "o", "x" : depart[0], "y" : depart[1]}

#print(create_perso((0,0)))


def generate_random_map(size_map,proportion_wall):
    m=[]
    for i in range(size_map[0]):
        m.append([])
        for j in range(size_map[1]):
            m[i].append(0)
    
    
    proportion_wall*=100    # on obtient le pourcentage de mur
    nb_mur = int( (proportion_wall * (size_map[0]*size_map[1])) /100 )
    
    for _ in range(nb_mur):                                                     # genere les murs
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)        
        while m[a][b]!=0:
        
            a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
        m[a][b]=1
    
    
    
    a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)           # genere l entree
    while m[a][b]!=0:
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    m[a][b]=2
    
    a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)           # genere sortie
    while m[a][b]!=0:
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    m[a][b]=3
    a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    
    while m[a][b]!=0:                                                           # genere cle
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    m[a][b]=4
    return m


## 3.1  - 3.2
def delete_all_walls(m,pos):
    
    if pos[0]-1>=0:
        if m[pos[0]-1] [pos[1]]==1:
            m[pos[0]-1] [pos[1]]=0
    
    if pos[0]+1<len(m[0]):
        if m[pos[0]+1] [pos[1]]==1:
            m[pos[0]+1] [pos[1]]=0
    
    if pos[1]-1>=0:
        if m[pos[0]][pos[1]-1]==1:
            m[pos[0]] [pos[1]-1]=0
    
    if pos[1]+1<len(m):
        if m[pos[0]] [pos[1]+1]==1:
            m[pos[0]] [pos[1]+1]=0
        
        
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
    elif letter=="e":
        delete_all_walls(m, (p["x"],p["y"]))
        
        
    
   
# 3.4 

 
def create_objects(nb_objects,m):       # probleme ne cree pas le bon nombre d'objet, superpostion des objets
    r=set()
    for i in range(nb_objects):
        
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
        #print(a,b , m[a][b]!=0 or (a==p["x"] and b==p["y"]),'1er' )
        while m[a][b]!=0 or (a==p["x"] and b==p["y"]) or (a,b) in r:
         #   print(a,b , m[a][b]!=0 and not (a==p["x"] and b==p["y"]) )
            a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
        r.add((a,b))
    #print(len(r))
    return r




    

def display_map_char_and_objects_key(m,d,p,o):
    for i in range(len(m)):
        for j in range(len(m[i])):      
        
            if i==p["x"] and j==p["y"]:
                print(p["char"],end="")
                
            elif (i,j) in o:
                print('€',end="")
                
        # print('indice',i,j)
            else :
                for c,v in d.items():
                #print(m[i][j])
                    if c==m[i][j]:
                        if c==3:
                            if key!=None:
                                print(' ',end='')
                            else:
                                print(v,end='')
                        else:
                            print(v , end="")
                        
    #                 print(m)
    
            #print(m[i][j],end="")
        print("")
    print("Votre score est de " + str(p["score"]))
    # print(m)
    return ''
   
#### 3.5

def update_objects_key(p,obj, key):
    if (p["x"],p["y"]) in obj:
        obj.remove((p["x"],p["y"]))
        p["score"]+=1
    elif (p["x"],p["y"]) == key:
        m[p["x"]][p["y"]]=0
        key=None
    return key
        

def create_new_level(p,obj,nb_obj,size_map,proportion_wall):
    m=generate_random_map(size_map, proportion_wall)
    print(obj , len(obj))
    for i in range(size_map[0]):
        for j in range(size_map[1]):        # change coordonee perso / point d apparition
            if m[i][j]==2:
                p["x"],p["y"] = i,j
            if m[i][j]==3:                  # Pour comparer les coordonnees perso avec coordonnee sortie
                sortie=(i,j)
    nb_obj+=1
    obj = create_objects(nb_obj, m)
    return m,obj,sortie
    

     
d = {0:' ',1:'#',2:" ",3:"֎",4:"Ꙉ"}
size_map=(3,3)
proportion_wall=0.1

m = generate_random_map(size_map,proportion_wall)

for i in range((size_map[0])):             # Instancie les premieres du premier niveau 
    for j in range((size_map[1])):
        if m[i][j]==2:
            p = create_perso((i,j))
        if m[i][j]==3:
            sortie=(i,j)
        if m[i][j]==4:                      
            key =(i,j)

nb_obj=1
obj = create_objects(nb_obj, m) 
#print(obj)
   
print(display_map_char_and_objects_key(m, d, p, obj))



start_time = time.perf_counter()
while True:
    
    a = input("Entrer direction  : ")
    sortie=None
    
    
    updat_p2(a,m)
    key= update_objects_key(p, obj,key)
    
    if (p["x"],p["y"])==sortie and key==None:
        demand = input('Sortir ? Oui: o , Non: n  : ')
        if demand=='o':
            m,obj,sortie = create_new_level(p,obj,nb_obj,size_map,proportion_wall)
            
    print(m)
    
    for i in range((size_map[0])):             # evite que le perso commence dans un mur
        for j in range((size_map[1])):
            if m[i][j]==4:
                key =(i,j)
    display_map_char_and_objects_key(m, d, p, obj) 
    
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
     
    print(f"Programme exécuté en : {execution_time: .2f} secondes")

     


