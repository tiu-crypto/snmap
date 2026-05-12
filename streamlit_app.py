import streamlit as st

st.set_page_config(layout="wide", page_title="Tampa Convention Center Monitor")

st.title("📍 Tampa Convention Center: Place Monitor")
st.write("Snapchat prevents direct embedding of 'Place' stories. Click a location below to open its live public story feed in a mobile-optimized window.")

# Organising your specific links into a dictionary
places = {
    "Main Convention Center (Primary)": "https://www.snapchat.com/place/tampa-convention-center/5b7693b0-9993-11e8-a4fc-8f3710c4f516",
    "Convention Center (Alt 1)": "https://www.snapchat.com/place/tampa-convention-center/4c721098-9992-11e8-a3c7-3f18e2fcbcb0",
    "Convention Center (Alt 2)": "https://www.snapchat.com/place/tampa-convention-center/cc1f253a-1dab-11ef-95b4-87d640dd6763",
    "Parking Garage": "https://www.snapchat.com/place/tampa-convention-center-parking-garage/b4b754ae-9994-11e8-b2f2-83d351c2e93f",
    "Convention Center Marina": "https://www.snapchat.com/place/tampa-convention-center-marina/d24709af-589d-4240-989e-d974d9593675",
    "Channelside Dr. Loading Dock": "https://www.snapchat.com/place/tampa-convention-center-channelside-dr.-loading-dock/cec03b11-4c7d-4b54-a18a-21842f6f0b65",
    "Visitor Drop-off": "https://www.snapchat.com/place/tampa-convention-center-visitor-drop-off/bcba61f3-972b-4a2a-929f-7a0bfb3314a6",
    "Franklin St. Loading Dock": "https://www.snapchat.com/place/tampa-convention-center-franklin-st.-loading-dock/9d646f75-7179-4ed6-bed7-34d86a012238",
    "Garage (Secondary)": "https://www.snapchat.com/place/tampa-convention-center-garage/727b08e5-b21c-4975-bd11-3e63af42a8f5",
    "Embassy Suites (Convention Center)": "https://www.snapchat.com/place/embassy-suites-by-hilton-tampa-downtown-convention-center/b12432d8-9991-11e8-9b53-031ff0c2500f"
}

# Creating a grid of buttons
cols = st.columns(2)
for i, (name, url) in enumerate(places.items()):
    with cols[i % 2]:
        if st.button(f"🔗 View {name}", use_container_width=True):
            # This JS opens the link in a way that bypasses the frame block
            js = f"window.open('{url}', '_blank').focus();"
            st.components.v1.html(f"<script>{js}</script>", height=0)

st.divider()
st.info("Pro-Tip: When the new window opens, press F12 and toggle the Device Toolbar (Mobile Icon) to see the stories in the high-res mobile format.")
