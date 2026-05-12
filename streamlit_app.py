import streamlit as st

st.title("Tampa Snap Map Monitor")

# A big, clean button that opens the map in a mobile-optimized window
if st.button("🚀 Launch Mobile Snap Map (Tampa)"):
    js = "window.open('https://map.snapchat.com/@27.9417,-82.4567,15.00z', '_blank').focus();"
    st.components.v1.html(f"<script>{js}</script>")

st.info("Snapchat's security blocks direct embedding on many dashboards. Use the button above to open the live Tampa feed in a dedicated window.")
