


def create_perso(depart):
    #print (depart[0])
    return {"char" : "o", "x" : depart[0], "y" : depart[1]}

#print(create_perso((0,0)))


d = {0:' ',1:'#'}

m =   [[0,0,0,1,1],
       [0,0,0,0,1],
       [1,1,0,0,0],
       [0,0,0,0,0]]

p = create_perso((0,0))

def display_map_and_char(m,d,p):
    m [p["x"]][p["y"]]=p["char"]
    for i in range(len(m)):
        for j in range(len(m[i])):      # Si on veut faire une carte pas en carre (rectangle, autres...)
        
            if i==p["x"] and j=="y":
                print(m[i][i],end="")
        
        # print('indice',i,j)
            for c,v in d.items():
                #print(m[i][j])
                if c==m[i][j]:                   
                    print(v , end="")
    #                 print(m)
    
            #print(m[i][j],end="")
        print("")
        

print(display_map_and_char(m, d, p))





def updat_p(letter):
    if letter=="z":
        p["x"]= p["x"] -1
    elif letter=="s":
        p["x"]= p["x"] +1
        
    elif letter=="d":
        p["y"]= p["y"]+1
    else:
        p["y"]= p["y"]-1
    
a = input("Entrer direction  : ")
updat_p(a)

display_map_and_char(m, d, p)
















