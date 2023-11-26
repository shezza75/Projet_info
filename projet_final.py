
import random
import time      # Pour faire la contrainte du temps




def create_perso(depart):        # création d'un dictionnaire pour le personnage
    #print (depart[0])
    return {"score":0,"char" : "o", "x" : depart[0], "y" : depart[1]}

#print(create_perso((0,0)))


def generate_random_map(size_map,proportion_wall):        # Création carte
    m=[]
    for i in range(size_map[0]):                          # Création d'une matrice de la taille souhaité par size_map rempli que de 0 (espace libre)
        m.append([])
        for j in range(size_map[1]):
            m[i].append(0)
    
    
    proportion_wall*=100    # on obtient le pourcentage de mur
    nb_mur = int( (proportion_wall * (size_map[0]*size_map[1])) /100 )        # On fait un produit en croix pour obtenir le nombre de murs (avec int pour que ce soit un entier)
    
    for _ in range(nb_mur):                                                     # genere les murs
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)        
        while m[a][b]!=0:                                                       # Tant que les coordonnées ne se situent pas dans un espace libre(évite la superposition des murs)
        
            a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
        m[a][b]=1                                                              # On créé le mur en modifiant la valeur de la matrice
    
    
    
    a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)           # genere l entree
    while m[a][b]!=0:                                                           # Tant que les coordonnées ne se situent pas dans un espace libre(évite la superposition)
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    m[a][b]=2
    
    a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)           # genere sortie
    while m[a][b]!=0:                                                            # Tant que les coordonnées ne se situent pas dans un espace libre(évite la superposition)
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    m[a][b]=3
    
    a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)  # genere cle
    while m[a][b]!=0:                                                  # Tant que les coordonnées ne se situent pas dans un espace libre(évite la superposition)
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
    m[a][b]=4
    return m


## 3.1  - 3.2
def delete_all_walls(m,pos):                # Supprime les murs adjacents à la position du personnage
    
    if pos[0]-1>=0:                       # Evite de faire une suppresion de murs en sortie de carte [°,0,1,1,1,0]
        if m[pos[0]-1] [pos[1]]==1:        # On verifie si la coordonnée est bien un mur 
            m[pos[0]-1] [pos[1]]=0         # On transforme le mur en un espace libre
    
    if pos[0]+1<len(m[0]):                # Evite de faire une erreur 
        if m[pos[0]+1] [pos[1]]==1:
            m[pos[0]+1] [pos[1]]=0
    
    if pos[1]-1>=0:
        if m[pos[0]][pos[1]-1]==1:
            m[pos[0]] [pos[1]-1]=0
    
    if pos[1]+1<len(m):
        if m[pos[0]] [pos[1]+1]==1:
            m[pos[0]] [pos[1]+1]=0
        
        
def updat_p2(letter,m):                        # Prend l'entrée de l'utilisateur sur l'action qu'il souhaite faire
    # print(len(m), len(m[0]))
    # print(p["x"] ,p["y"])
    if letter=="z" and not (p["x"] -1<0  or m[p["x"] -1][p["y"]]==1 ):         # le personnage monte(contrainte du mur/sortie de carte)
        p["x"]= p["x"] -1
        
    elif letter=="s" and not (p["x"] +1>=len(m) or m[p["x"] +1][p["y"]]==1): # le personnage descend
        p["x"]= p["x"] +1
        
        
    elif letter=="d" and not (p["y"] +1>=len(m[0]) or m[p["x"]][p["y"]+1]==1): # le personnage va a droite
        p["y"]= p["y"]+1
        
    elif letter=="q" and not (p["y"] -1<0 or m[p["x"]][p["y"]-1]==1):             # le personnage va a gauche
        p["y"]= p["y"]-1
    elif letter=="e":
        delete_all_walls(m, (p["x"],p["y"]))
        
        
    
   
# 3.4 

 
def create_objects(nb_objects,m):       # cree les objets 
    r=set()
    for i in range(nb_objects):
        
        a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)    
        #print(a,b , m[a][b]!=0 or (a==p["x"] and b==p["y"]),'1er' )
        while m[a][b]!=0 or (a==p["x"] and b==p["y"]) or (a,b) in r:     # si la coordonné est un espace libre, ne se superpose pas avec le personnage et les autres objets
         #   print(a,b , m[a][b]!=0 and not (a==p["x"] and b==p["y"]) )
            a,b = random.randint(0, len(m)-1), random.randint(0, len(m[0])-1)
        r.add((a,b)) # on ajoute l'objet a l'ensemble
    #print(len(r))
    return r




    

def display_map_char_and_objects_key(m,d,p,o): #Affiche la carte 
    for i in range(len(m)):
        for j in range(len(m[i])):      
        
            if i==p["x"] and j==p["y"]:        # le personnage
                print(p["char"],end="")
                
            elif (i,j) in o:                    #les objets
                print('€',end="")
                
        # print('indice',i,j)
            else :                                # le reste
                for c,v in d.items():
                #print(m[i][j])
                    if c==m[i][j]:
                        if c==3:                    # la coordonée est la sortie 
                            if key!=None:            # Si on a pas encore recuperer la clé
                                print(' ',end='')    #La sortie n'est pas affichée
                            else:
                                print(v,end='')      # Sinon la sortie est affichée
                        else:
                            print(v , end="") #Si c'est un autre objetn, on l'affiche
                        
    #                 print(m)
    
            #print(m[i][j],end="")
        print("")
    print("")
    print("Votre score est de " + str(p["score"]))
    # print(m)
    return ''
   
#### 3.5

def update_objects_key(p,obj, key):            # Recuperation objet 
    if (p["x"],p["y"]) in obj:        # recuperation points 
        obj.remove((p["x"],p["y"]))
        p["score"]+=1
    elif (p["x"],p["y"]) == key:        # recuperation clé
        m[p["x"]][p["y"]]=0
        key=None
    return key
        

def create_new_level(p,obj,nb_obj,size_map,proportion_wall):     # Creation nouveau niveau
    m=generate_random_map(size_map, proportion_wall)
    #print(obj , len(obj))
    for i in range(size_map[0]):
        for j in range(size_map[1]):        # change coordonee perso / point d apparition
            if m[i][j]==2:
                p["x"],p["y"] = i,j
            if m[i][j]==3:                  # Pour comparer les coordonnees perso avec coordonnee sortie
                sortie=(i,j)
    nb_obj+=1                            # on augmente le nombre d'objet a chaque niveau
    obj = create_objects(nb_obj, m)
    return m,obj,sortie
    

     
d = {0:' ',1:'#',2:" ",3:"֎",4:"Ꙉ"}
size_map=(7,7)
proportion_wall=0.25

m = generate_random_map(size_map,proportion_wall)

for i in range((size_map[0])):             # Instancie les premieres variable du niveau 1 
    for j in range((size_map[1])):
        if m[i][j]==2:
            p = create_perso((i,j))
        if m[i][j]==3:
            sortie=(i,j)
        if m[i][j]==4:                      
            key =(i,j)

nb_obj=5
obj = create_objects(nb_obj, m) 
#print(obj)
   
print(display_map_char_and_objects_key(m, d, p, obj))



start_time = time.perf_counter()            # pour gérer la contrainte du temps, on crée des variables qui serviront a faire un chronomètre
timer_base=25
end_time = time.perf_counter()
execution_time = timer_base-(end_time - start_time)

while execution_time>=0:            # Si le temps n'est pas encore écoulé 
    
    end_time = time.perf_counter()    
    execution_time = timer_base-(end_time - start_time)
    print("")
    if execution_time<0:
        break
    print(f"Attention, il vous reste : {execution_time: .2f} secondes pour sortir !!!")
    
    a = input("Entrer direction  : ")
    print("")
    
    
    
    updat_p2(a,m)
    key= update_objects_key(p, obj,key)
    
    if (p["x"],p["y"])==sortie and key==None:
        
            print("")
            print("Vous avez atteint la sortie")
            print("Niveau suivant en cours de chargement")
            for _ in range(6):
                print("...")                
                time.sleep(0.4)
            print("")
            proportion_wall+=0.025
            m,obj,sortie = create_new_level(p,obj,nb_obj,size_map,proportion_wall)
            
            start_time = time.perf_counter()
            timer_base-=2
            
            
    #print(m)
    
    for i in range((size_map[0])):             # evite que le perso commence dans un mur
        for j in range((size_map[1])):
            if m[i][j]==4:
                key =(i,j)
    display_map_char_and_objects_key(m, d, p, obj) 

print("")
print("Vous ne vous êtes pas échappé à temps")
print("Votre score final est de " + str(p["score"]))
print("")
print("")
print("Game over")
    
    

     


