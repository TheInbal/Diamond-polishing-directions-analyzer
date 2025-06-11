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

System definitions:
𝒁 - Culet direction of the stone:
(25) 𝒁 = (𝒆𝟏 𝒆𝟐 𝒆𝟑) ⋅ (
𝑍𝑒1
𝑍𝑒2
𝑍𝑒3
) = 𝑍𝑒1𝒆𝟏 + 𝑍𝑒2𝒆𝟐 + 𝑍𝑒3𝒆𝟑
𝑵 - Normal to facet:
(26) 𝑵 = (𝒆𝟏 𝒆𝟐 𝒆𝟑) ⋅ (
𝑁𝑒1
𝑁𝑒2
𝑁𝑒3
) = 𝑁𝑒1𝒆𝟏 + 𝑁𝑒2𝒆𝟐 + 𝑁𝑒3𝒆𝟑
Orientation matrix:
(27) [𝑈𝐴] = [
𝑎11 𝑎12 𝑎13
𝑎21 𝑎22 𝑎23
𝑎31 𝑎32 𝑎33
]

