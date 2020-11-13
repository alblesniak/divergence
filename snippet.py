import itertools
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx


edges = list(itertools.permutations(v.labels, 2))
edges_weighted = [(e[0], e[1], v.dist(e[0], e[1], dist_fn=KL_div)) for e in edges]
G = nx.DiGraph()

