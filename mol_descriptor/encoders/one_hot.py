from rdkit import Chem
import numpy as np
from sklearn.preprocessing import OneHotEncoder

"""
Have a list of unique atoms, iterate each mol against the list to generate a numpy array of 1s and 0s with 1 representing the molecule
"""

ref_atoms = {'H': 1, 'C': 6, 'N': 7, 'O': 8, 'F': 9}

"""
Do I need this????
"""


def get_atom_dict(rdmol):
    atom_dict = {}
    for atom in rdmol.GetAtoms():
        if atom.GetAtomicNum() not in key for keys in atom_dict.keys():
            atom_dict[atom.GetAtomicNum()] = 1

    return atom_dict


def one_hot(rdmol, atom_dict):
    atom_type_array = np.zeros(
        (len(rdmol.GetAtoms()), len(rdmol.GetAtoms())), dtype=int32)
    a_num = []
    for atom in rdmol.GetAtoms():
        a_num.append(atom.GetAtomicNum())
        atom_type_array = [ref_atoms[num for num in a_num]]

    return atom_type_array


def convert_labels_to_one_hot(dictionary_key):
    labelled_values = np.array(dictionary_key.values)


def sklearn_one_hot(atom_props):
    for idx in atom_props
