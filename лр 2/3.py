def is_prime(number):
    k=0
    for i in range(1, int(number**0.5)+1):
        if number%i==0: k+=2
    if k==2: return True
    else: return False
            
