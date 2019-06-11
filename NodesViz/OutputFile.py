# Asaf
import MakeNetworkxGraph
import networkx as nx
import holoviews as hv
from holoviews.operation.datashader import datashade, bundle_graph

# __makegraph__ properties:
# sep_type: 'comma', 'semicolon', 'tab'
# nodes_df_link='' Required.
# links_df_link='' Not required.
# cats_df_link='' Not required.
# weighted=True or False. Regarding edges. Not required.

# Example inputs:
# G = MakeNetworkxGraph.__makegraph__('tab', '../databases/wikispeedia/articles.tsv', '../databases/wikispeedia/links.tsv')
# G = MakeNetworkxGraph.__makegraph__(sep_type='semicolon', nodes_df_link='../databases/GephiMatrix_co-authorship.csv')

""" HERE """
# G = MakeNetworkxGraph.__makegraph__(sep_type='tab',
#                                     nodes_df_link='../databases/wikispeedia/articles.tsv',
#                                     links_df_link='../databases/wikispeedia/links.tsv',
#                                     cats_df_link='../databases/wikispeedia/categories.tsv')


""" Make HV network """
hv_graph = hv.Graph.from_networkx(G, nx.spring_layout, k=1).relabel('Force-Directed Spring')

hv_graph.opts(width=650, height=650, xaxis=None, yaxis=None,
              padding=0.1, node_size=hv.dim('size'),
              node_color=hv.dim('node_type'), cmap='YlOrBr',
              edge_color=hv.dim('weight'), edge_cmap='YlGnBu', edge_line_width=hv.dim('weight'))

bundle_graph = bundle_graph(hv_graph)

""" END HERE """


# TO DO (Ani): add HoloMap here, on attribute iterations between 0 and 1000? play with it

# Save files
# TO DO (Asaf):
# Output file, TO DO: add naming system based on CSV name and graph properties
# hv.save(hv_graph, 'smallgephitypetest.html', backend='bokeh')
# hv.save(bundle_graph, 'smallgephitypetestbundled.html', backend='bokeh')

# Output files to Flask
renderer = hv.renderer('bokeh')
plot = renderer.get_plot(hv_graph).state
bundle_plot = renderer.get_plot(bundle_graph).state