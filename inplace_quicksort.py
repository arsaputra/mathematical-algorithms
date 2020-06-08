def quicksort(n,cmp,swp):
    """
    Sortiert eine Liste der Laenge n mithilfe der Funktionen cmp und swp

    @param  int       n      die Laenge der zu sortierten Liste 
    @param  funktion  cmp    die Funktion, die genau 2 Elementen einer Liste vergleicht
    @param  funktion  swp    die Funktion, die 2 Elemente einer Liste vertauscht
    @return int       1

    Wenn man nach dem Aufruf der Funktion quicksort die Liste aufruft, wird die
    Liste nun schon aufsteigend sortiert
    """
    miniquicksort(0,n-1,cmp,swp) #fuehrt miniquicksort auf die ganze Liste aus
    return 1

def miniquicksort(first,last,cmp,swp):
    """
    @param  int      first  der Index der ersten Element der betrachteten Liste
    @param  int      last   der Index der letzten Element der betrachteten Liste
    @param  funktion cmp    die Funktion, die genau 2 Elementen einer Liste vergleicht
    @param  funktion swp    die Funktion, die 2 Elemente einer Liste vertauscht
    @return 
    """
    if last-first>1: #wenn die Laenge der Liste >=3
        if (cmp(first+1,first)==True and cmp(first,first+2)==True)or(cmp(first+2,first)==True and cmp(first,first+1)==True):
            index_pivot=first
        if (cmp(first,first+1)==True and cmp(first+1,first+2)==True)or(cmp(first+2,first+1)==True and cmp(first+1,first)==True):
            index_pivot=first+1
        if (cmp(first,first+2)==True and cmp(first+2,first+1)==True)or(cmp(first+1,first+2)==True and cmp(first+2,first)==True):
            index_pivot=first+2
        swp(first,index_pivot) #Pivot wird im 0. Position gelegt
        left,right,x=first+1,last,10 #Zeiger
        while x<100:
            while left<=right and cmp(left,first)==True:  #Bewegung von linkem Zeiger
                left+=1
            while right>=left and cmp(first,right)==True: #Bewegung von rechtem Zeiger
                right-=1
            if right<left: #Schleife terminiert
                x=1000 
            else: #Schleife setzt fort, wiederhole oben
                swp(right,left)
        swp(first,right)
        miniquicksort(first,right-1,cmp,swp) #Rekursiv linke Seite der Liste
        miniquicksort(right+1,last,cmp,swp)  #Rekurdiv rechte Seite der Liste
    else:
        #wenn die Laenge der Liste <=2. Rekursionsanker
        if not cmp(first,last)==True:
            swp(first,last)
    

