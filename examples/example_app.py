from streamlit_tile_grid import TileGrid
import streamlit as st

def app():
    st.set_page_config(layout="wide")
   
    # Define the number of tiles and grid size
    num_tiles = 4
    grid_size = 2


    title_list = ['Customer Lost Minutes', 'Super Metric <br> 99%', 'Title 3', 'Title 4']
    body_list = ['97%', '', 'Body 3', 'Body 4']
    icon_list = ['bell', 'book', 'people', 'download']

    # Create the tile grid component and render it
    tile_grid = TileGrid(num_tiles, grid_size)
    tile_grid.render(title_list, body_list, icon_list)

if __name__ == "__main__":
    app()