# Diagonal matrix
import numpy as np

def square_matrix():
	
	import sys
	n = int(input("Dimension of matrix:\t"))
	matrix = []
	
	# Warning Message/ Guide
	try:
		print("You will be asked the matrix input in the terminal. You just have to upload each row in this format a<space>b<space>...z<space>. Where a, b ... z are the elements of a particular row.")
		if input("Enter y/n for yes or no: ").lower() == "y":
			pass
		else:
			sys.exit()
	except Exception as e:
		print(e)
	
	# matrix
	for i in range(n):
		row = list(map(float, input(f"{i}_th row: ").split()))
		matrix.append(row)
	return np.array(matrix)
	
def makeMEdiagonal(matrix=square_matrix):
	import sys
	# matrix
	a = matrix()
	
	# check for square matrix
	if len(a) == len(a.T):
		n = len(a)
	else:
		raise ValueError("Your matrix is not a square matrix")
		sys.quit()
	
	# singularity
	for i in range(n):
		if a[i][i] == 0:
			for j in range(i,n):
				if a[j][j] != 0:
					a[i] = a[j]
	
	
	# upper diagonal matrix
	for i in range(n):
		pivot = a[i][i]
		
		for j in range(i+1,n):
			a[j] += -(a[j][i]/pivot) * a[i] 

	return a



	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

if __name__ == "__main__":
	print(makeMEdiagonal())
