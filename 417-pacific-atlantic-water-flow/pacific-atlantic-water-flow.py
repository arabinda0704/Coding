class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prev_height):
            # Out of bounds or invalid
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                (r, c) in visited or 
                heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        # Start DFS from Pacific and Atlantic borders
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])           # Top edge (Pacific)
            dfs(rows - 1, c, atlantic, heights[rows-1][c])  # Bottom edge (Atlantic)
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])           # Left edge (Pacific)
            dfs(r, cols - 1, atlantic, heights[r][cols-1])  # Right edge (Atlantic)
        
        # Intersection: cells that reach both oceans
        result = list(pacific & atlantic)
        
        return result