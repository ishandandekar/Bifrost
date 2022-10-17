import streamlit as st
import pickle
from script import Graph
print("Loading the object...")


@st.cache(allow_output_mutation=True)
def load_network() -> Graph:
    with open("network.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


st.set_page_config(page_title="BiFrost", page_icon=":train:", layout="wide")
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 2rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 0rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>BiFrost ⚡🚆</h1>",
            unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ## About the project

    """)
