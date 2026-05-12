import streamlit as st

st.set_page_config(layout="wide", page_title="Tampa Snap Map")

# 1. The Tampa coordinates
lat, lon, zoom = 27.9417, -82.4567, 15

# 2. The Direct URL
target_url = f"https://map.snapchat.com/@{lat},{lon},{zoom}z"

# 3. The Proxy (This is the secret sauce)
# We use 'allorigins' to pull the site content through a different environment
# This prevents the "Refused to Connect" error by stripping the security headers
proxy_url = f"https://api.allorigins.win/raw?url={target_url}"

st.markdown(
    f"""
    <style>
        .reportview-container .main .block-container {{
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }}
        iframe {{
            width: 100%;
            height: 95vh;
            border: none;
        }}
    </style>
    <iframe src="{proxy_url}"></iframe>
    """,
    unsafe_allow_html=True
)
