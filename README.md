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


D3 Sources
Resources for generating a blank U.S. map in D3:
https://billmill.org/making_a_us_map.html
https://medium.com/@amy.degenaro/introduction-to-digital-cartography-geojson-and-d3-js-c27f066aa84

Information about click handlers: 
Googled: how to get svg element clicked inside of d3 handler?
AI Overview: Inside a D3 event handler function, you have access to three key items: the current event object, the bound datum, and the DOM element itself. 
Here is how you can access them:
1. The Current Event (event)
The event object (commonly named event in modern D3 versions like v6 and later) is the first argument passed to the listener function. It provides standard DOM event properties such as event.clientX, event.pageY, event.type, and methods like event.preventDefault(). 
javascript
selection.on("click", (event, d) => {
  console.log(event.type); // e.g., "click"
});
For earlier D3 versions (v5 and below), this was accessed via the global variable d3.event. 
2. The Bound Datum (d)
The datum, typically named d, is the data element associated with the DOM element on which the event occurred. It is passed as the second argument to the listener function. This is crucial for creating data-driven interactions. 
javascript
selection.on("click", (event, d) => {
  console.log(d); // the data object bound to the element
});
3. The Current DOM Element (this)
The actual DOM element that triggered the event is available as the this context within the event handler function. You can use this to directly manipulate the element using native JavaScript methods or by re-selecting it with D3 (e.g., d3.select(this)). 
javascript
selection.on("click", function(event, d) { // Must use a non-arrow function to access 'this'
  console.log(this); // the DOM element (e.g., <circle>, <rect>)
  d3.select(this).style("fill", "orange");
});
For functions that use arrow syntax, this is lexically scoped and may not refer to the DOM element. In this case, event.currentTarget can be used to reference the element the event listener was attached to. 
https://www.w3schools.com/howto/howto_css_zoom_hover.asp


Resources for understanding how to add our own data on top of a blank US map:
https://observablehq.com/@d3/u-s-map 
https://d3js.org/d3-geo/conic
https://d3js.org/d3-geo/path

Blank U.S. Map GeoJson:
https://eric.clst.org/tech/usgeojson/

Pandas/Numpy Sources
https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
https://stackoverflow.com/questions/31789160/convert-select-columns-in-pandas-dataframe-to-numpy-array
https://stackoverflow.com/questions/45577630/print-sample-set-of-columns-from-dataframe-in-pandas

## Contributors
Annabel Goldman
Joanna Soltys