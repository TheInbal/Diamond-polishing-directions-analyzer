import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import Data_module_diamond

# The data folder need to include: Transformation matrix, Target facets, normals to facets, z vector, good polish areas.
# Please find the information about files formats in project's README.
folder_path = sys.argv[1]
stone_name = sys.argv[2]


# Transformation matrix from polisher coordinates to crystal coordinates system:
Trans_mat = Data_module_diamond.Trans_mat(folder_path)

# List of the numbers of the facets which were checked by the polisher: 
Target_facets = Data_module_diamond.Target_facets(folder_path)

# Normals of the facets in polisher's CS:
normals = Data_module_diamond.normals(folder_path)

# Z vector of the diamond in polisher's CS:
Z_vec = Data_module_diamond.Z_vec(folder_path)

# Ranges (in angles) of good polishing from polisher scans:
# Every row built like folowing: [from1, to1, from2, to2, from3, to3, from4, to4, facet number]
Good_polish_ranges = Data_module_diamond.Good_polish_ranges(folder_path)



def color_polar_sector(ax, min_angle, max_angle, min_radius, max_radius, color):
  """Colors a sector in a polar plot.
  Args:
    ax: The matplotlib axes object.
    min_angle: Minimum angle of the sector in radians.
    max_angle: Maximum angle of the sector in radians.
    min_radius: Minimum radius of the sector.
    max_radius: Maximum radius of the sector.
    color: Color of the sector."""

  angles = np.linspace(min_angle, max_angle, 100)
  radii_outer = np.full_like(angles, max_radius)
  radii_inner = np.full_like(angles, min_radius)

  ax.fill_between(angles, radii_inner, radii_outer, color=color, alpha=0.2)


def find_axis_dir(normal_normal, axis):
    """Find if axis is point outside the stone or inside
    Args:
      normal_normal: the normalized normal
      axis: one of the main axis of the crystal ([1 0 0], [0 1 0], [0 0 1])"""

    A = np.dot(normal_normal, axis)
    angle_with_plane = np.arccos(A)
    deg_angle = np.rad2deg(angle_with_plane)
    if deg_angle <= 90:
        axis = axis
    else:
        axis = axis * (-1)
    return axis


def get_integer_direction(A0, tolerance):
    Asort = np.sort(np.abs(A0))
    A = A0 / Asort[-1]
    stop = np.where(np.abs(A - np.round(A)) < tolerance)[0]
    k = 1
    while len(stop) < 3:
        k += 1
        A = A * k / (k - 1)
        stop = np.where(np.abs(A - np.round(A)) < tolerance)[0]
    A = np.round(A)
    AB = f'({int(A[0])}  {int(A[1])}  {int(A[2])})'
    n = k / Asort[-1]
    return AB, n



for i in range(len(Target_facets)):
    # normal to the face:
    N = normals[i]
    N /= np.linalg.norm(N)
    e1 = np.cross(Z_vec, N)
    e1 = e1 / np.linalg.norm(e1)
    e2 = np.cross(N, e1)
    e2 = e2 / np.linalg.norm(e2)


    # Transformation matrix from crystal coordinates to face coordinates:
    F_mat = np.array([[e1[0], e2[0], N[0]],
                      [e1[1], e2[1], N[1]],
                      [e1[2], e2[2], N[2]]])

    a_axis = np.array([1, 0, 0])
    a = find_axis_dir(N, a_axis)
    a = np.matmul(a, F_mat)
    minus_a = np.array([-a[0], -a[1], -a[2]])
    b_axis = np.array([0, 1, 0])
    b = find_axis_dir(N, b_axis)
    b = np.matmul(b, F_mat)
    minus_b = np.array([-b[0], -b[1], -b[2]])
    c_axis = np.array([0, 0, 1])
    c = find_axis_dir(N, c_axis)
    c = np.matmul(c, F_mat)
    minus_c = np.array([-c[0], -c[1], -c[2]])
    e1 = np.matmul(e1, F_mat)
    e2 = np.matmul(e2, F_mat)


    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    colors = ['red', 'green', 'blue', 'red', 'green', 'blue']

    # Quiver plot
    quiver = plt.quiver(
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [a[0], b[0], c[0], minus_a[0], minus_b[0], minus_c[0]],
        [a[1], b[1], c[1], minus_a[1], minus_b[1], minus_c[1]],
        angles='xy', scale_units='xy', ls=['solid', 'solid', 'solid', 'dashed', 'dashed', 'dashed'],
        scale=1, linewidth=[3, 3, 3, 3, 3, 3], fc='none', ec=colors)

    ax1 = fig.add_subplot(111, projection='polar', facecolor="none")

    # Set plot limits
    ax.set_aspect('equal')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax1.set_rlim(0, 1)
    ax.grid(True)

    # Create custom legend handles
    legend_handles = [
        plt.Line2D([0], [0], color='red', lw=5, label=r'$a_{{1}}$'),
        plt.Line2D([0], [0], color='green', lw=5, label=r'$a_{{2}}$'),
        plt.Line2D([0], [0], color='blue', lw=5, label=r'$a_{{3}}$')]

    color_polar_sector(ax1, np.deg2rad(Good_polish_ranges[i, 0]), np.deg2rad(Good_polish_ranges[i, 1]), 0, 1, 'orange')
    if Good_polish_ranges[i, 2] != 0:
        color_polar_sector(ax1, np.deg2rad(Good_polish_ranges[i, 2]), np.deg2rad(Good_polish_ranges[i, 3]), 0, 1, 'orange')
    if Good_polish_ranges[i, 4] != 0:
        color_polar_sector(ax1, np.deg2rad(Good_polish_ranges[i, 4]), np.deg2rad(Good_polish_ranges[i, 5]), 0, 1, 'orange')
    if Good_polish_ranges[i, 6] != 0:
        color_polar_sector(ax1, np.deg2rad(Good_polish_ranges[i, 6]), np.deg2rad(Good_polish_ranges[i, 7]), 0, 1, 'orange')

    ax1.legend(handles=legend_handles, fontsize=20, framealpha=1)
    plt.title(f'Stone {stone_name}, Facet {Target_facets[i]}, Miller indices: {get_integer_direction(N, 0.2)[0]} ', fontsize=25, weight='bold')

    import os
    dir = f'facet_plots_{stone_name}'
    if not os.path.exists(dir):
        os.mkdir(dir)
    path = f'{dir}/facet_{Target_facets[i]}.png'
    plt.savefig(path)
