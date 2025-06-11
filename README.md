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

This tool is designed to automate the analysis process and provide a clearer and more convenient view of the data in order to draw more definitive conclusions.

# How is it works?

\section{Analysis Method}

To achieve the primary objectives of this study to find a correlation between the optimal polishing directions determined through the polishing tests and the crystallographic directions, the analysis required the alignment of three coordinate systems:

\begin{itemize}
    \item Crystallographic Coordinate System (3D indices)
    \item Laboratory Coordinate System (3D indices)
    \item Facet Coordinate System (2D indices)
\end{itemize}

The analysis was conducted using Python according to the following algorithmic approach.

\subsection{System Definitions}

\begin{itemize}
    \item Culet direction of the stone
    \item Normal to facet
    \item Orientation matrix
\end{itemize}

\subsection{Step 1: Transformation matrix from lab CS to crystallographic CS}

Creating a transformation matrix $[S]$ to convert vectors from the lab CS to the crystallographic CS:

A negative sign is assigned to the $y$-axis to account for the desynchronization introduced during the scanning process between the polishing and diffractometer laboratories.

\subsection{Step 2: Define the facet coordinate system (2D)}

Convert vectors from lab CS to crystallographic CS.

Setting two orthogonal vectors on the facet.

Creating a transformation matrix $[F]$ to convert vectors from the crystallographic CS to the facet CS.

Given that the normal is orthogonal to the facet, multiplication of a vector by the matrix $F$ will annihilate the third component in the facet's plane, consequently reducing the system to two dimensions.

\subsection{Step 3}

The orientation of the axis is determined by the angle relative to the stone. Specifically, it can be found for the three basis vectors of the crystal $[1\ 0\ 0]$, $[0\ 1\ 0]$, $[0\ 0\ 1]$.

Determining whether the axis points towards or away from the face of the stone:

If the angle $< 90^\circ$ then the axis points away from the stone, and if the angle $> 90^\circ$ then the axis points towards the st

