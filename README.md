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

1. Polish scan height data (csv file)
2. Facets normals as a list of vectors (csv file)
3. Crystal orientation matrix
4. Diamond's culet direction vector

### Output:

2D facet plot with both radial and cartesian coordinates systems (CS).
Good polish directions ranges will be signed on the radial CS, and projections of the principal crystal axes onto the crystal will be according to the cartesian CS.


# Use instructions and requirements
To run this project you need: 

Python 3 with numpy, pandas and matplotlib lybraries. 

Project repository link - https://github.com/TheInbal/Diamond-polishing-directions-analyzer.git


## Extra Information
This project was written as part of this python course https://github.com/Code-Maven/wis-python-course-2025-03.git.
