class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS queue
        # q = deque([source])
        # visited = set([source])
        
        # while q:
        #     node = q.popleft()
        #     if node == destination:
        #         return True
        #     for nei in graph[node]:
        #         if nei not in visited:
        #             visited.add(nei)
        #             q.append(nei)
        
        # return False
        #DFS
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited and dfs(nei):
                    return True
            return False
        
        return dfs(source)
        