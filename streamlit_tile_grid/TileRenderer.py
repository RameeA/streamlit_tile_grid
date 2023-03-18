import streamlit as st
import pandas as pd
import numpy as np

class TileGrid:
    def __init__(self, num_tiles=4, grid_size=2):
        self.num_tiles = num_tiles
        self.grid_size = grid_size

    def render(self, title_list, body_list, icon_list=None, tile_color="rgb(97, 218, 251)"):
        # Define the HTML for the tile grid
        html = """
                <head>
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
                </head>
                <div class='tile-grid'>
                """

        for i in range(self.num_tiles):
            # Define the HTML for each tile
            title = title_list[i] if i < len(title_list) else ""
            body = body_list[i] if i < len(body_list) else ""
            icon = f"<i class='bi-{icon_list[i]}'></i><br>" if icon_list and i < len(icon_list) and icon_list[i] else ""
            tile_html = f"<div class='tile'><h3>{icon} {title}</h3><p>{body}</p></div>"
            html += tile_html
        html += "</div>"
        # Add the HTML to the Streamlit app
        st.markdown(html, unsafe_allow_html=True)

        css = f"""        
        <style>
        .tile-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }}

        .tile {{
            background-color: {tile_color};
            border: 1px solid #ccc;
            padding: 15px;
            box-shadow: 0 5px 10px #4398af;
            border-radius: 5px;
            background: {tile_color};
            text-align: center;
            height: 200px;
            padding: 30px 20px;
            overflow-y: auto;
        }}

        .bi {{
            display: inline-block;
            font-size: 1.5rem;
            line-height: 1;
            font-family: 'Glyphicons Halflings';
            font-weight: normal;
            font-style: normal;
            text-transform: none;
            test-align: justify;
            speak: none;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}
        </style>
        """

        st.markdown(css, unsafe_allow_html=True)
