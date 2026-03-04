# scc_finder.py 
 
from collections import defaultdict 
 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = defaultdict(list) 
 
    def add_edge(self, u, v): 
        self.graph[u].append(v) 
 
    def fill_order(self, v, visited, stack): 
        visited[v] = True 
        for neighbour in self.graph[v]: 
            if not visited[neighbour]: 
                self.fill_order(neighbour, visited, stack) 
        stack.append(v) 
 
     
    def get_transpose(self): 
        g = Graph(self.V) 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.add_edge(j, i) 
        return g 
 
     
    def dfs(self, v, visited, component): 
        visited[v] = True 
        component.append(v) 
        for neighbour in self.graph[v]: 
            if not visited[neighbour]: 
                self.dfs(neighbour, visited, component) 
 
    def print_sccs(self): 
        stack = [] 
        visited = [False] * (self.V + 1) 
 
        for i in range(1, self.V + 1): 
            if not visited[i]: 
                self.fill_order(i, visited, stack) 
 
        gr = self.get_transpose() 
        visited = [False] * (self.V + 1) 
 
        scc_list = [] 
 
        while stack: 
            i = stack.pop() 
            if not visited[i]: 
                component = [] 
                gr.dfs(i, visited, component) 
                scc_list.append(component) 
 
        return scc_list 
 
 
def main(): 
    g = Graph(6) 
 
    g.add_edge(1, 3) 
    g.add_edge(1, 2) 
    g.add_edge(2, 4) 
    g.add_edge(3, 4) 
    g.add_edge(3, 5) 
    g.add_edge(4, 1) 
    g.add_edge(4, 6) 
    g.add_edge(5, 6) 
 
    sccs = g.print_sccs() 
 
    print("Strongly Connected Components:") 
    for scc in sccs: 
        print(set(scc)) 
    with open("scc_output.txt", "w") as f: 
        f.write("Strongly Connected Components (SCCs):\n\n") 
        for scc in sccs: 
            f.write(str(set(scc)) + "\n") 
            print("\nResults saved to scc_output.txt") 
            if __name__ == "__main__": 
                main() 