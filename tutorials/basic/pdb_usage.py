from itertools import repeat
import pdb

def insertion_sort(A, p, r):

    for j in range(p+1, r+1):
        pdb.set_trace()
        key = A[j]
        i = j-1
        while i>=p and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    print A


if __name__ == "__main__":
    A = [1,24,7,34,6,64,34,56,3]
    insertion_sort(A, 1, 8)