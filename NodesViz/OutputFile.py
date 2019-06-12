# Asaf
import MakeNetworkxGraph
import PickleMe
import networkx as nx
import holoviews as hv
from holoviews.operation.datashader import datashade, bundle_graph


# __makegraph__ properties:
# sep_type: 'comma', 'semicolon', 'tab'
# nodes_df_link='' Required.
# links_df_link='' Not required.
# cats_df_link='' Not required.
# weighted=True or False. Regarding edges. Not required.

# Example inputs to uploadGraph:
# 1
# ('tab', '../databases/wikispeedia/articles.tsv', '../databases/wikispeedia/links.tsv')
# 2
# (sep_type='semicolon', nodes_df_link='../databases/GephiMatrix_co-authorship.csv')

# 3
# (sep_type='tab',
#                                     nodes_df_link='../databases/wikispeedia/articles.tsv',
#                                     links_df_link='../databases/wikispeedia/links.tsv',
#                                     cats_df_link='../databases/wikispeedia/categories.tsv')

# Upload new
def uploadGraph(CSVtype, nodes_path, links_path=None, cats_path=None):
    graph = MakeNetworkxGraph.__makegraph__(sep_type=CSVtype, nodes_df_link=nodes_path,
                                            links_df_link=links_path, cats_df_link=cats_path)
    return graph


# Get made graph (pickle)
def chooseGraph(directory, pickled_graph):
    PickleMe.set_directory(directory)
    return PickleMe.get_pickle(pickled_graph)


G = chooseGraph("../Pickles/", "GWikiTest.pickle")

""" Make HV network """


def makeHVGraph(layout, filename, NetworkX_Graph):
    new_name = filename + "." + layout + ".HVG"

    # Use pickled graph, unpickle it

    try:
        graph = PickleMe.get_pickle(new_name)

    # Create new graph and pickle it
    except:
        if layout == 'spring':
            graph = hv.Graph.from_networkx(NetworkX_Graph, nx.spring_layout, k=1).relabel('Force-Directed Spring Layout')
        elif layout == 'spectral':
            graph = hv.Graph.from_networkx(NetworkX_Graph, nx.spectral_layout).relabel('Spectral Layout')
        else:
            graph = hv.Graph.from_networkx(NetworkX_Graph, nx.circular_layout).relabel('Circular Layout')
            layout = 'circular'
        PickleMe.pickelize(graph, new_name)
    return graph


hv_graph = makeHVGraph(layout='spring', filename='Wikipedia', NetworkX_Graph=G)

hv_graph.opts(width=650, height=650, xaxis=None, yaxis=None,
              padding=0.1, node_size=hv.dim('size'),
              node_color=hv.dim('node_type'), cmap='viridis',
              edge_color=hv.dim('weight'), edge_cmap='viridis', edge_line_width=hv.dim('weight'))

bundle_graph = bundle_graph(hv_graph)

""" END HERE """

# TO DO (Ani): add HoloMap here, on attribute iterations between 0 and 1000? play with it
frequencies = [0, 50, 100, 250, 500, 750, 1000]
hmap=hv.HoloMap(hv_graph, kdims='frequencies')
hmap

# Save files
# TO DO (Asaf):
# Output file, TO DO: add naming system based on CSV name and graph properties
hv.save(hv_graph, 'pickledtest.html', backend='bokeh')
hv.save(bundle_graph, 'pickledtestbundled.html', backend='bokeh')

# Output files to Flask
renderer = hv.renderer('bokeh')
plot = renderer.get_plot(hv_graph).state
bundle_plot = renderer.get_plot(bundle_graph).state
