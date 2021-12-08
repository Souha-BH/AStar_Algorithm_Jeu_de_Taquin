EtatInitial = [7,2,4,5,0,6,8,3,1]
EtatFinal = [0,1,2,3,4,5,6,7,8]
Voisins = [
                    [1,3],
                    [0,2,4],
                    [1,5],
                    [0,4,6],
                    [1,3,5,7],
                    [2,4,8],
                    [3,7],
                    [4,6,8],
                    [5,7],
                  ]
def PossibleResults(Etat):
        Branches=[]
        for index in range(0,9) :
          

          LVoisins = Voisins[index]

          for v in LVoisins:
             
            if(Etat[v] == 0):
                
                Branch=Etat.copy()
                Branch[v]=Branch[index]
                Branch[index]=0
                Branches.append(Branch)
                 
        return(Branches)    
def heuristique_1(Etat):
    n=0
    for i in range(9):
        if (Etat[i] != i  and Etat[i]!=0):
            n+=1
    return n
        
def heuristique_2(Etat):
    n=0
    for i in range(9):
        if Etat[i]!=0:
            n+=abs(int(i / 3 )-int(Etat[i]/3))+ abs(i %3 - Etat[i]%3)
    return n

def is_goal(Etat):
    if Etat==EtatFinal:
        return True 
    else:
        return False




    
class List():
    def __init__(self,parent=None,ListValues=EtatInitial):
        self.parent=parent
        self.ListValues=ListValues
        self.g=0
        self.h=0
        self.f=0
    
 
def AStar(start,goal,heuristiqueFunc):
    
    start_list=List(None,start)
    start_list.g=0
    start_list.h=heuristiqueFunc(start_list.ListValues)
    print(start_list.h)
    start_list.f=start_list.h + start_list.g
    end_list=List(None,goal)
    end_list.g=end_list.h=end_list.f=0
    
    open_list=[]
    closed_list=[]
    
    open_list.append(start_list)
    
    while (len(open_list)>0):
        current_list=open_list[0]
        current_index=0
        
        for index,item in enumerate(open_list):
            if item.f <current_list.f:
                current_list=item
                current_index=index

        open_list.pop(current_index)
        closed_list.append(current_list)
        
        if is_goal(current_list.ListValues):
            path=[]
            current=current_list
            while current is not None:
                path.append(current.ListValues)
                current=current.parent
            return path[::-1]
        
        for child in PossibleResults(current_list.ListValues):
            isChildInClosed = False
            child_list=List(current_list,child)
            for closed_child in closed_list:
                if child_list.ListValues == closed_child.ListValues:
                    isChildInClosed = True
                    break
            if isChildInClosed == False:
                child_list.g=current_list.g +1
                child_list.h=heuristiqueFunc(child)
                child_list.f=child_list.g + child_list.h
                
                # for open_child in open_list:
                #     if child_list.ListValues == open_child.ListValues and child_list.g>open_child.g:
                #         continue
                open_list.append(child_list)

def printNode(node):
    i = 0
    while i < 9:
        print(node[i:i+3])
        print('\n')
        i += 3

def printPath(path):
    for node in path:
        print("---------------- NODE -----------------------")
        printNode(node)
        print("---------------------------------------------")  
    return(len(path))  

length2 = printPath(AStar(EtatInitial,EtatFinal,heuristique_2));
length1 = printPath(AStar(EtatInitial,EtatFinal,heuristique_1));

print(length1)

print(length2)
diff= length1 - length2
print(diff)
if diff<0:
    print("heuristique 1 is better")
else:
    print("heuristique 2 is better")