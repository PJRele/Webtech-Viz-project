from ImportGeneral import G
import networkx as nx
import holoviews as hv

""" Make HV network """
# node_size_dim = hv.Dimension(hashed_size_dict, label='Node size',)
hv_graph = hv.Graph.from_networkx(G, nx.spring_layout, k=1).relabel('Force-Directed Spring')
hv_graph.opts(width=650, height=650, xaxis=None, yaxis=None, padding=0.1, node_size=hv.dim('size'))
# TO DO (Ani): add HoloMap here, on attribute iterations between 0 and 1000? play with it


hv.save(hv_graph, 'graphtest.html', backend='bokeh')

