class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Use a max-heap to sort the points by proximity to [0, 0].
        We'll then return the k closest / smallest points.

        To keep the K smallest distances, you need a way to quickly identify 
        and discard the farthest point among your current best candidates 
        whenever a closer point arrives.
        """     
        import heapq
        max_heap = []
        
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush_max(max_heap, [dist, x, y])
            if len(max_heap) > k:
                heapq.heappop_max(max_heap)

        res = []
        while max_heap:
            dist, x, y = heapq.heappop(max_heap)
            res.append([x, y])

        return res
