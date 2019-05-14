# Asaf 10/5/19
import bokeh # 1.1.0
import pandas as pd # 0.24.2
import matplotlib.pyplot as plt # 3.0.3
import networkx as nx # 2.2
import holoviews as hv # 1.12.1
import hvplot.networkx as hvnx
from holoviews import opts
from holoviews import dim
from holoviews.operation.datashader import datashade, bundle_graph, shade, dynspread, rasterize
from holoviews.operation import decimate
hv.extension('bokeh','matplotlib')

""" PARAMETERS """
# sample node size, len(df.columns) to get all
N = len(df.columns)
# number of max points on screen, excludes edgeless nodes
decimate.max_samples=1000
# fractional spread of adjacent nodes
dynspread.max_px=20
dynspread.threshold=0.5
# bundled_boolean 
BB = True

""" Renderer """
renderer = hv.renderer('bokeh')


""" Read File """
df = pd.read_csv('C:/Users/Asaf/Documents/TU Software/Y3/Q4/DBL HTI Webtevh/Github/Webtech-Viz-project/Given CSVs/GephiMatrix_co-citation.csv', delimiter=';')


""" Edges """
# sample size edges + weights
def make_edges(dframe, sample_size, weight_threshold):
    edges = []
    weights = []
    nodes = dframe.columns.tolist()
    # TO DO1 : instead of counting like this, put the name and its 'index'
    for row in range (0, sample_size):
        for col in range (0, sample_size):
            if dframe.iat[row,col] > weight_threshold:
                edges.append([nodes[row],nodes[col],dframe.iat[row,col]])
                weights.append(dframe.iat[row,col])
    return edges, weights
# row, column, weight
sample_edges, sample_weights = make_edges(df, N-1, 0)

""" Nodes """
# the nodes, with deleted ';' in head of file
all_nodes = df.columns.tolist()
sample_nodes = all_nodes[:N-1]

# dictionary where key is node name, value is count of edges 
node_dict={sample_nodes[0]:0}
for node in sample_nodes:
    if node not in node_dict.keys():
        node_dict[node] = 0

# make node size based on edge count
for edge in sample_edges:
    if edge[0] in node_dict.keys():
        node_dict[edge[0]] = node_dict[edge[0]] + 1

node_sizes = []
for key in node_dict.keys():
    # +1 to show all nodes, *50 to make it larger
    node_sizes.append((node_dict[key] * 10)+1)

weight_dimensions = [hv.Dimension(('node_sizes','Node Size'))]



""" NetworkX Graph"""
# create graph
# TO DO : add arrows
def make_network(nodes, edges):
    graph=nx.DiGraph()
    graph.add_nodes_from(nodes, node_size=node_sizes)
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2], width=edge[2]*3)
    return graph

# everything works until here


""" NETWORKX Graph to Holoviews"""
G = make_network(sample_nodes, sample_edges)
# nx.draw_networkx(G, with_labels=False, node_size=node_sizes, width=sample_weights)

# TO DO : make the following into a test
# print('edges ', G.edges(data=True))

# TO DO : write about these plots in report :
# plt.figure(1,figsize=(12,12))
# pos = nx.circular_layout(G)
# nx.draw_networkx_nodes(G, pos, node_size=100)
# for i in range (0, len(sample_weights)-1):
#     nx.draw_networkx_edges(G, pos, edge_list=[sample_edges[i]], width=sample_weights[i]/10)
# nx.draw(G,with_labels=False,font_size=15,node_size=100, k=1, iterations=20)
# plt.show()
# print('edges ', G.edges(data=True))

def get_net(layout, bundled):

    if (layout.lower() == 'circular'):
        net = hv.Graph.from_networkx(G, nx.layout.circular_layout).relabel('Circular Layout').opts(
            width=650, height=650, xaxis=None,
                                        yaxis=None, padding=0.1)
    elif(layout.lower() == 'spring'):
         net = hv.Graph.from_networkx(G, nx.layout.spring_layout, k=0.8, iterations=100).relabel('Force-Directed Fruchterman_Reingold').opts(width=650, height=650, xaxis=None, yaxis=None, padding=0.1)
#             , node_size=node_dict[i] for i in node_dict.keys())
    else:
        net = 'Error 1: unimplemented layout request.'
    
    if (bundled==True):
        net = bundle_graph(net)
    return net

hv_graph = get_net('spring', BB)
# decimate(hv_graph)

# TO DO REPORT : Explain why adding node and edge sizes is not gonna happen
# TO DO : create option to select nodes OR edges
""" Export Graph """
# renderer.save(hv_graph, 'force-directed-bundled')
