import numpy as np
import math

#####avg magnetization############

def avg_mag(A):
  return np.sum(A)/A.size
  
######get neighbors of (i, j)#####

def nbrs(A, i, j):
  N = len(A)
  return [A[i][(j+1)%N], A[i][(j-1)%N], A[(i+1)%N][j], A[(i-1)%N][j]]
  
#######interaction terms##########

def int_term(A):
  N = len(A)
  total = 0
  for i in range(N):
    for j in range(N):
      total = total - A[i][j]*np.sum(nbrs(A, i, j))
  
  return total
  
