class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        
        queue = deque([("0000", 0)])
        visited = {"0000"}
        
        while queue:
            state, steps = queue.popleft()
            
            # Found target
            if state == target:
                return steps
            
            # Skip if deadend
            if state in dead:
                continue
            
            # Explore neighbors (each wheel +1 and -1)
            for i in range(4):
                digit = int(state[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    
                    if new_state not in visited and new_state not in dead:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))
        
        return -1