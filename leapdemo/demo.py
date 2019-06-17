import networkx as nx
import matplotlib.pyplot as plt
from dimod.reference.samplers import ExactSolver
import dwave_networkx as dnx
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite


s5 = nx.star_graph(4)
plt.subplot(121)
nx.draw(s5, with_labels=True, font_weight='bold')

sampler = ExactSolver()
print(dnx.min_vertex_cover(s5,sampler))

sampler = EmbeddingComposite(DWaveSampler())
print(dnx.min_vertex_cover(s5, sampler))

w5 = nx.wheel_graph(5)
plt.subplot(121)
nx.draw(w5, with_labels=True, font_weights='bold')
print(dnx.min_vertex_cover(w5, sampler))
