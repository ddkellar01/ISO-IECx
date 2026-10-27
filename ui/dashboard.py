"""Streamlit dashboard interface for exploring ISO/IEC standards and generating video prompts."""
import streamlit as st
from scouts.iso_crawler import ISOScout
from workflows.google_flow_video import GoogleFlowVideoGenerator

st.title("ISO-IECx Intelligence & Google Flow Dashboard")

standard_id = st.text_input("Enter ISO/IEC Standard ID (e.g., 27001):", "27001")

if st.button("Scout & Generate Video Prompt"):
    scout = ISOScout()
    data = scout.scout_standard(standard_id)
    
    if "error" in data:
        st.error(f"Error fetching standard: {data['error']}")
    else:
        st.success(f"Loaded: {data['title']}")
        st.write(data['abstract'])
        
        generator = GoogleFlowVideoGenerator(char_limit=350)
        prompt = generator.format_video_description(standard_id, data['abstract'])
        
        st.subheader("Google Flow Video Prompt (<=350 Chars)")
        st.code(prompt)
        st.info(f"Character Count: {len(prompt)} / 350")
