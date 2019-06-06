import ImportGeneral
import networkx as nx
import math
import operator


""" ########################## """
""" Make node and edge weights """
""" ########################## """


def make_node_degrees(nodes_list, edges_list):
    # dictionary where key is node name, value is count of edges
    node_degrees = {node: 0 for node in nodes_list}

    # make node size based on edge count
    for edge in edges_list:
        if edge[0] in node_degrees.keys(): node_degrees[edge[0]] = node_degrees[edge[0]] + 1

    return node_degrees


def really_safe_normalise_in_place(d):
    factor = 1.0 / math.fsum(d.values())
    for k in d:
        d[k] = d[k] * factor
    key_for_max = max(d.items(), key=operator.itemgetter(1))[0]
    diff = 1.0 - math.fsum(d.values())
    # print "discrepancy = " + str(diff)
    d[key_for_max] += diff
    return d


def make_node_sizes(nodes_list, edges_list):
    dic = make_node_degrees(nodes_list, edges_list)
    for k in dic:
        dic[k] = dic[k] + 1
    new_dic = really_safe_normalise_in_place(dic)
    for k in new_dic:
        new_dic[k] = int(new_dic[k] * 10000)
    return new_dic


""" Edge weights module without weighted edge boolean """


def make_edge_weights(nodes_list, edges_list):
    dic = make_node_degrees(nodes_list, edges_list)
    edge_weights = []
    for edge in edges_list:
        edge_weights.append([edge[0], edge[1], dic[edge[0]] + dic[edge[1]]])
    return edge_weights


""" ############ """
""" Make Networkx """
""" ############ """


# Make networkx graph
def make_network(nodes_list, edges_list, weighted, cat_nodes_list=None, cat_links_list=None,):
    graph = nx.DiGraph()

    # make node dimensions
    node_degrees = make_node_degrees(nodes_list, edges_list)
    node_sizes = make_node_sizes(nodes_list, edges_list)

    # add nodes to graph
    for node in nodes_list:
        graph.add_node(node, label=True, degree=node_degrees[node], size=node_sizes[node])

    # make edges
    if weighted == False:
        weighted_edges = make_edge_weights(nodes_list, edges_list)
        edges_list = weighted_edges

    for edge in edges_list:
        graph.add_edge(edge[0], edge[1], weight=edge[2])

    return graph


""" ################################### """
""" Make CATEGORY node and edge weights """
""" ################################### """
# TO DO: fix this
# def make_cat_network(nodes, links, categoriesdf, cat_cols):
#     G = make_network(nodes, links)

#     cat_list = categoriesdf[cat_cols[1]].tolist()
#     ucat_list = list(set(cat_list))

#     # make category edges
#     cat_links = []
#     for col in range(0, len(cat_list) - 1):
#         cat_links.append([categoriesdf.iat[col, 0], categoriesdf.iat[col, 1]])

#     # add category edge weights
#     """ DO THIS """
#     cat_links = make_edge_weights(ucat_list, cat_links)

#     # category dimensions
#     cat_degrees = make_node_degrees(ucat_list, cat_links)
#     cat_sizes = make_node_sizes(ucat_list, cat_links)

#     # add cat nodes to graph
#     for cat in ucat_list:
#         G.add_node(cat, label=True, degree=cat_degrees[cat], size=cat_sizes[cat], node_color='#df3a10')

#     # add cat edges to graph
#     for link in cat_links:
#         G.add_edge(link[0], link[1], weight=link[2], edge_color='#df3a10')
#     return graph


# TO DO: remove, not holoviews
# plt.figure(figsize=(50,50))

""" ####### """
""" DO THIS """
""" ####### """


# TO DO: return graph G

# TO DO: add functionality
def __makegraph__(sep_type, nodes_df_link, links_df_link=None, cats_df_link=None, weighted=False):
    if cats_df_link is None:
        nodes_list, edges_list = \
            ImportGeneral.importcsv(sep_type, nodes_df_link, links_df_link, cats_df_link)
        cat_nodes_list, cat_links_list = None, None
    else:
        nodes_list, edges_list, cat_nodes_list, cat_links_list = \
            ImportGeneral.importcsv(sep_type, nodes_df_link, links_df_link, cats_df_link)

    G = make_network(nodes_list=nodes_list, edges_list=edges_list,
                     cat_nodes_list=cat_nodes_list, cat_links_list=cat_links_list, weighted=weighted)
    return G


# TO DO: remove, not holoviews
# nx.draw_spring(G, node_size=[v*100 for v in degrees.values()],with_labels=True, edge_color='#ffff00')
# plt.show()
# END TO DO
