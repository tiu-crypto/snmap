import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Tampa Convention Center
snap_url = "https://map.snapchat.com/@27.9417,-82.4567,15.00z"

# This script creates an iframe but 'spoofs' the navigator.userAgent
# to make the site believe it is being viewed on an iPhone.
components.html(
    f"""
    <div id="map-container" style="width:100%; height:90vh;">
        <iframe 
            id="snapMap"
            src="{snap_url}" 
            width="100%" 
            height="100%" 
            style="border:none;"
            allow="geolocation">
        </iframe>
    </div>

    <script>
        const iframe = document.getElementById('snapMap');
        
        // We override the userAgent for the iframe's window
        Object.defineProperty(iframe.contentWindow.navigator, 'userAgent', {{
            get: function () {{ return 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'; }},
        }});
        
        Object.defineProperty(iframe.contentWindow.navigator, 'platform', {{
            get: function () {{ return 'iPhone'; }},
        }});
    </script>
    """,
    height=850,
)
