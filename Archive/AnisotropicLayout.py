# Inputs: graph G={V,E,W}; max number of iterations k; depth field lag l;
# step size a; weighing factor wp
# Output: Positions X = {xi:1<=1<=n} for all vi in V
def create_layout(V, E, W, k, l, a, wp):
    n = V.length()
    X = []
    X.append(MDS_initialize()) # section 2.2
    # cbar in R^n <- compute graph centrality values for vi in V
    cbar = 0
    j = -1 # index to keep track of field updates
    for t in range(1, k):
        if t%l == 0:
            j = j + 1
            try:
                X[j] = X[t]
            except:
                print("X[j]=X[t] error.")
           # M[X[j]][cbar] = monotonic_field() # section 2.3
        # X[t+1] = X[t-a()] # formula from section 3.1, gradient update step
    return X

# section 2.2
# MDS = multidimensional scaling
def MDS_initialize(init_pos, links):
    # get initial position as list size N (number of nodes), form (x0,y0),...
    # links



    return init_pos

def monotonic_field():
    node_field = 0
    return node_field