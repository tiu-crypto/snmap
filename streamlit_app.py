import streamlit as st
import streamlit.components.v1 as components

# Fill the screen
st.set_page_config(layout="wide")

# The Tampa Link
snap_url = "https://map.snapchat.com/@27.9417,-82.4567,15.00z"

# New method: This embeds the map using a different HTML container
# that sometimes tricks the 'Refused to Connect' security check.
components.html(
    f"""
    <div style="width:100%; height:800px;">
        <embed src="{snap_url}" style="width:100%; height:100%;">
    </div>
    """,
    height=800,
)
