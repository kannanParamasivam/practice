from typing import List


class Solution:


    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.colored_nodes = {}
        
        for node in range(len(graph)):
            if node not in self.colored_nodes:
                if not self.dfs(graph, node):
                    return False
        
        return True

    
    def dfs(self, graph, root):
        color = 1
        stack = []
        
        self.colored_nodes[root] = color
        stack.append(root)
    
        while len(stack) > 0:
        
            node = stack.pop()
            
            for nei in graph[node]:
                if nei not in self.colored_nodes:
                    self.colored_nodes[nei] = self.colored_nodes[node]^1
                    stack.append(nei)
                elif self.colored_nodes[nei] == self.colored_nodes[node]:
                    return False
            
        return True


# graph = [[1,3], [0,2], [1,3], [0,2]]
# graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
graph = [[],[3],[],[1],[]]
sol = Solution()
print(sol.isBipartite(graph))        
        
        
        
    
    
    
    
    
