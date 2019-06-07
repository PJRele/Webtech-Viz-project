import MakeNetworkxGraph
import networkx as nx
import holoviews as hv

# __makegraph__ properties:
# sep_type: 'comma', 'semicolon', 'tab'
# nodes_df_link='' Required.
# links_df_link='' Not required.
# cats_df_link='' Not required.
# weighted=True or False. Regarding edges. Not required.

# Example inputs:
# G = MakeNetworkxGraph.__makegraph__('tab', '../databases/wikispeedia/articles.tsv', '../databases/wikispeedia/links.tsv')
# G = MakeNetworkxGraph.__makegraph__(sep_type='semicolon', nodes_df_link='../databases/GephiMatrix_co-citation.csv')

""" Make HV network """
hv_graph = hv.Graph.from_networkx(G, nx.spring_layout, k=1).relabel('Force-Directed Spring')
hv_graph.opts(width=650, height=650, xaxis=None, yaxis=None, padding=0.1, node_size=hv.dim('size'))
# TO DO (Ani): add HoloMap here, on attribute iterations between 0 and 1000? play with it

# Output file, TO DO: add naming system based on CSV name and graph properties
hv.save(hv_graph, 'yournamehere.html', backend='bokeh')
