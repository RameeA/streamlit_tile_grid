# Streamlit Tile Grid 

Library to display tile grid/donut grid which can be used to showcase key metrics within a dashboard or other application. You can use bootstrap icons on the top of your tiles (https://icons.getbootstrap.com/). Example app deployed here https://rameea-streamlit-tile-grid-examplesexample-app-o022ba.streamlit.app/


## Installation

``` pip install streamlit-tile-grid ```

## Example

To run the example:

1) Install the library
2) Install plotly as it is required by the example.
3) In your terminal run ``` streamlit run examples/example_app.py```

![image](https://user-images.githubusercontent.com/37738513/227699904-247357fb-0fad-47aa-9bea-e5d5fe1bbcae.png)


## Tiles

```

from streamlit_tile_grid.TileRenderer import TileGrid
import streamlit as st

def app():
    st.set_page_config(layout="wide")
    st.sidebar.title("Streamlit Tile Grid")
    # Define the number of tiles and grid size
    num_tiles = 4

    # Add some widgets to the sidebar
    st.sidebar.header("Settings")
    tile_color = st.sidebar.color_picker("Tile Color", value="#61dafb")
    text_color = st.sidebar.color_picker("Text Color", value="#000")
    tile_shadow = st.sidebar.color_picker("Tile Shadow", value="#4398af")
    num_tiles = st.sidebar.number_input("Number of Tiles", min_value=1, max_value=20, value=num_tiles)

    title_list = ['Customer Lost Minutes', 'Precision <br> 99%', 'Retention Rate', 'Accuracy <br> 99%']
    body_list = ['97%', '', 'Retention rate measures the percentage of users ...', '']
    icon_list = ['bell', 'book', 'people', 'download']

    # Create the tile grid component and render it
    st.title('Tiles')
    tile_grid = TileGrid(num_tiles)
    tile_grid.render(title_list, body_list, icon_list, icon_size='1.5', tile_color=tile_color, tile_shadow=tile_shadow, text_color=text_color)

if __name__ == "__main__":
    app()
```

## Donuts 

```
from streamlit_tile_grid.DonutRenderer import DonutRenderer 
import streamlit as st

def app():
    st.set_page_config(layout="wide")
    st.sidebar.title("Streamlit Animated Donut Metrics")
    donut_params = [
            {
                "percent": 69,
                "data": "3450 widgets",
                "color": f"aqua"
            },
            {
                "percent": 30,
                "data": "1500 widgets",
                "color": "#d9e021"
            },
            {
                "percent": 20,
                "data": "50 widgets",
                "color": "#ed1e79"
            },
                {
                "percent": 81,
                "data": "3450 widgets",
                "color": "purple"
            },
            {
                "percent": 45,
                "data": "1500 widgets",
                "color": "green"
            },
            {
                "percent": 20,
                "data": "50 widgets",
                "color": "red"
            },
            
        ]
    # Create the tile grid component and render it
    st.title('Donut Metrics')
    donut_grid = DonutRenderer()
    donut_grid.render(donut_params)

if __name__ == "__main__":
    app()
```
