import streamlit as st

st.set_page_config(layout="wide")

# 1. Tampa Convention Center Coordinates
snap_url = "https://map.snapchat.com/@27.9417,-82.4567,15.00z"

# 2. The Proxy Magic
# This fetches the map content through a middleman that strips the security blocks.
proxy_url = f"https://api.allorigins.win/raw?url={encodeURIComponent(snap_url)}"

# Note: Since we can't easily use encodeURIComponent in pure Python here, 
# we use the direct proxied string below:
final_url = f"https://api.allorigins.win/raw?url=https://map.snapchat.com/@27.9417,-82.4567,15.00z"

st.markdown(
    f"""
    <div style="display: flex; justify-content: center; background-color: #0d1117; padding: 20px;">
        <div style="width: 375px; height: 812px; border: 12px solid #333; border-radius: 40px; overflow: hidden; background: white; box-shadow: 0 0 20px rgba(0,0,0,0.5);">
            <iframe 
                src="{final_url}" 
                style="width: 100%; height: 100%; border: none;"
                allow="geolocation">
            </iframe>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
