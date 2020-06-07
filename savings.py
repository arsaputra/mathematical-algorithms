def total_savings(starting_saving,yearly_savings,time,interest,year):
    L=[i for i in range(time+1)]
    L[0]=starting_saving
    t=0
    while t!=time:
        t+=1
        L[t]=L[t-1]*(1+interest/100)+yearly_savings
    return L[year]
    
# Assuming starting saving and yearly savings are equal

def find_initial_investment(total,time,interest,TOL):
    tolerance=float('inf')
    a,b=0,total
    while True:
        z=(a+b)/2
        res=total_savings(z,z,time,interest,time)
        tolerance=abs(total-res)
        if tolerance<=TOL and res>=total:
            break
        else:
            if res<total:
                a=z
                continue
            if res>total:
                b=z
                continue
    return int(z+1) 
                
                
        
# Runtime: O(log(total)*time)
    
    
