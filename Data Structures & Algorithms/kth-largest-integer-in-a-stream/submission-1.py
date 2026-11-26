class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)

        print(len(self.min_heap))

        # To maintain the k-th largest element in a stream of numbers, we do not need to store all values.
        # Instead, we only need to keep track of the k largest elements seen so far,
        # thus satisfying the KthLargest constraint on initiatlization.
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
    

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            # Pop the smallest item from the min-heap to
            # ensure we stay within the size k for the heap.
            heapq.heappop(self.min_heap)

        print(self.min_heap)

        # Since we are using a min-heap, and min_heap only store up to k number
        # of elements, the very first element will be the KthLargest.
        return self.min_heap[0]
