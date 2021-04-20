import collections 
import multiprocessing
import random
import time
import numpy as np
# def process_item(item):
#      return {'name': item.name, 'age': 2017 - item.born   }


# Scientist = collections.namedtuple('Scientist', [   'name',   'born',])

# scientists = (Scientist(name='Ada Lovelace', born=1815),
#                     Scientist(name='Emmy Noether', born=1882),
#                     Scientist(name='Marie Curie', born=1867),
#                     Scientist(name='Tu Youyou', born=1930),
#                     Scientist(name='Ada Yonath', born=1939),
#                     Scientist(name='Vera Rubin', born=1928),
#                     Scientist(name='Sally Ride', born=1951),)

# pool = multiprocessing.Pool()
# result = pool.map(process_item, scientists)

# def matrix_multiplier(A, B_transposed):
# 	out=[]
# 	len_minimal=min(len(A), len(B))
# 	for i in range(len(A)):
# 		out.append([])
# 		for k in range(len(B_transposed)):
# 			out[i].append(row_column_multiplier(A[i], B_transposed[k])*8+3)
# 	return out

def row_column_multiplier(row, column):
	len_minimal=min(len(row), len(column))
	summ=0
	for i in range(len_minimal):
		summ+=row[i]*column[i]
	return summ*8+3

A, B, C=[], [], []
result, B_transposed = [], []
for i in range(5*10**2):
	A.append([])
	B.append([])
	for k in range(5*10**2):
		A[i].append(random.randint(0,10))
		B[i].append(random.randint(0,10))
# print(A, "A")
# print(B, "B")

###########################################	SINGLE MODE
# start_time = time.time()
# for i in range(len(A)):		#Transpose B
# 	B_transposed.append([])
# 	for k in range(len(A)):
# 		B_transposed[i].append(B[k][i])

# for i in range(len(A)):
# 	C.append([])
# 	for k in range(len(B_transposed)):
# 		C[i].append(row_column_multiplier(A[i], B_transposed[k]))

# # print(C, "SP_mode")
# method_SP_time = time.time() - start_time
# print("--- %s seconds without multiprocessing---" % (method_SP_time))
###########################################
for i in range(10):
	num_processes=i+1
	###########################################	MULTIPROCCESS MODE
	stage1=time.time()
	# pool = multiprocessing.Pool()
	with multiprocessing.Pool(processes=num_processes) as pool:
		B_transposed=list(map(list, zip(*B)))	#Transpose B
		for i in range(len(A)):
			# zip_list = zip(A, cycle(B_transposed)) if len(A[i]) > len(B_transposed) else zip(cycle(A), B_transposed)
			# print(list(zip_list))
			# (A[i],A[i])*(2-len(B_transposed)), B_transposed)
			A_doubled=[A[i]]*len(B_transposed)
			# print(A_doubled)
			result.append(pool.starmap(row_column_multiplier,zip(A_doubled, B_transposed)))

	# print(result, 'MP_mode')
	method_MP_time = time.time() - stage1
	print("--- %s seconds with multiprocessing---" % (method_MP_time), num_processes, ' processes')
	###########################################

print('\n Time difference: ', method_SP_time - method_MP_time)