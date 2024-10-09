# Rylee, Liz




def total(n):
    total = 0
    for step in range (1, n):
        if n % step == 0:
            total = total + step
    return total

def perfect():
    n = int(input("give me a number \n"))
    summ = total(n)
    if summ == n:
        return  True
    else:
        return False


print(perfect())
        
            
