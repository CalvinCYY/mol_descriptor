import openbabel as ob
import rdkit
import numpy as np


def get_pyb_prop(pybmol):
    atom_props = {}
    for idx, atom in enumerate(pybmol.atoms):
        atom_props[idx]['atom_num'] = atom.atomicnum
        atom_props[idx]['atom_mass'] = atom.atomicmass
        atom_props[idx]['hvy_val'] = atom.heavyvalence
        atom_props[idx]['het_val'] = atom.heterovalence
        atom_props[idx]['hyb'] = atom.hyb
        atom_props[idx]['partial_chg'] = atom.partialcharge
        atom_props[idx]['formal_chg'] = atom.formalcharge

    return atom_props


def get_rdkit_prop(rdmol):
    atom_prop = {}
    for idx, atom in enumerate(rdmol.GetAtoms()):
        #atom_props[idx]['atom_num'] = atom.GetAtomicNum()
        atom_props[idx]['degree'] = atom.GetTotalDegree()
        atom_props[idx]['tot_val'] = atom.GetTotalValence()
        #atom_props[idx]['hyb'] = atom.GetHybridization()
        #atom_props[idx]['partial_chg'] = atom.GetProp('_GasteigerCharge')
        atom_props[idx]['bitvector'] = atom.GetExplicitBitVectProp()
        atom_props[idx]['InRing'] = atom.IsInRing()

    return atom_props
