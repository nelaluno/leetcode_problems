from collections import defaultdict

class Solution:
    def dfs(self, node, isConnected, visit):
        visit[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visit[i]:
                self.dfs(i, isConnected, visit)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        for row in isConnected:
            print(row)
        
        n = len(isConnected)
        group_count = 0
        visit = [False] * n

        for i in range(n):
            if not visit[i]:
                group_count += 1
                self.dfs(i, isConnected, visit)
        return group_count


