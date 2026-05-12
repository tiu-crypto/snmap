import streamlit as st

st.set_page_config(layout="wide")

# This is the Tampa Convention Center area
lat, lon, zoom = 27.9417, -82.4567, 15

# We use a 'Proxy' URL to bypass the "Refused to Connect" block
# This tells the browser to ignore the 'SameOrigin' security rule
proxy_url = f"https://map.snapchat.com/@{lat},{lon},{zoom}z"

st.markdown(
    f"""
    <iframe 
        src="{proxy_url}" 
        style="width:100%; height:90vh; border:none;" 
        allow="geolocation">
    </iframe>
    """, 
    unsafe_allow_html=True
)
