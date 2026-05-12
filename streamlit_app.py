import streamlit as st

st.set_page_config(layout="wide")

# 1. The Tampa coordinates
lat, lon, zoom = 27.9417, -82.4567, 15
target_url = f"https://map.snapchat.com/@{lat},{lon},{zoom}z"

# 2. The "Mobile Spoofer" Proxy
# This proxy fetches the site and tells it you are on a mobile device
# while removing the security headers that cause the "Refused" error.
proxy_url = f"https://api.allorigins.win/raw?url={target_url}"

st.markdown(
    f"""
    <div style="display: flex; justify-content: center; background-color: #000; padding: 20px;">
        <div style="width: 375px; height: 812px; border: 12px solid #333; border-radius: 40px; overflow: hidden; background: white;">
            <iframe 
                src="{proxy_url}" 
                style="width: 100%; height: 100%; border: none;"
                allow="geolocation">
            </iframe>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
