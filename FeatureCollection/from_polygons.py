'''
<table class="ee-notebook-buttons" align="left">
    <td><a target="_blank"  href="https://github.com/giswqs/earthengine-py-notebooks/tree/master/FeatureCollection/from_polygons.ipynb"><img width=32px src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" /> View source on GitHub</a></td>
    <td><a target="_blank"  href="https://nbviewer.jupyter.org/github/giswqs/earthengine-py-notebooks/blob/master/FeatureCollection/from_polygons.ipynb"><img width=26px src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" />Notebook Viewer</a></td>
    <td><a target="_blank"  href="https://mybinder.org/v2/gh/giswqs/earthengine-py-notebooks/master?filepath=FeatureCollection/from_polygons.ipynb"><img width=58px src="https://mybinder.org/static/images/logo_social.png" />Run in binder</a></td>
    <td><a target="_blank"  href="https://colab.research.google.com/github/giswqs/earthengine-py-notebooks/blob/master/FeatureCollection/from_polygons.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run in Google Colab</a></td>
</table>
'''

# %%
'''
## Install Earth Engine API
Install the [Earth Engine Python API](https://developers.google.com/earth-engine/python_install) and [geehydro](https://github.com/giswqs/geehydro). The **geehydro** Python package builds on the [folium](https://github.com/python-visualization/folium) package and implements several methods for displaying Earth Engine data layers, such as `Map.addLayer()`, `Map.setCenter()`, `Map.centerObject()`, and `Map.setOptions()`.
The magic command `%%capture` can be used to hide output from a specific cell. Uncomment these lines if you are running this notebook for the first time.
'''


# %%
# %%capture
# !pip install earthengine-api
# !pip install geehydro

# %%
'''
Import libraries
'''


# %%
import ee
import folium
import geehydro

# %%
'''
Authenticate and initialize Earth Engine API. You only need to authenticate the Earth Engine API once. Uncomment the line `ee.Authenticate()` 
if you are running this notebook for the first time or if you are getting an authentication error.  
'''


# %%
# ee.Authenticate()
ee.Initialize()

# %%
'''
## Create an interactive map 
This step creates an interactive map using [folium](https://github.com/python-visualization/folium). The default basemap is the OpenStreetMap. Additional basemaps can be added using the `Map.setOptions()` function. 
The optional basemaps can be `ROADMAP`, `SATELLITE`, `HYBRID`, `TERRAIN`, or `ESRI`.
'''

# %%
Map = folium.Map(location=[40, -100], zoom_start=4)
Map.setOptions('HYBRID')

# %%
'''
## Add Earth Engine Python script 

'''

# %%
Map.setCenter(-107, 41, 6)

fc = ee.FeatureCollection([
    ee.Feature(
        ee.Geometry.Polygon(
            [[-109.05, 41], [-109.05, 37], [-102.05, 37], [-102.05, 41]]),
        {'name': 'Colorado', 'fill': 1}),
    ee.Feature(
        ee.Geometry.Polygon(
            [[-114.05, 37.0], [-109.05, 37.0], [-109.05, 41.0],
             [-111.05, 41.0], [-111.05, 42.0], [-114.05, 42.0]]),
        {'name': 'Utah', 'fill': 2})
    ])

# Fill, then outline the polygons into a blank image.
image1 = ee.Image(0).mask(0).toByte()
image2 = image1.paint(fc, 'fill')  # Get color from property named 'fill'
image3 = image2.paint(fc, 3, 5)    # Outline using color 3, width 5.

Map.addLayer(image3, {
    'palette': ['000000', 'FF0000', '00FF00', '0000FF'],
    'max': 3,
    'opacity': 0.5
}, "Colorado & Utah")


# %%
'''
## Display Earth Engine data layers 

'''


# %%
Map.setControlVisibility(layerControl=True, fullscreenControl=True, latLngPopup=True)
Map