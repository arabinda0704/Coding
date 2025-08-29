class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        l = []
        
        # Up to Down (Vertical)
        for i in range(king[0] + 1, 8):
            if [i, king[1]] in queens:
                l.append([i, king[1]])
                break
        
        # Down to Up (Vertical)
        for i in range(king[0] - 1, -1, -1):
            if [i, king[1]] in queens:
                l.append([i, king[1]])
                break
                
        # Left to Right (Horizontal)
        for i in range(king[1] + 1, 8):
            if [king[0], i] in queens:
                l.append([king[0], i])
                break
                
        # Right to Left (Horizontal)
        for i in range(king[1] - 1, -1, -1):
            if [king[0], i] in queens:
                l.append([king[0], i])
                break

        # ==================================
        #  FOUR DIAGONAL CHECKS
        # ==================================
        
        # Diagonal: Up-Right
        i, j = king[0] + 1, king[1] + 1
        while i < 8 and j < 8:
            if [i, j] in queens:
                l.append([i, j])
                break
            i += 1
            j += 1
        
        # Diagonal: Up-Left
        i, j = king[0] + 1, king[1] - 1
        while i < 8 and j >= 0:
            if [i, j] in queens:
                l.append([i, j])
                break
            i += 1
            j -= 1

        # Diagonal: Down-Right
        i, j = king[0] - 1, king[1] + 1
        while i >= 0 and j < 8:
            if [i, j] in queens:
                l.append([i, j])
                break
            i -= 1
            j += 1
            
        # Diagonal: Down-Left
        i, j = king[0] - 1, king[1] - 1
        while i >= 0 and j >= 0:
            if [i, j] in queens:
                l.append([i, j])
                break
            i -= 1
            j -= 1
        
        return l