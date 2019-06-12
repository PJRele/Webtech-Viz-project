# DATAVIZ
A website that allows for interactive visualizations. Coming soon.

## Installation
Unzip the file or go to Github Desktop, like standard. 

## Current usage Nodes link
To check the nodes-link diagram, go to the NodesViz folder, and open the file OutputFile.py. In the line that defines G (G = ...), set it equal to uploadGraph(parameters), where the parameters are (in order) the separation type, nodes file, links file, and categories file. To view, the input must be saved as an HTML file. Go to the bottom of OutputFile.py, where it says "hv.save(hv_graph,'yourname.html',backend='bokeh')" and replace 'yourname' with the name you prefer. To see a bundled version of the graph, save that as well; it is in the next line. To choose a layout, change the line that defines 'hv_graph', "hv_graph = makeHVGraph(layout='spring', filename='Wikipedia', NetworkX_Graph=G)" to 'spring', 'spectral', or 'circular'.

## Pickling Nodes link
When uploading a new graph to OutputFile.py, it gets saved as an object in the Pickles directory. To choose the name of this file (it has to be unique to get saved), change "Wikipedia" in the line "hv_graph = makeHVGraph(layout='spring', filename='Wikipedia', NetworkX_Graph=G)".

## Nodes link Parameters
Separation type: "comma", "semicolon", or "tab".
Nodes file: if only this is uploaded, it's assumed that it's in the form of a Gephi matrix. The first line describes the header, or the nodes, the subsequent lines define the edge weights between nodes. 
Single nodes file example: 
,Bob,Christie,Dave
Bob,0,1,0,
Christie,1,0,3,
Dave,0,3,0
Nodes file (alongside links file): CSV of node names.
Links file: two-column CSV, each line describes the connection between two nodes.
Categories file: two-column CSV, each line defines a node and its category. If a node appeared in the nodes file but not this one, it is category-less.


## Current usage matrix
## Usage of the website, coming soon.
- An Upload button allows for uploading files for it to be visualized.
- A Play button refreshes the visualisation.
- The left frame contains a node visualisation.
- The right frame contains a matrix visualisation.
