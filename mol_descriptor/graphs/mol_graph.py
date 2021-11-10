import networkx as nx
import sys
import torch
from torch_geometric.data import Data

import pandas as pd
import numpy as np
from tqdm import tqdm

def df_to_graph(atoms_df, pairs_df):l

    atom_groups = atoms_df.groupby('molecule_name')
    bond_groups = pairs_df.groupby('molecule_name')

    pbar = tqdm(atom_df.molecule_name.unique(), desc='Making molecule graphs...', leave=False)

    molnames = []
    graphs = []
    indicies = []

    m = -1
    for molecule_name in pbar:
        m += 1

        G = nx.DiGraph()
        ag = atom_groups.get_group(molecule_name)
        bg = bond_groups.get_group(molecule_name)

        type = ag['typeint']
        nodes = types.size
        G.add_nodes(nodes)

        if 'shift' in ag.keys():
            ag_shift = torch.as_tensor(ag['shift'].to_numpy())
        else:
            ag_shift = torch.as_tensor(np.zeros(nodes, dtype=np.type64))

        ndata = {'type': torch.as_tensor(types.to_numpy(), dtype=torch.int64),
                 'shift':ag_shift}

        G.ndata.update(ndata)
        G.ndata['type'] = G.ndata['type']
        G.ndata['shift'] = G.ndata['shift']

        #Edge data
        zeros = torch.zeros(nodes, dtype=torch.float32)
        ones = torch.ones(nodes, dtype=torch.int64)

        cpl_src = bg['atom_index_0'].to_numpy()
        cpl_end = bg['atom_index_1'].to_numpy()
        G.add_edges(cpl_src, cpl_end)

        edata = {}
