def get_graph(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            lst = line.replace(',', '').split()
            graph[lst[0]] = lst[2:]
    return graph

def find_path(graph, start, end, path=None):
        """ find a path from start_vertex to end_vertex 
            in graph """
        if path == None:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                extended_path = find_path(graph, node, 
                                               end, 
                                               path)
                if extended_path: 
                    return extended_path
        return None

def find_group_count(graph, start):
    count = 0
    nodes = graph.keys()
    for node in nodes:
        if find_path(graph, start, node):
            count += 1
    return count

def find_group(graph, start):
    group = [start]
    nodes = graph.keys()
    for node in nodes:
        if find_path(graph, start, node):
            group += [node]
    return group
    

def day12(filename):
    graph = get_graph(filename)

    # part_one
    part_one = find_group_count(graph, '0')
    print part_one

    # part_two
    num_groups = 0
    nodes = set(graph.keys())
    while len(nodes) > 0:
        node = nodes.pop()
        group = find_group(graph, node)
        num_groups += 1
        nodes = nodes - set(group)
    print num_groups
        
    
 
            
    
            
