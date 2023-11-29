# tee ratkaisu tänne
def uniikit(listaus):
    
    uniikit=[]
    foundduplicate=False

    for i in range(0,len(listaus)):
        
        foundduplicate=False

        for j in range(0,len(uniikit)):
            if uniikit[j]==listaus[i]:
                foundduplicate=True
                break
        
        if foundduplicate==False:
            uniikit.append(listaus[i])
            
    uniikit.sort()
    return uniikit

if __name__ == "__main__":
    
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista)) # [1, 2, 3]