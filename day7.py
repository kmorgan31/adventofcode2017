def day7(filename):
    ans = 0
    weight_map = dict()
    parent_children_map = dict()
    total = set()
    all_children = set()
    
    with open(filename, 'r') as f:
        for line in f:
            line = list(line.replace(',','').strip().split())
            root = line[0]

            # get weight of all nodes
            weight = int(line[1].replace('(','').replace(')',''))
            weight_map[root] = weight

            # get children of all parents
            children = line[3:]
            parent_children_map[root] = children

            # add root to seen nodes
            total.add(root)

            # add children to seen children
            for child in children:
                all_children.add(child)

    ans = (total - all_children).pop()
    print ans # part 1

    def calc_children_weights(root):
        children_weights = []
        for child in parent_children_map[root]:
            children_weights.append(calc_weight(child))
        return children_weights

    def check_bal(root):
        if parent_children_map[root]== []:
            return True
        children_weights = calc_children_weights(root)
        return len(set(children_weights)) == 1

    def unbalanced_child(root):
        children_weights = calc_children_weights(root)
        for child in parent_children_map[root]:
            curr_weight = calc_weight(child)
            if children_weights.count(curr_weight) == 1:
                return child

    def calc_weight(root):
        tot = weight_map[root]
        for child in parent_children_map[root]:
            tot += calc_weight(child)
        return tot


    # get weight needed to balance tree
    ans_parent = ans # make root the parent
    while not check_bal(ans):
        ans_parent = ans
        ans = unbalanced_child(ans)
    another_kid = parent_children_map[ans_parent][0]
    if another_kid == ans:
        another_kid = parent_children_map[ans_parent][1]
    print weight_map[ans] - calc_weight(ans) + calc_weight(another_kid)
