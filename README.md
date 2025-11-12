# Interactive Visualization for U.S. Traffic Accidents from 2016-2023

## How to Run this Project
1) Make sure you have Anaconda installed on your machine, which can be done here: https://www.anaconda.com/download. It is sufficient to install the smaller version of it called Miniconda.
2) Once Anaconda is installed on your machine, clone this repository to obtain a local copy. Open a terminal at the root of the cloned repository and run `conda env create -f environment.yml`.
3) Once the conda environment has been created, run `conda activate datacleaning`.

## How to View Our Visualization Locally
1) Run `python -m http.server` in the root of this project.
2) Go to `localhost:8000` 
3) Click on the HTML file corresponding to the visualization you wish to see. 

## References Used
Raw Dataset: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data

Resources for setting up Conda and Pandas to make data cleaning on our large data set possible:
https://saturncloud.io/blog/how-to-create-a-conda-environment-based-on-a-yaml-file-a-guide-for-data-scientists/
http://gist.github.com/raeidsaqur/72cc9b4cfff22081ccb34dc8292e3c91
https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp

Resources for generating a blank U.S. map in D3:
https://billmill.org/making_a_us_map.html
https://medium.com/@amy.degenaro/introduction-to-digital-cartography-geojson-and-d3-js-c27f066aa84

Resources for understanding how to add our own data on top of a blank US map:
https://observablehq.com/@d3/u-s-map 
https://d3js.org/d3-geo/conic
https://d3js.org/d3-geo/path

## Contributors
Annabel Goldman
Joanna Soltys