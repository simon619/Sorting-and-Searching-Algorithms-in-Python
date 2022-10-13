class Node:
    def __init__(self, data):
        self.data = data
        self.adj = []


class TopologicalSort:

    def __init__(self):
        self.index_recorder = {}

    def dfs(self, current_node, visited, visited_nodes, node_list):
        visited[self.index_recorder[current_node]] = True
        for edge in current_node.adj:
            if not visited[self.index_recorder[edge]]:
                visited_nodes = self.dfs(edge, visited, visited_nodes, node_list)
        visited_nodes.append(current_node)
        return visited_nodes

    def topo_sort(self, node_list):
        number_of_nodes = len(node_list)
        visited = [False] * number_of_nodes
        for n in range(len(node_list)):
            self.index_recorder[node_list[n]] = n
        order = [0] * number_of_nodes
        pointer = number_of_nodes - 1
        for n in range(number_of_nodes):
            if not visited[n]:
                visited_nodes = []
                visited_nodes = self.dfs(node_list[n], visited, visited_nodes, node_list)
                for node_id in visited_nodes:
                    order[pointer] = node_id.data
                    pointer -= 1
        return order


if __name__ == '__main__':
    graph = {'A': ['D'], 'B': ['D'], 'C': ['A', 'B'], 'D': ['H', 'G'], 'E': ['A', 'D', 'F'], 'F': ['K', 'J'],
             'G': ['I'], 'H': ['I', 'J'], 'I': ['L'], 'J': ['L', 'M'], 'K': ['J'], 'L': [], 'M': []}
    node_list, node_dic = [], {}
    for node in graph:
        new_node = Node(node)
        node_list.append(new_node)
        node_dic[node] = new_node
    for key, val in graph.items():
        node_dic[key].adj = [node_dic[ad] for ad in val]
    obj = TopologicalSort()
    sorted_order = obj.topo_sort(node_list)
    print(f'Topologically Sorted: {sorted_order}')
