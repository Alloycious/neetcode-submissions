class Solution:
    import heapq

    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        We want to remove the two heaviest stones from the stones List
        at each step until one stone is remaining.
        """
        heapq.heapify_max(stones)

        while len(stones) > 1:
            largest = stones[0]
            s_largest = stones[1]

            if largest == s_largest:
                heapq.heappop_max(stones)
                heapq.heappop_max(stones)
            elif s_largest < largest:
                largest_stone = heapq.heappop_max(stones)
                
                # Pop second largest stone and restore largest_stone
                s_largest_stone = heapq.heappop_max(stones)

                largest_stone -= s_largest_stone
                heapq.heappush_max(stones, largest_stone)
            else:
                continue

        return stones[0] if stones else 0
