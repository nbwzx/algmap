import pandas as pd
import networkx as nx
from pyvis.network import Network
df = pd.read_csv("corner.csv")
G = nx.from_pandas_edgelist(df, source='Source', target='Target')
net = Network(notebook=True, width=1450, height=800)
net.from_nx(G)
net.show("index.html")