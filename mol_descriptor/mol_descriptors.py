from mol_translator import aemol

from .chemical_features import *
from .encoders import *
from .graphs import *


class mol_descriptor(object):
    def __init__(self, aemol):
        self.mol = aemol
        self.descriptors = None
        self.atom_properties = {}
        self.pair_properties = {}
        self.molecular_rep = None

    def generate_basic_atom_props(self):
        self.atom_properties = atom_prop.get_pyb_prop(self.mol.pybmol)
        self.atom_properties.update(atom_prop.get_rdkit_prop(self.mol.rdmol))

    def generate_basic_pair_props(self):
        self.pair_properties = pair_prop.get_pyb_prop(self.mol.pybmol)

    def one_hot_encode(self, atom_prop_key):
        return one_hot_df

    def generate_graph_from_df(atoms_df, pairs_df, graph_type='FC'):
        if graph_type == 'FC':
            mol_graphs=graphs.mol_graph(atoms_df, pairs_df)
        elif graph_type == 'weave':
            mol_graphs=graphs.weave(atoms_df, pairs_df)
        elif graph_type == 'graph_conv':
            mol_graphs=graphs.graphconv(atoms_df, pairs_df)
        else:
            raise ValueError(
                f"graph_type: {graph_type} is currently not supported")
