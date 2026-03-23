import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration
st.set_page_config(
    page_title="AI Learning Hub | Class XI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    # Hide Streamlit's default header, footer, and padding to maximize space
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Get the directory where app.py is located
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the HTML file
    html_file_path = os.path.join(BASE_DIR, "cbse_ai_class12_v3.html")
    
    if os.path.exists(html_file_path):
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        st.components.class11_ai_oneshot_v2.html(html_content, height=1200, scrolling=True)
    else:
        st.error(f"Could not find the file: {html_file_path}. Please make sure you are running the app from the correct directory.")

if __name__ == "__main__":
    main()
