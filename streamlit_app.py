import streamlit as st

# 1. Page Configuration for a high-end dashboard look
st.set_page_config(
    layout="wide", 
    page_title="SnapChat Place Page Videos",
    initial_sidebar_state="collapsed"
)

# 2. Visual Styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #262730;
        color: white;
        border: 1px solid #464b5d;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        border-color: #FFFC00; /* Snapchat Yellow */
        color: #FFFC00;
    }
    .main-title {
        text-align: center;
        padding: 20px;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 class='main-title'>📍 SnapChat Place Page Videos: Tampa Convention Center</h1>", unsafe_allow_html=True)
st.markdown("---")

# 4. Data Organization
# I've grouped these to keep the grid balanced
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

# 5. Build the Grid
# Using 2 columns for a clean, balanced look
cols = st.columns(2)

for i, place in enumerate(places):
    col_idx = i % 2
    with cols[col_idx]:
        if st.button(f"🎥 {place['name']}", key=f"btn_{i}"):
            # JavaScript to open in new tab
            js = f"window.open('{place['url']}', '_blank').focus();"
            st.components.v1.html(f"<script>{js}</script>", height=0)

# 6. Footer Info
st.markdown("---")
st.caption("Monitoring Note: If a page appears empty, there are currently no active public stories for that specific pinpoint. Check the 'Main Hall' links for general area activity.")
