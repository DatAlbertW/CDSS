import streamlit as st

def reset():
    st.session_state.clear()
    st.experimental_rerun()

def main():
    st.title("STI Genital Ulcers Decision Tree")


