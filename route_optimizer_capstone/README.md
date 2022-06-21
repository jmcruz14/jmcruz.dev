# ROUTE-APP-PROJECT

### Rough notes (4/12/22)

The promised application is one that functions offline with online support.

But the prototype that we should deliver by Monday must ideally have online functionality in place.

#### Rough Project Stack
- Flask Web Framework
- Google ORTools API for Route Optimization and OSMPythonTools + osmnx for Map API
- Pandas for Data Cleaning, Sorting, and Analysis

#### Project Steps
- [x] Confirming initial project stack
- [x] Assembling raw data
- [x] Developing initial code and pseudocode equivalent
- [x] Spyder test run
- [x] Initialize on Dash
- [x] Integrate app function with Dash capabilities

#### Additional Notes on the Code
- What is the back-up map API to employ in case OpenStreetMap does not offer the location of interest?
- What modules are essential in overlaying the map with the generated route from OpenStreetMaps?
- Is there a way to employ Google OR-Tools with the generated nodes as the input and the OSM data as possible sources for the edges?
- How can we confirm an upload file before it releases the data?
- How can we improve the design of this application?* (Note: this is not a priority in design)

- The Waze Map is preloaded upon booting the application! (*Solved by uploading saved JSON fragments of Metro Manila + Greater NCR onto the file)
