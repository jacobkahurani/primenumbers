import time # import time module to asist in assymptotic analysis
def my_prime_numbers(n):#Define your function
	"""Fucnction to display prime numbers between zero and any random number n"""
    start = time.time()#Assignn variable to the value of run time
    li=list() #initialize a list called li
    if type(n) is int: #Check type of input is integer
    	for i in range(0,n+1): #iterate over range of n
        	if i>1: # Check if value of input is greater than 1
            	for j in range(2,i): #iterate over range of i
                	if (i % j) == 0:# perform check using moduli operation
                    	break #break from loop
                	else: 
            
           	    		li.append(i)#append to initialized list values of prime numbers
    		elif i=1 or i=0: raise ValueError, "only integers allowed" # Check that 0 and 1 not included as input.
    		else: raise ValueError, "only positive values" #Ensure input contains poitive values
    	end =time.time() #assign end variable to run time
    	return li,end-start #output list and time difference, ie time taken
 