import openbabel as ob
import rdkit
import numpy as np

def get_bond_order_matrix_rdkit(aemol):
    aemol.to_rdkit()
    bo_mat = np.zeros((len(aemol.rdmol.GetAtoms()), len(aemol.rdmol.GetAtoms())), dtype=np.int32)
    for a in range(len(aemol.rdmol.GetAtoms())):
        for b in range(len(aemol.rdmol.GetAtoms())):
            if a == b: continue
            bo = float(aemol.rdmol.GetBondBetweenAtoms(a,b).GetBondTypeAsDouble())
            bo_mat[a][b] = bo
            bo_mat[b][a] = bo

    return bo_mat

def get_bond_order_matrix_pyb(aemol):
    aemol.to_rdkit()
    bo_mat = np.zeros((len(aemol.pybmol.atoms), len(aemol.pybmol.atoms)), dtype=np.int32)
    for a in range(len(aemol.pybmol.atoms)):
        for b in range(len(aemol.pybmol.atoms)):
            if a == b: continue
            bo = float(aemol.pybmol.atoms[a].OBAtom.GetBond(b).GetBondOrder())
            bo_mat[a][b] = bo
            bo_mat[b][a] = bo

    return bo_mat

def get_distance_matrix(aemol):
    aemol.to_pybel()
    dist_mat = np.zeros((len(aemol.pybmol.atoms), len(aemol.pybmol.atoms)), dtype=np.int32)
    for a in range(len(aemol.pybmol.atoms)):
        for b in range(len(aemol.pybmol.atoms)):
            if a == b: continue
            dist = aemol.pybmol.atoms[a].OBAtom.GetDistance(aemol.pybmol.atoms[b].OBAtom)
            dist_mat[a][b] = int(dist)
            dist_mat[b][a] = int(dist)

    return dist_mat

def get_angle_matrix(aemol):
    aemol.to_pybel()
    ang_mat = np.zeros((len(pymol.atoms),len(pymol.atoms), len(pymol.atoms)), dtype=np.int32)
    for a in range(len(pymol.atoms)):
        for b in range(len(pymol.atoms)):
            if a == b: continue
            for c in range(len(pymol.atoms)):
                if a == c: continue
                if b == c: continue

                ang = pymol.atoms[a].OBAtom.GetAngle(pymol.atoms[b].OBAtom, pymol.atoms[c].OBAtom)
                ang_mat[a][b][c] = float(ang)
                ang_mat[c][b][a] = float(ang)

    return ang_mat

def get_pyb_prop(aemol):
    pair_properties = {}
    pair_properties['distance_matrix'] = get_distance_matrix(aemol)
    pair_properties['angle_matrix'] = get_angle_matrix(aemol)
    pair_properties['bond_matrix'] = get_bond_order_matrix_pyb(aemol)
    return pair_properties
