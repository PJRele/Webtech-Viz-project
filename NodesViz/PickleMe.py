import pickle
from os import listdir
from os.path import isfile, join
import MakeNetworkxGraph
import networkx as nx

""" TEST """

# Gtest = MakeNetworkxGraph.__makegraph__(sep_type='tab',
#                                     nodes_df_link='../databases/wikispeedia/articles.tsv',
#                                     links_df_link='../databases/wikispeedia/links.tsv',
#                                     cats_df_link='../databases/wikispeedia/categories.tsv')
#
# TO DO: make this work with individual user's computer's cookie folder
filepath = "../Pickles/"

def set_directory(directory):
    filepath = directory

def pickelize(Graph, name):
    pickling_on = open(filepath + "%s.pickle" % name,"wb")
    pickle.dump(Graph, pickling_on)
    pickling_on.close()


# To list saved files
def get_pickles(directory):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    return onlyfiles

# Use .pickle at the end
def get_pickle(name):
    full_path = filepath + name
    try:
        pickle_off = open(full_path, "rb")
    except:
        pickle_off = open(full_path + ".pickle", "rb")

    loadedGraph = pickle.load(pickle_off)
    return loadedGraph

graph = get_pickle("GWikiTest.pickle")


# print(graph.edges())