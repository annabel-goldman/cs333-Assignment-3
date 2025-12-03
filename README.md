# Interactive Visualization for Florida Traffic Accidents During Jan-March 2023

## How to Run this Project Locally
1. Clone this repository
2. Install Anaconda or MiniConda: 
    https://www.anaconda.com/download 
    https://www.anaconda.com/docs/getting-started/miniconda/install
3. Open a terminal at the root of the cloned repository and run `conda env create -f environment.yml`.
3. Once the conda environment has been created, run `conda activate datacleaning`.
4. Obtain a csv file of our data set avalible at  
    https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data
5. Put the CSV file into the root of our repository and rename it "data.csv"
6. Run the jyptr notebook code 
7. Run `python -m http.server` in the root of this project.
8. Go to `localhost:8000`


## References Used

#### Raw Dataset
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data

#### Resources for setting up Conda and Pandas for data cleaning
https://saturncloud.io/blog/how-to-create-a-conda-environment-based-on-a-yaml-file-a-guide-for-data-scientists/
http://gist.github.com/raeidsaqur/72cc9b4cfff22081ccb34dc8292e3c91
https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp

#### Using Pandas/Numpy Sources
https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
https://stackoverflow.com/questions/31789160/convert-select-columns-in-pandas-dataframe-to-numpy-array
https://stackoverflow.com/questions/45577630/print-sample-set-of-columns-from-dataframe-in-pandas

#### Generating a blank U.S. map in D3:
https://billmill.org/making_a_us_map.html
https://medium.com/@amy.degenaro/introduction-to-digital-cartography-geojson-and-d3-js-c27f066aa84
https://d3js.org/d3-zoom
https://www.w3schools.com/howto/howto_css_zoom_hover.asp

#### Blank Florida Map GeoJson:
https://github.com/danielcs88/fl_geo_json

#### How to add our own data on top of a blank US map in D3:
https://observablehq.com/@d3/u-s-map
https://d3js.org/d3-geo/conic
https://d3js.org/d3-geo/path

#### Implementing sliders in D3:
https://www.geeksforgeeks.org/html/how-to-add-a-range-slider-using-html/
https://stackoverflow.com/questions/18389224/how-to-style-html5-range-input-to-have-different-color-before-and-after-slider
https://jsfiddle.net/esyvws3d/
https://stackoverflow.com/questions/4753946/html-slider-with-two-inputs-possible
https://codepen.io/vsync/pen/mdEJMLv


#### Chat Convo about GeoJSON
https://chatgpt.com/share/690f9723-07d8-800e-9946-1c58deb63a65
https://chatgpt.com/c/690f9693-73cc-8330-bbcc-b3a4c13f5af3


#### Calendar input
https://www.w3schools.com/TAGS/att_input_type_date.asp
https://stackoverflow.com/questions/32378590/set-date-input-fields-max-date-to-today

#### Contributors
Annabel Goldman 
Joanna Soltys