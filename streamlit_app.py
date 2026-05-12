import streamlit as st

# 1. Page Configuration
st.set_page_config(
    layout="wide", 
    page_title="SnapChat Place Videos",
    initial_sidebar_state="collapsed"
)

# 2. CSS for 90% Width, Large Font, and Centering
st.markdown("""
    <style>
    /* Constrain the main container to 90% and center it */
    .block-container {
        max-width: 90% !important;
        padding-top: 2rem;
        margin: auto;
    }

    /* Centering and sizing the Title */
    .main-title {
        text-align: center;
        font-size: 48px !important;
        font-weight: 700;
        margin-bottom: 40px;
        color: white;
    }
    
    /* Double the font size for the labels (approx 44px) */
    div.stButton > button {
        width: 100%;
        height: 3.5em !important; 
        font-size: 44px !important; 
        font-weight: 700 !important;
        border-radius: 8px;
        background-color: #262730;
        color: white;
        border: 1px solid #464b5d;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    div.stButton > button:hover {
        border-color: #FFFC00;
        color: #FFFC00;
    }

    /* Standardized row spacing */
    .element-container {
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Updated Title
st.markdown("<h1 class='main-title'>📍 SnapChat Place Videos: Tampa Convention Center</h1>", unsafe_allow_html=True)

# 4. Links Data
places = [
    {"name": "Main Hall (Primary)", "url": "https://www.snapchat.com/place/tampa-convention-center/5b7693b0-9993-11e8-a4fc-8f3710c4f516"},
    {"name": "Main Hall (Alt 1)", "url": "https://www.snapchat.com/place/tampa-convention-center/4c721098-9992-11e8-a3c7-3f18e2fcbcb0"},
    {"name": "Main Hall (Alt 2)", "url": "https://www.snapchat.com/place/tampa-convention-center/cc1f253a-1dab-11ef-95b4-87d640dd6763"},
    {"name": "Embassy Suites Hotel", "url": "https://www.snapchat.com/place/embassy-suites-by-hilton-tampa-downtown-convention-center/b12432d8-9991-11e8-9b53-031ff0c2500f"},
    {"name": "Parking Garage (Main)", "url": "https://www.snapchat.com/place/tampa-convention-center-parking-garage/b4b754ae-9994-11e8-b2f2-83d351c2e93f"},
    {"name": "Parking Garage (Secondary)", "url": "https://www.snapchat.com/place/tampa-convention-center-garage/727b08e5-b21c-4975-bd11-3e63af42a8f5"},
    {"name": "Visitor Drop-off Area", "url": "https://www.snapchat.com/place/tampa-convention-center-visitor-drop-off/bcba61f3-972b-4a2a-929f-7a0bfb3314a6"},
    {"name": "Convention Center Marina", "url": "https://www.snapchat.com/place/tampa-convention-center-marina/d24709af-589d-4240-989e-d974d9593675"},
    {"name": "Channelside Loading Dock", "url": "https://www.snapchat.com/place/tampa-convention-center-channelside-dr.-loading-dock/cec03b11-4c7d-4b54-a18a-21842f6f0b65"},
    {"name": "Franklin St. Loading Dock", "url": "https://www.snapchat.com/place/tampa-convention-center-franklin-st.-loading-dock/9d646f75-7179-4ed6-bed7-34d86a012238"}
]

# 5. Centered Grid Layout
col1, col2 = st.columns(2, gap="large")

for i, place in enumerate(places):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        if st.button(f"🎥 {place['name']}", key=f"btn_{i}", use_container_width=True):
            js = f"window.open('{place['url']}', '_blank').focus();"
            st.components.v1.html(f"<script>{js}</script>", height=0)

# 6. Reverted Original Footer
st.markdown("---")
st.caption("Monitoring Note: If a page appears empty, there are currently no active public stories for that specific pinpoint. Check the 'Main Hall' links for general area activity.")
