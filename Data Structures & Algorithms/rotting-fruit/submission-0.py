class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        fresh = 0

        def addCell(r, c):
            if (r < 0 or r == rows or
            c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visit):
                return False

            q.append([r, c])
            visit.add((r, c))
            return True

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        minute = 0
    
        while q:
            rottedThisRound = False
            for i in range(len(q)):
                r, c = q.popleft()

                for neiRow, neiCol in ((r + 1, c), (r - 1 , c), (r, c - 1), (r, c + 1)):
                    if addCell(neiRow, neiCol):
                        fresh -= 1
                        rottedThisRound = True
                    
            if rottedThisRound:
                minute += 1
        
        return minute if fresh == 0 else -1

                
        



        