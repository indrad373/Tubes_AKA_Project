from numpy import random
import random
import time
start_time = time.time()
def merge(arr, l, m, r): 
	n1 = m - l + 1
	n2 = r- m 

	# buat temp arrays 
	L = [0] * (n1) 
	R = [0] * (n2) 

	# Copy data ke temp arrays L[] dan R[] 
	for i in range(0 , n1): 
		L[i] = arr[l + i] 

	for j in range(0 , n2): 
		R[j] = arr[m + 1 + j] 

	# Merge temp arrays kembali ke arr[l..r] 
	i = 0	 # Initial index dari subarray pertama
	j = 0	 # Initial index dari subarray kedua 
	k = l	 # Initial index dari subarray ketiga

	while i < n1 and j < n2 : 
		if L[i] <= R[j]: 
			arr[k] = L[i] 
			i += 1
		else: 
			arr[k] = R[j] 
			j += 1
		k += 1

	# Copy element tersisa dari L[], jika ada 
	while i < n1: 
		arr[k] = L[i] 
		i += 1
		k += 1

	# Copy element tersisa dari R[], jika ada 
	while j < n2: 
		arr[k] = R[j] 
		j += 1
		k += 1

# l adalah untuk left index dan r adalah right index untuk 
# sub-array dari arr yang akan diurutkan 
def mergeSort(arr,l,r): 
	if l < r: 

		m = (l+(r-1))//2

		mergeSort(arr, l, m) 
		mergeSort(arr, m+1, r) 
		merge(arr, l, m, r) 

#random array dengan range 100
arr = random.sample(range(100), 100)
n = len(arr)

mergeSort(arr,0,n-1) 

print("--- %s seconds ---" % (time.time() - start_time))
