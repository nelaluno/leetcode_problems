class Solution:    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # spiral = [0] (len(matrix) * (len(matrix[0]) if )
        spiral = []
        m = len(matrix)
        n = len(matrix[0])
        m_min, m_max = 0, m-1
        n_min, n_max = 0, n-1
        while m_min <= m_max and n_min <= n_max:
            spiral.extend(matrix[m_min][n_min:n_max+1])
            m_min += 1
            if m_min > m_max:
                break
            
            for m in matrix[m_min:m_max+1]:
                spiral.append(m[n_max])
            n_max -= 1
            if n_min > n_max:
                break
            
            spiral.extend(matrix[m_max][n_min:n_max+1][::-1])
            m_max -= 1
            if m_min > m_max:
                break
            
            for m in matrix[m_min:m_max+1][::-1]:
                spiral.append(m[n_min])
            n_min += 1
            if n_min > n_max:
                break
        return spiral
