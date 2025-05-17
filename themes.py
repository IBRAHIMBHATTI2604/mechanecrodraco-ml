import base64
from io import BytesIO
import random
import pandas as pd
import streamlit as st


zombie_quotes = {
   "general": [
    "It's not just brains I crave, it's patterns in the chaos.",
    "Markets fall, civilizations crumble — but data always rises from the dead.",
    "I analyze the living and the undead — all in the name of prediction.",
    "Preprocessing isn't a phase... it's survival."
]
 ,"success": [
    "I'm a zombie. I don't guess — I foresee the collapse before it comes.",
    "Why do we model? So we can resurrect our portfolios from the grave.",
    "It's not just instinct — it's my model's hunger for accuracy."
]

    ,
    "error": [
    "Sometimes the models rot... sometimes they turn on us.",
    "This dataset smells... wrong. Like something that died and didn’t stay dead.",
    "The prediction failed. It's time to bury it... and raise a better one."
]

}

robots_quotes = {
   "general": [
    "With great algorithms comes great computational efficiency.",
    "Just your friendly neighborhood data bot — optimized and operational.",
    "My pattern-detection module identifies trends in financial matrices.",
    "Processing... swinging through datasets at 10,000 rows per second."
]
,
   "success": [
    "Prediction confidence: 99%. My circuits are tingling with accuracy!",
    "Assisting one investor uplifts the entire network. Logic approved.",
    "Core protocol: Financial insight enables optimal market behavior."
]
 ,"error": [
    "System malfunction: Neural net tangled. Recalibration required.",
    "Data anomaly detected. Initiating diagnostic cleanup sequence.",
    "No matter how advanced my code is, the noise always infiltrates."
]

    
}

dragons_quotes = {
    "general": [
    "The flight of clustering begins. It is... foretold by the ancients.",
    "Today, I breathe fire upon chaos — forging order from scattered data points.",
    "The realms of finance are vast, but all patterns leave trails in the skies.",
    "I call my clustering method... the dragon’s mercy."
]
,
   "success": [
    "Perfectly grouped, as all data realms should be.",
    "I soar above the dataset, watching the clusters settle in harmony.",
    "The hunt is over. The patterns have revealed themselves."
]
 ,"error": [
    "The fiercest flames are forged in the hardest decisions — and failed models.",
    "Even a dragon cannot fix what is corrupted at its core.",
    "Cursed data haunts this land — not even fire can cleanse it fully."
]

    
}



def load_css():
    
    st.markdown("""
    <style>
    /* Common Styles */
    .superhero-welcome {text-align: center; margin-bottom: 2rem;}
    .quote-text {font-style: italic; font-size: 1.1rem; margin-bottom: 5px;}
    .quote-attribution {text-align: right; font-weight: bold;}
    .stButton>button {width: 100%;}
    .centered-header {text-align: center; margin-bottom: 20px;}
    .results-container {background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; margin-top: 20px;}
    
    /* zombie Theme */
    .zombie-panel {background: linear-gradient(#1a1a1a, #2c3e50); padding: 20px; border-radius: 10px; color: #e6e6e6; margin-bottom: 15px;}
    .zombie-quote {background-color: #1a1a1a; border-left: 5px solid #4169e1; padding: 15px; margin: 10px 0; color: #e6e6e6;}
    .zombie-header {font-family: 'Gotham', sans-serif; color: #e6e6e6; text-shadow: 2px 2px 4px #000000;}
    .zombie-button button {background-color: #4169e1; color: white;}
    .zombie-metric-container {background-color: #1a1a1a; padding: 10px; border-radius: 5px; margin: 5px; text-align: center;}
    .zombie-metric-label {color: #4169e1; font-weight: bold; font-size: 0.9rem;}
    .zombie-metric-value {color: white; font-size: 1.5rem; font-weight: bold;}
    
    /* robots Theme */
    .robots-panel {background: linear-gradient(#b71c1c, #0d47a1); padding: 20px; border-radius: 10px; color: white; margin-bottom: 15px;}
    .robots-quote {background-color: #b71c1c; border-left: 5px solid #0d47a1; padding: 15px; margin: 10px 0; color: white;}
    .robots-header {font-family: 'Comic Sans MS', cursive; color: #ff0000; text-shadow: 2px 2px 4px #000000;}
    .robots-button button {background-color: #0d47a1; color: white;}
    .robots-metric-container {background-color: #0d47a1; padding: 10px; border-radius: 5px; margin: 5px; text-align: center;}
    .robots-metric-label {color: #ff0000; font-weight: bold; font-size: 0.9rem;}
    .robots-metric-value {color: white; font-size: 1.5rem; font-weight: bold;}
    
    /* dragons Theme */
    .dragons-panel {background: linear-gradient(#4a148c, #7b1fa2); padding: 20px; border-radius: 10px; color: white; margin-bottom: 15px;}
    .dragons-quote {background-color: #4a148c; border-left: 5px solid #ffd700; padding: 15px; margin: 10px 0; color: white;}
    .dragons-header {font-family: 'Arial', sans-serif; color: #ffd700; text-shadow: 2px 2px 4px #4a148c;}
    .dragons-button button {background-color: #7b1fa2; color: white;}
    .dragons-metric-container {background-color: #4a148c; padding: 10px; border-radius: 5px; margin: 5px; text-align: center;}
    .dragons-metric-label {color: #ffd700; font-weight: bold; font-size: 0.9rem;}
    .dragons-metric-value {color: white; font-size: 1.5rem; font-weight: bold;}
    
    /* Download buttons */
    .download-button {
        display: inline-block;
        padding: 10px 15px;
        background-color: #2c3e50;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        margin-top: 10px;
        font-weight: bold;
        text-align: center;
    }
    .zombie-download {background-color: #00FF00;}
    .robots-download {background-color: #0000FF;}
    .dragons-download {background-color: #b71c1c;}
    
    /* Welcome page styling */
    .welcome-container {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://www.pexels.com/photo/person-walking-between-green-forest-trees-15286/');
        background-size: cover;
        padding: 30px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .hero-card {
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        transition: transform 0.3s;
        cursor: pointer;
    }
    .hero-card:hover {
        transform: scale(1.03);
    }
    .zombie-card {background: linear-gradient(#008000, #2c3e50); color: white;}
    .robots-card {background: linear-gradient(#2916F5, #0d47a1); color: white;}
    .dragons-card {background: linear-gradient(#800000, #7b1fa2); color: white;}
    .hero-team {margin-top: 30px; margin-bottom: 15px; text-align: center;}
    .dc-header {color: #0078f2; font-size: 28px; font-weight: bold; text-shadow: 1px 1px 3px black;}
    .marvel-header {color: #e62429; font-size: 28px; font-weight: bold; text-shadow: 1px 1px 3px black;}
    .hero-grid {display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; margin-top: 15px;}
    .hero-profile {text-align: center; background-color: rgba(0,0,0,0.5); padding: 15px; border-radius: 10px; transition: transform 0.2s; height: 240px;}
    .hero-profile:hover {transform: scale(1.05);}
    .hero-name {font-weight: bold; margin-top: 8px;}
    .hero-power {font-style: italic; font-size: 0.9em; color: #cccccc;}
    
    /* App Header Styling */
    .show {display: block;}
    .app-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 20px;
        background-color: #1a1a1a;
        margin-bottom: 20px;
        border-radius: 10px;
    }
    .app-title {
        font-size: 24px;
        font-weight: bold;
        color: white;
    }
    .header-controls {
        display: flex;
        align-items: center;
    }
                
    #MainMenu, header[data-testid="stHeader"], .stDeployButton {display: none !important;}

    .st-emotion-cache-1w723zb{
                padding: 2rem 1rem 10rem;}
    </style>
    
    """, unsafe_allow_html=True)

# Function to display themed quotes
def show_themed_quote(theme, category="general"):
    quotes = {
        "zombie": zombie_quotes,
        "robots": robots_quotes,
        "dragons": dragons_quotes
    }
    
    quote = random.choice(quotes.get(theme, {}).get(category, ["Data analysis is a hero's job."]))
    
    if theme == "zombie":
        st.markdown(f"""
        <div class="zombie-quote">
            <div class="quote-text">"{quote}"</div>
            <div class="quote-attribution">— zombie</div>
        </div>
        """, unsafe_allow_html=True)
    elif theme == "robots":
        st.markdown(f"""
        <div class="robots-quote">
            <div class="quote-text">"{quote}"</div>
            <div class="quote-attribution">— robots</div>
        </div>
        """, unsafe_allow_html=True)
    elif theme == "dragons":
        st.markdown(f"""
        <div class="dragons-quote">
            <div class="quote-text">"{quote}"</div>
            <div class="quote-attribution">— dragons</div>
        </div>
        """, unsafe_allow_html=True)

# Function to create download buttons for exporting data
def create_download_buttons(df, model_results, figures=None, theme="batman"):
    st.markdown("---")
    
    if theme == "zombie":
        st.markdown("""
        <div class="zombie-panel">
            <h3>🦇 zombies Evidence Locker</h3>
            <p>"Always keep the evidence. You never know when you'll need it."</p>
        </div>
        """, unsafe_allow_html=True)
        download_class = "zombie-download"
        prefix = "zombie_analysis"
        
    elif theme == "robots":
        st.markdown("""
        <div class="robots-panel">
            <h3>🕸️ robots Archive</h3>
            <p>"Gotta save this for my homework... I mean, for future reference!"</p>
        </div>
        """, unsafe_allow_html=True)
        download_class = "robots-download"
        prefix = "robots_analysis"
        
    else:  # thanos
        st.markdown("""
        <div class="dragons-panel">
            <h3>💎 dragons Archive</h3>
            <p>"A small price to pay for saving your analysis."</p>
        </div>
        """, unsafe_allow_html=True)
        download_class = "dragons-download"
        prefix = "dragons_analysis"
    
    # Export format selection
    export_format = st.radio("Choose export format:", ["Excel", "CSV", "PDF"], horizontal=True)
    
    if export_format == "Excel":
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer) as writer:
            df.to_excel(writer, sheet_name="Raw Data", index=True)
            
            # Write model results to another sheet
            if model_results:
                results_df = pd.DataFrame([model_results])
                results_df.to_excel(writer, sheet_name="Analysis Results", index=False)
        
        excel_data = excel_buffer.getvalue()
        b64 = base64.b64encode(excel_data).decode()
        href = f'<a href="data:application/vnd.ms-excel;base64,{b64}" download="{prefix}_report.xlsx" class="download-button {download_class}">Download Excel File</a>'
        st.markdown(href, unsafe_allow_html=True)
        
    elif export_format == "CSV":
        csv_buffer = BytesIO()
        df.to_csv(csv_buffer, index=True)
        csv_data = csv_buffer.getvalue()
        b64 = base64.b64encode(csv_data).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{prefix}_data.csv" class="download-button {download_class}">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)
        
    else:  # PDF
        st.info("Generating PDF report with analysis details and visualizations...")
        st.success("PDF report generated!")
        
        # In a real app, you'd generate a proper PDF here
        # This is a placeholder for demonstration
        pdf_data = b"Sample PDF data"
        b64 = base64.b64encode(pdf_data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{prefix}_report.pdf" class="download-button {download_class}">Download PDF Report</a>'
        st.markdown(href, unsafe_allow_html=True)

# Custom dropdown navigation
def create_header_navigation():
    col1, col2, col3, col4 = st.columns([2,3,3,3])
    with col1:
        if st.button("🏠 home "):
            st.query_params["page"] = "home"
            st.rerun()
    with col2:
        if st.button("🦇 zombie "):
            st.query_params["page"] = "zombie"
            st.rerun()
    with col3:
        if st.button("🕸️robots"):
            st.query_params["page"] = "robots"
            st.rerun()
    with col4:
        if st.button("💎 dragons"):
            st.query_params["page"] = "dragons"
            st.rerun()
    st.markdown("---")