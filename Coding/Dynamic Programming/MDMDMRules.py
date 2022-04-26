#the function is called recursively twice once for 0 and 1
#root to leaf traversal. values are passed to the leaf and are printed at the leaf
# time complexity is O(2^n)
import time
#from memory_profiler import profile

def bin_recursive(n,answer):
        if(n==0):
            print(answer)
        else:
            bin_recursive(n-1, answer+"0")
            bin_recursive(n-1, answer+"1")

#bin_recursive(20,"")


# each recursive call returns 2 sets of value which is combined to be one before returning.
#leaf to root traversal -  backwards

def bin_recursive(n):
        if(n==1):
            return ["0","1"]
        else:
            bitlist = bin_recursive(n-1) # calulate values for n-1
            bitlist_n =  ["0" + bit for bit in bitlist] + ["1" + bit for bit in bitlist]
            return bitlist_n

#print(bin_recursive(15))



def bin_recursive_memo(n,memo={}):
        if(n in memo): return memo[n]
        if(n==1):
            memo[n] = ["0","1"]
            return ["0","1"]
        else:
            bitlist = bin_recursive_memo(n-1,memo) # calulate values for n-1
            bitlist_n =  ["0" + bit for bit in bitlist] + ["1" + bit for bit in bitlist]
            memo[n] = bitlist_n
            #print(memo)
            return bitlist_n
        
start_time = time.time()
print(bin_recursive_memo(6,{}))
print("time taken: " + str(time.time() - start_time))