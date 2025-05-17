import time
import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from models import generate_sample_data
from screens import zombie, home, dragons, robots
from themes import load_css, create_header_navigation

def main():
    # Load CSS and initialize session state
    load_css()
    
    # Initialize session state
    if 'data' not in st.session_state:
        st.session_state.data = None
    if 'theme' not in st.session_state:
        st.session_state.theme = "welcome"
    if 'model_results' not in st.session_state:
        st.session_state.model_results = None
    if 'prev_page' not in st.session_state:
        st.session_state.prev_page = "welcome"
    
    # Header navigation
    create_header_navigation()
    
    # Page routing
    query_params = st.query_params

    current_page = query_params.get("page", "welcome")

    if(st.session_state.prev_page != current_page):
        st.session_state.model_results = None
        st.session_state.prev_page = current_page
    
    if current_page == "zombie":       
        zombie.render()
    elif current_page == "robots":
        robots.render()
    elif current_page == "dragons":
        dragons.render()
        
    else:
        home.render_welcome_page()

if __name__ == "__main__":
    main()