import time
import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from models import generate_sample_data

# Welcome page with hero information
def render_welcome_page():
    st.markdown("""
    <div class="welcome-container">
        <h1 class="centered-header">MechaNecroDraco ML
(Mecha = Robot, Necro = Zombie, Draco = Dragon)</h1>
        <h3 class="centered-header">Where Financial Data meets  Powers!</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    Welcome to the Multiverse of Financial ML Legends — where undead minds, sentient machines, and ancient dragons harness machine learning to tame the chaos of financial data.

🧟 Zombies resurrect buried trends with eerie intuition.  
🤖 Robots analyze with precision and cold logic.  
🐉 Dragons wield ancient wisdom to cluster and predict with fiery insight.

Choose your dimension — Zombie, Robot, or Dragon — and unlock the secrets of data-driven forecasting!

    """)
    
    # Quick access to hero pages
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="hero-card zombie-card">
            <h3>ZOMBIE</h3>
            <p>ZOMBIE's Linear Regression</p>
            <p><em>"Predicting values with undead precision"</em></p>
        </div>
        """, unsafe_allow_html=True)
        
    
    with col2:
        st.markdown("""
        <div class="hero-card robots-card">
            <h3>ROBOT</h3>
            <p>ROBOT's Logistic Regression</p>
            <p><em>"Classifying with ROBOTS accuracy"</em></p>
        </div>
        """, unsafe_allow_html=True)
        
    
    with col3:
        st.markdown("""
        <div class="hero-card dragons-card">
            <h3>DRAGON</h3>
            <p>DRAGON's K-Means Clustering</p>
            <p><em>"Perfectly balanced data grouping"</em></p>
        </div>
        """, unsafe_allow_html=True)
        
    
    
    
   
    
    # Data source section
    st.markdown("---")
    st.subheader("📊 Select Your Data Source")
    
    data_source = st.radio(
        "",
        ["Upload your own files", "Yahoo Finance API", "Sample Datasets"],
        horizontal=True,
    )
    
    # Conditional display based on data source selection
    if data_source == "Upload your own files":
        st.markdown("""
        <div class="zombie-panel">
            <h3>🦇 zombie's File Analyzer</h3>
            <p>"I'm good at puzzling through data others have missed."</p>
        </div>
        """, unsafe_allow_html=True)
        
        file_type = st.radio("Select file type:", ["CSV", "Excel"], horizontal=True)
        
        if file_type == "CSV":
            uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
            if uploaded_file is not None:
                try:
                    df = pd.read_csv(uploaded_file)
                    st.session_state.data = df
                    st.success("File successfully uploaded to the Batcomputer!")
                    st.dataframe(df.head())
                except Exception as e:
                    st.error(f"Error reading file: {e}")
        else:
            uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])
            if uploaded_file is not None:
                try:
                    df = pd.read_excel(uploaded_file)
                    st.session_state.data = df
                    st.success("File successfully uploaded to the Batcomputer!")
                    st.dataframe(df.head())
                except Exception as e:
                    st.error(f"Error reading file: {e}")
                
    elif data_source == "Yahoo Finance API":
        st.markdown("""
        <div class="spiderman-panel">
            <h3>DRAGON </h3>
            <p>"Your friendly neighborhood data collector is on the job!"</p>
        </div>
        """, unsafe_allow_html=True)
        
        ticker_symbol = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL, MSFT, GOOG)")
        period = st.select_slider("Select Time Period", 
                                options=["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"])
        
        if ticker_symbol:
            try:
                with st.spinner(f"Spider-Man is swinging through the web to fetch {ticker_symbol} data..."):
                    df = yf.download(ticker_symbol, period=period)
                    if not df.empty:
                        # Reset index to make Date a column
                        df = df.reset_index()
                        st.session_state.data = df
                        st.success(f"Thwip! Successfully fetched {ticker_symbol} data!")
                        st.dataframe(df.head())
                        
                        # Display a quick chart
                        fig = px.line(df, x='Date', y='Close', title=f'{ticker_symbol} Stock Price')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error("No data found. Is that ticker correct?")
            except Exception as e:
                st.error(f"My Spider-sense detected a problem: {e}")
                
    else:  # Sample Datasets
        st.markdown("""
        <div class="dragons-panel">
            <h3>💎 DRAGONS Infinity Datasets</h3>
            <p>"I call that... mercy. Providing you with perfectly balanced datasets."</p>
        </div>
        """, unsafe_allow_html=True)
        
        dataset_choice = st.selectbox(
            "Choose a sample dataset:",
            ["S&P 500 Historical", "Bitcoin Price History", "Stock Market Crash 2008", 
             "Tech Stocks Performance", "Financial Classification Data", "Market Clustering Dataset"]
        )
        
        if st.button("Snap! Get the Dataset"):
            with st.spinner("Balancing the universe... and your dataset"):
                # Add slight delay for effect
                time.sleep(1)
                
                # Generate appropriate sample data based on selection
                if "Classification" in dataset_choice:
                    df = generate_sample_data("binary")
                elif "Clustering" in dataset_choice:
                    df = generate_sample_data("cluster")
                else:
                    df = generate_sample_data("stock")
                
                st.session_state.data = df
                st.success(f"With a snap, Thanos has balanced the {dataset_choice} for you!")
                st.dataframe(df.head())