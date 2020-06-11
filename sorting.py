import math

class sortArray:
    def __init__(self, Arr):
        self.arr = Arr
    
    @staticmethod
    def swap(A, i, j):
        """Function takes an array and positions which needs to 
        swap returns the array after swaping"""
        A[i], A[j] = A[j], A[i]
        return A
    
    # heap sort starts here
    
    def max_heapify(self, i, heap_size):
        """it takes the position of the element where you
        apply the max_heapify function, and the heap size"""
        l = 2*i+1
        r = 2*i+2
        if l < heap_size and self.arr[l] > self.arr[i]:
            maximum = l
        else:
            maximum = i
        if r < heap_size and self.arr[r] > self.arr[maximum]:
            maximum = r
        if maximum != i:
            self.swap(self.arr, i, maximum)
            self.max_heapify(maximum, heap_size)
        return self.arr
    
    def heapify(self, heap_size):
        """ heapify function takes the heap size """
        i = math.floor(heap_size/2) - 1
        while i >= 0:
            self.max_heapify(i, heap_size)
            i-=1
        return self.arr
    
    def heapsort(self):
        """Sort the object"""
        heap_size = len(self.arr)
        while heap_size > 1:
            self.heapify(heap_size)
            self.swap(self.arr, 0, heap_size-1)
            heap_size -= 1
        return self.arr
    
    # Insersion Sort starts here
    
    def partialInsersionSort(self, l):
        """Takes the already sorted list and 
        insert the next element on right spot"""
        key = self.arr[l]
        j = l-1
        while j > -1:
            if self.arr[j] > key:
                self.arr[j+1] = self.arr[j]
            else:
                self.arr[j+1] = key
                break
            j-=1
        else:
            self.arr[0] = key
        return self.arr
    
    def insersionSort(self):
        j = 1
        while j < len(self.arr):
            self.partialInsersionSort(j)
            j+=1
        return self.arr

    # Merge sort starts from here
    
    def merge(self, p, q, r):
        """It merges the already sorted lists first list starting from index p 
        to q and second starting from q+1 to r"""
        n1 = q-p+1 
        n2 = r-q
        L=[]
        R=[]
        for i in range(n1):
            L.append(self.arr[p+i])
        for j in range(n2):
            R.append(self.arr[q+j+1])
        L.append(math.exp(100))
        R.append(math.exp(100))
        l = 0
        m = 0
        for k in range(p, r+1):
            if L[l] > R[m]:
                self.arr[k] = R[m]
                m+=1
            else:
                self.arr[k] = L[l]
                l+=1
        return self.arr
    
    def mergeSort(self, p, r):
        """sortd the list using merge method recursively"""
        if p < r:
            q = math.floor((p+r)/2)
            self.mergeSort(p, q)
            self.mergeSort(q+1, r)
            self.merge(p, q, r)
        return self.arr
    
    # bubble sort starts from here
    
    def bubbleSort(self):
        k = len(self.arr)-1
        while k>0:
            i = k
            while i > 0:
                if self.arr[i-1] > self.arr[i]:
                    self.swap(self.arr, i-1, i)
                i-=1
            k-=1
        return self.arr
    
    # Quick sort starts here
    
    def partition(self, p, q):
        # i identifiies till which index everything is less than pivot
        pivot = self.arr[q]
        i = p-1
        for j in range(p, q):
            if self.arr[j] <= pivot:
                i+=1
                self.swap(self.arr, i, j)
        self.swap(self.arr, i+1, q)
        return i+1
    
    def quickSort(self, p, r):
        if p<r:
            q = self.partition(p, r)
            self.quickSort(p, q-1)
            self.quickSort(q+1, r)
        return self.arr
    
    
        
            
        
    
            
        
            
        
        