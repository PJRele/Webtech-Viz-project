# Asaf 26/5/19
from ImportingGiven import df, N, BB, B_edge_select, figtype, node_sizes, sample_edges, sample_nodes, sample_weights, BS
import math
import bokeh  # 1.1.0
import pandas as pd  # 0.24.2
import matplotlib.pyplot as plt  # 3.0.3
import networkx as nx  # 2.2
import holoviews as hv  # 1.12.1
# import hvplot.networkx as hvnx
from holoviews import opts
from holoviews import dim
# from holoviews.operation.datashader import datashade, bundle_graph, shade, dynspread, rasterize
from holoviews.operation.datashader import bundle_graph

# from holoviews.operation import decimate
hv.extension('bokeh')
import holoviews.operation.datashader as hd

hd.shade.cmap = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999']

""" NetworkX Graph"""


# create graph
# TO DO : add arrows
def make_network(nodes, edges, weighted):
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes, node_size=node_sizes, label=True)
    for edge in edges:
        if weighted:
            graph.add_edge(edge[0], edge[1], weight=edge[2], width=edge[2])
        else:
            graph.add_edge(edge[0], edge[1])
    return graph


# everything works until here


""" NETWORKX Graph to Holoviews"""
G = make_network(sample_nodes, sample_edges, True)


# nx.draw_networkx(G, with_labels=True, node_size=node_sizes, width=sample_weights)

# TO DO : make the following into a test
# print('edges ', G.edges(data=True))

# TO DO : write about these plots in report :
# plt.figure(1,figsize=(12,12))
# pos = nx.circular_layout(G)
# nx.draw_networkx_nodes(G, pos, node_size=100)
# for i in range (0, len(sample_weights)-1):
#     nx.draw_networkx_edges(G, pos, edge_list=[sample_edges[i]], width=sample_weights[i])
# nx.draw(G,with_labels=True,font_size=15,node_size=100, k=1, iterations=20)
# plt.show()
# print('edges ', G.edges(data=True))

def get_net(layout, bundled, shade):
    if (layout.lower() == 'circle'):
        net = hv.Graph.from_networkx(G, nx.layout.circular_layout).relabel('Circular Layout').opts(
            width=650, height=650, xaxis=None,
            yaxis=None, padding=0.1)
    elif layout.lower() == 'spring':
        net = hv.Graph.from_networkx(G, nx.layout.spring_layout, k=0.8, iterations=100).relabel(
            'Force-Directed Fruchterman-Reingold').opts(width=650, height=650, xaxis=None, yaxis=None, padding=0.1)
    #             , node_size=node_dict[i] for i in node_dict.keys())
    else:
        net = "Error 1: layout type must be: 'circle', 'spring'"
    net.opts(width=650, height=650, xaxis=None, yaxis=None, padding=0.1, edge_color_index='weight', edge_cmap='jet')
    if bundled:
        net = bundle_graph(net)
    if B_edge_select:
        net.opts(inspection_policy='edges')
    if shade:
        net = hd.datashade(net).opts(plot=dict(height=650, width=650))
    return net


hv_graph = get_net(figtype, BB, BS)


# decimate(hv_graph)

# doc = hv.renderer('bokeh').server_doc(hv_graph)
def saveFile():
    file_name = figtype + '_' + str(N) + '_'
    if BB & N <= 500:
        file_name = file_name + 'bundled' + '_'
    else:
        file_name = file_name + 'notbundled' + '_'
    if B_edge_select:
        file_name = file_name + 'edgeselect' + '_'
    else:
        file_name = file_name + 'nodeselect' + '_'
    if BS:
        file_name=file_name + 'datashaded'
    else:
        file_name = file_name + 'notdatashaded'
    file_name = file_name + '.html'
    hv.save(hv_graph, file_name, backend='bokeh')


saveFile()
# TO DO REPORT : Explain why adding node and edge sizes is not gonna happen
# TO DO : create option to select nodes OR edges
# """ Export Graph """
# renderer.save(hv_graph, 'force-directed-bundled')
# print (sample_weights)
