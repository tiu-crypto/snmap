import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered", page_title="Mobile Snap Monitor")

# Custom CSS to make the app look like a phone frame
st.markdown("""
    <style>
    .block-container { padding: 0px; }
    .phone-frame {
        width: 375px;
        height: 812px;
        border: 12px solid #333;
        border-radius: 40px;
        margin: auto;
        overflow: hidden;
        background: black;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
        position: relative;
    }
    </style>
""", unsafe_allow_html=True)

# The Tampa Map Link
snap_url = "https://map.snapchat.com/@27.9417,-82.4567,15.00z"

st.write("### 📍 Downtown Tampa RTCC Feed")

# The Virtual Device
st.markdown('<div class="phone-frame">', unsafe_allow_html=True)

components.html(
    f"""
    <iframe 
        id="mobileFrame"
        src="{snap_url}" 
        width="375" 
        height="812" 
        style="border:none;"
        allow="geolocation">
    </iframe>
    <script>
        // Spoofing the Mobile Environment
        const frame = document.getElementById('mobileFrame');
        
        // This tells the iframe it is an iPhone
        const mobileUA = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1";
        
        Object.defineProperty(frame.contentWindow.navigator, 'userAgent', {{
            get: function () {{ return mobileUA; }}
        }});
    </script>
    """,
    height=812,
)

st.markdown('</div>', unsafe_allow_html=True)
