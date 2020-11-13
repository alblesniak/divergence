import itertools
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx

def visualize_graph(G):
    pos = nx.layout.spring_layout(G)
    node_sizes = [3 + 10 * i for i in range(len(G))]
    M = G.number_of_edges()
    edge_colors = range(2, M + 2)
    edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
    nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="blue")
    edges = nx.draw_networkx_edges(
    G,
    pos,
    node_size=node_sizes,
    arrowstyle="->",
    arrowsize=10,
    edge_color=edge_colors,
    edge_cmap=plt.cm.Blues,
    width=2)
    nx.draw_networkx_labels(G, pos, font_size=16)
    # set alpha value for each edge
    for i in range(M):
        edges[i].set_alpha(edge_alphas[i])
    pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
    pc.set_array(edge_colors)
    plt.colorbar(pc)
    ax = plt.gca()
    ax.set_axis_off()
    plt.show()


edges = list(itertools.permutations(v.labels, 2))
edges_weighted = [(e[0], e[1], v.dist(e[0], e[1], dist_fn=KL_div)) for e in edges]
G = nx.DiGraph()
for e in edges:
    print(e, v.dist(e[0], e[1], dist_fn=KL_div))
G = nx.DiGraph()
for e in edges:
    G.add_edge(e[0].lstrip('darwin/chapter_').rstrip('.txt'), e[1].lstrip('darwin/chapter_').rstrip('.txt'), weight=v.dist(e[0], e[1], dist_fn=KL_div))
G.edges(data=True)
G.nodes()
nx.write_gexf(G, "darwin_all.gexf")
G_2 = nx.DiGraph()
for node1, node2 in G.edges():
    if G[node1][node2]['weight'] > G[node2][node1]['weight']:
        G_2.add_edge(node1, node2, weight=G[node1][node2]['weight'])
    else:
        continue
len(G_2.edges())