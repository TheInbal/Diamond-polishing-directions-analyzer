# Diamond-polishing-directions-analyzer
This analyzer built to find a correlation between the optimal polishing directions determined through a polishing tests and the crystallographic directions. 

# Background
Diamond, the hardest material in nature, presents unique challenges for polishing due to its anisotropic
hardness, which changes with crystallographic orientation. While polishing some facets aligns with established
theoretical models, other facets remains challenging to predict. With growing demand in the diamond industry
and increasing need in automation, a complete physical model is required to address the critical questions:

• Which orientations allow for the most efficient and effective polishing on each facet?

• Is there a single model that accurately predicts preferable polishing directions for all the facets?

Our research seeks to test and expand upon existing theories of diamond polishing using X-ray diffraction and
polishing experiments on single-crystal diamonds. 


![image](https://github.com/user-attachments/assets/000c7d81-d1cd-448b-833b-4db4b017f5d1)


This tool is designed to automate the analysis process and provide a clearer and more convenient view of the data in order to draw more definitive conclusions.

# Input and Output
### Inputs:

To run the program you should have a folder which includes 5 text files:
1. Transformation_matrix (3x3 matrix), components seperated by tab.
2. Normals - facets normals (3 components per normal x, y, z), components seperated by tab.
3. Target_facets - every facet number in a different line.
4. Z_vector - diamond's culet direction vector, components seperated by tab.
5. Good_polish_ranges - ranges (in angles) of good polishing from polisher scans. Every row built like folowing: [from1, to1, from2, to2, from3, to3, from4, to4, facet number]

This will be your 'Data folder'. Make sure to fill the files in the same format as it appears in the example folder here on github!


### Output:

2D facet plot with both radial and cartesian coordinates systems (CS).
Good polish directions ranges will be signed on the radial CS, and projections of the principal crystal axes onto the crystal will be according to the cartesian CS.


# Use instructions and requirements
To run this project you need: 
Python 3 with numpy, pandas and matplotlib lybraries. 

**Run command:** Python  Diamond_polishing_project.py  Data_folder_path  stone_name

Project repository link - https://github.com/TheInbal/Diamond-polishing-directions-analyzer.git


## Extra Information
* The polishing processes in this research are carried out by an external party. Some of the data used in the project originates from the same external source, which collects information about the polishing for us. We study this data within a crystallographic framework and using an X-ray diffractometer. Inside the code, this external source called 'polisher'.
* This project was written as part of this python course https://github.com/Code-Maven/wis-python-course-2025-03.git.
