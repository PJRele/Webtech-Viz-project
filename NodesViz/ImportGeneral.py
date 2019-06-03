import pandas as pd  # 0.24.2
import networkx as nx  # 2.2

""" Import CSVs """
node_df = pd.read_csv(
    '../databases/wikispeedia/articles.tsv',
    delimiter='\t')  # 4603 articles
links_df = pd.read_csv(
    '../databases/wikispeedia/links.tsv',
    delimiter='\t')
# categories_df = pd.read_csv(
#     '../databases/wikispeedia/categories.tsv',
#     delimiter='\t')

""" Make nodes list, links list """
nodes = node_df['Article_Name'].tolist()
N = len(nodes)
links = []
for col in range(0, N - 1):
    links.append([links_df.iat[col, 0], links_df.iat[col, 1]])


def make_node_weights(nodes_list, edges_list):
    # dictionary where key is node name, value is count of edges
    node_dict = {node: 0 for node in nodes_list}

    # make node size based on edge count
    for edge in edges_list:
        if edge[0] in node_dict.keys(): node_dict[edge[0]] = node_dict[edge[0]] + 1

    return node_dict


def make_edge_weights(nodes_list, edges_list, weighted):
    dict = make_node_weights(nodes_list, edges_list)
    edge_weights = []

    if weighted == 'y':
        for edge in edges_list: edge_weights.append([edge[0], edge[1], edge[2]])
    else:
        for edge in edges_list:
            edge_weights.append([edge[0], edge[1], dict[edge[0]] + dict[edge[1]]])

    return edge_weights


def make_network(nodes_list, edges_list, weighted):
    graph = nx.DiGraph()
    weighted_edges = make_edge_weights(nodes_list, edges_list, weighted)
    # add nodes to graph
    for node in nodes_list:
        graph.add_node(node, label=True, node_size=dict[node])

    for edge in weighted_edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2], width=edge[2])

    return graph

#
# while (1):
#     weighted = (input('Does your input have an edge-weight column? (y/n)\n'))
#     if weighted.lower() == 'n' or weighted.lower() == 'y':
#         break
#     print('Enter "y" or "n". If unsure, enter "n".')
#
# G = make_network(nodes, links, weighted)
# nx.draw(G)

