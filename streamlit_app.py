import streamlit as st

# 1. Page Configuration (Fixed the function name)
st.set_page_config(
    layout="wide", 
    page_title="SnapChat Place Videos",
    initial_sidebar_state="collapsed"
)

# 2. CSS for 90% Width and Ultra-Compact Sizing
st.markdown("""
    <style>
    /* Constrain the main container to 90% and center it */
    .block-container {
        max-width: 90% !important;
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
        margin: auto;
    }

    /* Smaller Title to save vertical space */
    .main-title {
        text-align: center;
        font-size: 32px !important;
        font-weight: 700;
        margin-bottom: 10px;
        color: white;
    }

    /* Compact Section Headers */
    .section-header {
        text-align: center;
        font-size: 22px !important;
        font-weight: 600;
        margin-top: 5px;
        margin-bottom: 5px;
        color: #FFFC00;
    }
    
    /* Button height and font adjusted for no-scroll layout */
    div.stButton > button {
        width: 100%;
        height: 1.2em !important; 
        font-size: 22px !important; 
        font-weight: 700 !important;
        border-radius: 6px;
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

    /* Minimal spacing between elements */
    .element-container {
        margin-bottom: 2px !important;
    }
    
    hr {
        margin: 0.5em 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Updated Title
st.markdown("<h1 class='main-title'>📍 SnapChat Place Videos: Event Campus</h1>", unsafe_allow_html=True)

# 4. Section 1: Tampa Convention Center
places_cc = [
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

col1, col2 = st.columns(2, gap="small")
for i, place in enumerate(places_cc):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        if st.button(f"🎥 {place['name']}", key=f"cc_{i}", use_container_width=True):
            st.components.v1.html(f"<script>window.open('{place['url']}', '_blank').focus();</script>", height=0)

st.markdown("---")
st.markdown("<h2 class='section-header'>Additional Area Pages</h2>", unsafe_allow_html=True)

# 5. Section 2: Davis Island / Aviation
places_ext = [
    {"name": "Davis Island Boat Ramp", "url": "https://www.snapchat.com/place/davis-island-boat-ramp/5f069be0-9a6c-11e8-82fb-d72269707099"},
    {"name": "Davis Island Dog Beach", "url": "https://www.snapchat.com/place/davis-island-dog-beach/beda1a40-9992-11e8-85c0-efbb0e9de6fb"},
    {"name": "Davis Island Seaplane Basin", "url": "https://www.snapchat.com/place/davis-island-seaplane-basin/81856d74-9a6f-11e8-9fe2-0f545a5dee3b"},
    {"name": "Davis Island (General)", "url": "https://www.snapchat.com/place/davis-island/64bdcec4-cf98-47d3-9f7b-1fd77fd5836a"},
    {"name": "Seaplane Basin Park", "url": "https://www.snapchat.com/place/seaplane-basin-park/0ad6af44-67e6-4a62-b979-c596302dee0a"},
    {"name": "Atlas Aviation Tampa", "url": "https://www.snapchat.com/place/atlas-aviation-tampa/00cb3728-9992-11e8-9e2e-7bb77402d9f3"},
    {"name": "FlyVenture (Tampa)", "url": "https://www.snapchat.com/place/flyventure-(tampa)/66d7b1f4-bd98-11eb-88d9-63cdbc71d7ea"},
    {"name": "Sarasota Avionics", "url": "https://www.snapchat.com/place/sarasota-avionics-%26-maintenance/9222fea8-2f38-46a4-a46e-2f48bd4107b4"},
    {"name": "Vantage Aviation USA", "url": "https://www.snapchat.com/place/vantage-aviation-usa/4f32afbd-f74f-41b3-9856-85f0a75c613a"},
    {"name": "Icon Aircraft Hangar", "url": "https://www.snapchat.com/place/icon-aircraft-maintenance-hanger/3e2871a6-f7ec-4b49-9694-060718175aaa"},
    {"name": "Tampa Bay Boating Adv.", "url": "https://www.snapchat.com/place/tampa-bay-boating-adventures/7108a34e-4b45-4b3e-adef-c8afe9338b20"}
]

col3, col4 = st.columns(2, gap="small")
for i, place in enumerate(places_ext):
    target_col = col3 if i % 2 == 0 else col4
    with target_col:
        if st.button(f"🎥 {place['name']}", key=f"ext_{i}", use_container_width=True):
            st.components.v1.html(f"<script>window.open('{place['url']}', '_blank').focus();</script>", height=0)

# 6. Reverted Original Footer
st.markdown("---")
st.caption("Monitoring Note: If a page appears empty, there are currently no active public stories for that specific pinpoint. Check the 'Main Hall' links for general area activity.")
