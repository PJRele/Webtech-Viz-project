import pandas as pd  # 0.24.2
import networkx as nx  # 2.2
from matplotlib import pyplot as plt
from collections import Counter
import holoviews as hv
from holoviews import opts
import math
import operator

hv.extension('bokeh', 'matplotlib')

""" ########### """
""" Import CSVs """
""" ########### """


# TO DO: single CSV Gephi input
# def importcsv(inputstring):

# import nodes, links, by separation type
def importcsv(node_csv, link_csv, separation_type):
    if separation_type == "semicolon":
        nodes = pd.read_csv(
            node_csv,
            delimiter=';')  # 4603 articles
        links = pd.read_csv(
            link_csv,
            delimiter=';')
    elif separation_type == "tab":
        nodes = pd.read_csv(
            node_csv,
            delimiter='\t')  # 4603 articles
        links = pd.read_csv(
            link_csv,
            delimiter='\t')
    elif separation_type == 'comma':
        nodes = pd.read_csv(
            node_csv,
            delimiter=',')  # 4603 articles
        links = pd.read_csv(
            link_csv,
            delimiter=',')
    else:
        nodes = 'Broken'
        links = 'Broken'
        print("Please choose 'comma', 'semicolon' or 'tab'.")
    return (nodes, links)


# import nodes, links, categories, by separation type
def importcsv(node_csv, link_csv, categories_csv, separation_type):
    if separation_type == "semicolon":
        nodes = pd.read_csv(node_csv, delimiter=';')  # 4603 articles
        links = pd.read_csv(link_csv, delimiter=';')
        categories = pd.read_csv(categories_csv, delimiter=';')
    elif separation_type == "tab":
        nodes = pd.read_csv(node_csv, delimiter='\t')  # 4603 articles
        links = pd.read_csv(link_csv, delimiter='\t')
        categories = pd.read_csv(categories_csv, delimiter='\t')
    elif separation_type == 'comma':
        nodes = pd.read_csv(node_csv, delimiter=',')  # 4603 articles
        links = pd.read_csv(link_csv, delimiter=',')
        categories = pd.read_csv(categories_csv, delimiter=',')
    else:
        nodes = 'Broken'
        links = 'Broken'
        categories = 'Broken'
        print("Please choose 'comma', 'semicolon' or 'tab'.")
    return nodes, links, categories


node_df, links_df, categories_df = importcsv('databases/wikispeedia/articles.tsv', 'databases/wikispeedia/links.tsv',
                                             'databases/wikispeedia/categories.tsv', 'tab')

""" ########################### """
""" Make nodes list, links list """
""" ########################### """
columns = []
for col in node_df.columns:
    columns.append(col)

nodes = node_df[columns[0]].tolist()
N = len(nodes)
links = []
for col in range(0, N - 1):
    links.append([links_df.iat[col, 0], links_df.iat[col, 1]])

""" Get number of unique columns """
# get DF columns
cat_columns = []
for col in categories_df.columns:
    cat_columns.append(col)

# node as dict key, category as value
categories_dict = {categories_df.iloc[i, 0]: categories_df.iloc[i, 1] for i in range(0, len(categories_df.index) - 1)}
# turn to colors, turn to labels
count = Counter(e for e in categories_dict.values())
num_cats = len(count)

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


""" Edges module with weighted edge boolean """


def make_edge_weights(nodes_list, edges_list, weighted):
    dict = make_node_degrees(nodes_list, edges_list)
    edge_weights = []

    if weighted == 'y':
        for edge in edges_list: edge_weights.append([edge[0], edge[1], edge[2]])
    else:
        for edge in edges_list:
            edge_weights.append([edge[0], edge[1], dict[edge[0]] + dict[edge[1]]])

    return edge_weights


""" Edges module without weighted edge boolean """


def make_edge_weights(nodes_list, edges_list):
    dict = make_node_degrees(nodes_list, edges_list)
    edge_weights = []
    for edge in edges_list:
        edge_weights.append([edge[0], edge[1], dict[edge[0]] + dict[edge[1]]])
    return edge_weights


""" ############ """
""" Make Networkx """
""" ############ """


# make network, asking about weight
def make_network(nodes_list, edges_list, weighted):
    graph = nx.DiGraph()

    # make dimensions
    node_degrees = make_node_degrees(nodes_list, edges_list)
    node_sizes = make_node_sizes(nodes_list, edges_list)
    weighted_edges = make_edge_weights(nodes_list, edges_list, weighted)

    # add nodes to graph
    for node in nodes_list:
        graph.add_node(node, label=True, degree=node_degrees[node], size=node_sizes[node])

    for edge in weighted_edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2])

    return graph


# make network, not asking about weight
def make_network(nodes_list, edges_list):
    graph = nx.DiGraph()

    # make dimensions
    node_degrees = make_node_degrees(nodes_list, edges_list)
    node_sizes = make_node_sizes(nodes_list, edges_list)
    weighted_edges = make_edge_weights(nodes_list, edges_list)

    # add nodes to graph
    for node in nodes_list:
        graph.add_node(node, label=True, degree=node_degrees[node], size=node_sizes[node])

    # add edges to graph
    for edge in weighted_edges:
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


G = make_network(nodes, links)

""" Make HV network """
# node_size_dim = hv.Dimension(hashed_size_dict, label='Node size',)
hv_graph = hv.Graph.from_networkx(G, nx.spring_layout, k=1).relabel('Force-Directed Spring')
hv_graph.opts(width=650, height=650, xaxis=None, yaxis=None, padding=0.1, node_size=hv.dim('size'))
hv_graph

# TO DO: remove, not holoviews
# nx.draw_spring(G, node_size=[v*100 for v in degrees.values()],with_labels=True, edge_color='#ffff00')
# plt.show()
# END TO DO
