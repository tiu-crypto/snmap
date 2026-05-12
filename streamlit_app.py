import streamlit as st

# This makes the map fill the whole screen
st.set_page_config(layout="wide")

# The Tampa Convention Center Link
snap_url = "https://map.snapchat.com/@27.9417,-82.4567,15.00z"

# This creates the "Window" inside Streamlit
st.components.v1.iframe(snap_url, height=800, scrolling=True)
