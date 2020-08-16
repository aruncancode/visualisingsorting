class Sorting:

    def bubbleSort(self, ar):
        n = len(ar)
        for i in range(n):
            for j in range(0, n-i-1):
                if ar[j] > ar[j+1] :
                    ar[j], ar[j+1] = ar[j+1], ar[j]