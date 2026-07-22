import streamlit as st
from youtube_analyzer import build_agent

agent = build_agent()
st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.title("🕵️‍♂️AI YouTube Analyzer")
st.subheader('You can Analyze any YouTube Video just by pasting Link')

v_link =st.text_input("Enter YouTube Video Link!")
button = st.button("Analyze✨")

if v_link and button :
    st.balloons()
    with st.spinner(text = "Analyzing..."):
        response = agent.run(
            f"Analyze this video : {v_link}"
        )
    st.markdown("Analysis Report of Video :")
    st.markdown(response.content)
    