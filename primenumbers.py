import time
def my_prime_numbers(n):
	"""Fucnction to display prime numbers between zero and any random number n"""
    start = time.time()
    li=list()
    if type(n) is int:
    	for i in range(0,n+1):
        	if i>1:
            	for j in range(2,i):
                	if (i % j) == 0:
                    	break
                	else:
            
           	    		li.append(i)
    		elif i=1 or i=0: raise ValueError, "only integers allowed"
    		else: raise ValueError, "only positive values"
    	end =time.time()
    	return li,end-start
 