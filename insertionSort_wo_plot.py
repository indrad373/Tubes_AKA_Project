from numpy import random
import random
import time
start_time = time.time()
 
def insertionSort(arr): 

	#loop melalui 1 hingga len(arr) 
	for i in range(1, len(arr)): 

		key = arr[i] 

		j = i-1
		while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
		arr[j+1] = key 


# random array range 10 dimulai dari 0
arr = random.sample(range(10), 10) 
insertionSort(arr)
print("--- %s seconds ---" % (time.time() - start_time))
