# -*- coding: utf-8 -*-


def find_neighbors(degree_sep, node):
    """
    find a nodes neighbors to n degrees of seperation.
    ------------
    params - degree_sep: degrees of seperation. integer > 1
             node: node id
    ------------
    return - a set of neighbors to the nth degree with no 'NoneType'
    """
    neighbors = set([])
    newset = set([])

    # update a set for neighbors iteration.
    # updat direct neighbors into the neighbors list
    newset.update(node.neighbors)
    neighbors.update(node.neighbors)

    # drives the following iterations
    # n-1 because 1st degree neighbors are automatically updated to set
    for x in range(degree_sep-1):

        # keeps track of next neighbor set for iteration with a helperset
        helperset = set([])

        # finds neighbors of newset and updates to the helperset
        # checks newset for 'NoneType' and removes them
        for neighbor in newset:
            if neighbor:
                helperset.update(neighbor.neighbors)
        # changes the helperset into newset for next round of iterations
        newset = helperset

        # appends neighbors for each degree of seperation to the masterlist
        neighbors.update(newset)

    #filter final NoneType
    return filter(bool, neighbors)


def att_filter(myset, att_type, att):
    nodes = []
    visible = g.filter(att_type == att)
    for node in myset:
        if node in visible.nodes:
            nodes.append(node)
    nodes = set(nodes)
    return nodes


def filter_set_type(myset, att):
    nodes = []
    for node in myset:
        if node.NodeType == att:
            nodes.append(node)
    nodes = set(nodes)
    return nodes


def type_neighbors(att_type, att, myset):
    nodes = att_filter(att_type, att, myset)
    neighbors = set(nodes)
    for node in nodes:
        neighbors.update(node.neighbors)
    return neighbors


def fix_set(myset):
    """
    fixes the position of a set of nodes in the graph
    --------------------------
    param - myset: any set of nodes
    """
    for node in myset:
        node.fixed = True


def color_set(myset, color):
    """
    color a set of nodes
    -----------------
    params - set: the set of nodes to be colored
             color: the desired color
    """
    for node in myset:
        node.color = color


def size_set(myset, size):
    """
    control the size of a set of nodes
    -----------------
    params - set1: the set of nodes to be sized
             size: the desired size
    """
    for node in myset:
        if node:
            node.size = size


def return_label(myset):
    """
    return the labels of a set of nodes
    ---------------
    param - set: a set of nodes
    -----------
    return - the labels of a set of nodes
    """
    labellist = []
    for node in myset:
        labellist.append(node.label)
    return labellist


def set_intersect(set1, set2):
    """
    find the intersecting nodes of two sets
    ________________
    params - set1, set 2: subsets of nodes in a graph
    ____________
    return - the intersecting set
    """
    return set(set(set1) & set(set2))
