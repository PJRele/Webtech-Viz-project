# Asaf 26/5/19
from Importing import *

# Make edges dataframe
edge_df = pd.DataFrame(sample_edges)
edge_df.columns = ['source', 'target', 'value']

# Make nodes dataframe
node_df = pd.DataFrame(sample_nodes)
# node_df.insert(0, 'index','0')
# for col in range(0, N-1):
#     node_df.iat[col, 0]=col
node_df.insert(1, 'group','1')


# Turn DF to usable HV
edge_ds = hv.Dataset(edge_df)
node_ds = hv.Dataset(pd.DataFrame(pd.DataFrame(sample_nodes)))


# chord = hv.Chord((edge_ds, node_ds),['source','target','value'])
#
# hv.save(chord, 'chord.html', backend='bokeh')

# 26/5/2019 - not working