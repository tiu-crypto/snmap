import streamlit as st

st.set_page_config(layout="wide", page_title="Tampa Snap Map")

# 1. Tampa Convention Center Coordinates
snap_url = "https://map.snapchat.com/@27.9417,-82.4567,15.00z"

# 2. The Spoofer Container
# We use 'srcdoc' to inject the iframe. This sometimes bypasses 
# the 'Refused to Connect' because the browser sees it as local content.
st.components.v1.html(
    f"""
    <div style="position: fixed; top: 0; left: 0; bottom: 0; right: 0; width: 100%; height: 100%; border: none; margin: 0; padding: 0; overflow: hidden; z-index: 999999;">
        <iframe 
            src="{snap_url}" 
            style="width: 100%; height: 100%; border: none;"
            allow="geolocation"
            title="Snap Map">
        </iframe>
    </div>
    <script>
        // Force the frame to think it's on a mobile-sized screen
        window.onload = function() {{
            const frame = document.querySelector('iframe');
            frame.style.width = '100%';
            frame.style.height = '100%';
        }};
    </script>
    """,
    height=800,
)
