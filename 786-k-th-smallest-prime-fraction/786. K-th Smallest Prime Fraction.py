class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        heap = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                heapq.heappush(heap,(arr[i]/arr[j],(i,j)))
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        frac,(i,j) = heapq.heappop(heap)
        if (i,j):
            return [arr[i],arr[j]]
        return []
        