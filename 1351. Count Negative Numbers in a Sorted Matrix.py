class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n_bound = len(grid[0])
        m_bound = len(grid)

        i = 0
        j = 0

        count = 0

        while i < m_bound:
            while j < n_bound:
                if grid[i][j] < 0:
                    count += (m_bound-i)*(n_bound-j)
                    n_bound = j
                j += 1
            i +=1
            j=0
        
        return count