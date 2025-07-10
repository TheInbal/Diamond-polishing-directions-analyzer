import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


# The data folder need to include: Transformation matrix, Target facets, normals to facets, z vector, good polish areas.
# Please find the information about files formats in project's README.
# folder_path = sys.argv[1]
# stone_name = sys.argv[2]
# folder_path = 'C:\\Inbal\\University\\Chemistry Msc Weizmann\\Courses\\Python Course\\Final Project\\Data Diamond 005'


# Transformation matrix from polisher coordinates to crystal coordinates system:
def Trans_mat(folder_path):
    trans_mat_file = folder_path + "\\Transformation_matrix.txt"
    df_trans_mat = pd.read_csv(trans_mat_file, sep='\t')
    Trans_mat = df_trans_mat.values
    return Trans_mat

# List of the numbers of the facets which were checked by the polisher: 
def Target_facets(folder_path):
    tar_fac_file = folder_path + "\\Target_facets.txt"
    with open(tar_fac_file) as f:
        Target_facets=[]
        for line in f:
            line = line.split() # to deal with blank 
            if line:            # lines (ie skip them)
                line = [int(i) for i in line]
                Target_facets.append(line)
    return Target_facets

# Normals of the facets in polisher's CS:
def normals(folder_path):
    normals_file = folder_path + "\\Normals.txt"
    df_normals = pd.read_csv(normals_file, sep='\t')
    normals = df_normals.values
    return normals


# Z vector of the diamond in polisher's CS:
def Z_vec(folder_path):
    z_vec_file = folder_path + "\\Z_vector.txt"
    df_z = pd.read_csv(z_vec_file, sep='\t')
    Z_vec_full = df_z.values
    Z_vec = Z_vec_full[0]
    return Z_vec


# Ranges (in angles) of good polishing from polisher scans:
# Every row built like folowing: [from1, to1, from2, to2, from3, to3, from4, to4, facet number]
def Good_polish_ranges(folder_path):
    good_pol_file = folder_path + "\\Good_polish_ranges.txt"
    df_good_pol = pd.read_csv(good_pol_file, sep='\t')
    Good_polish_ranges = df_good_pol.values
    return Good_polish_ranges





