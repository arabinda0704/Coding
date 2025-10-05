class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # (cost, current_city, stops)
        heap = [(0, src, 0)]
        
        # track best cost for (city, stops)
        best = {(src, 0): 0}
        
        while heap:
            cost, city, stops = heapq.heappop(heap)
            
            # Reached destination
            if city == dst:
                return cost
            
            # If we can still make stops
            if stops <= k:
                for nei, price in graph[city]:
                    new_cost = cost + price
                    # only push if it's cheaper than any previously found path to (nei, stops+1)
                    if best.get((nei, stops + 1), float('inf')) > new_cost:
                        best[(nei, stops + 1)] = new_cost
                        heapq.heappush(heap, (new_cost, nei, stops + 1))
        
        return -1
        