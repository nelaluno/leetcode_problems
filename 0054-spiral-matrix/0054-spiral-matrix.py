class Solution:    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # spiral = [0] (len(matrix) * (len(matrix[0]) if )
        spiral = []
        m = len(matrix)
        n = len(matrix[0])
        m_min, m_max = 0, m-1
        n_min, n_max = 0, n-1
        while m_min <= m_max and n_min <= n_max:
            # print("round")
            # print(f"[{m_min}][{n_min}:{n_max+1}]")
            spiral.extend(matrix[m_min][n_min:n_max+1])
            # print(spiral)

            m_min += 1
            if m_min > m_max:
                break
            
            # print(f"[{m_min}:{m_max+1}][{n_max}]")
            for m in matrix[m_min:m_max+1]:
                spiral.append(m[n_max])
            # print(spiral)

            n_max -= 1
            if n_min > n_max:
                break

            # print(f"[{m_max}][{n_min}:{n_max+1}][::-1]")
            spiral.extend(matrix[m_max][n_min:n_max+1][::-1])
            # print(spiral)

            m_max -= 1
            if m_min > m_max:
                break
            
            # print(f"[{m_min}:{m_max+1}][::-1][{n_min}]")
            for m in matrix[m_min:m_max+1][::-1]:
                spiral.append(m[n_min])
            # print(spiral)
            
            n_min += 1
            # print((m_min, m_max), (n_min, n_max))
            if n_min > n_max:
                break
        return spiral
