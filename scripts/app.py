import streamlit as st
import pickle
from script import Graph
import os

BASE_DIR = os.getcwd()


@st.cache(allow_output_mutation=True)
def load_network() -> Graph:
    with open(f"{os.path.join(os.path.join(BASE_DIR,'scripts'), 'network.pkl')}", 'rb') as f:
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
    ## Introduction

**BiFrost** is an AI application, which gives an optimal route between two places, based on the time taken for the journey. The algorithm for path ooptimization, is A-star search algorithm. The idea behind this project is to give the user better transportation options, when travelling using public transport. For example, if a person wants to go from Point A to Point B, you have multiple options. The algorithm then calculates a path considering the time taken for the journey to get the best path.  
In the early development stages, we used Mumbai(Maharashtra, India) and Navi Mumbai(Maharashtra, India). We got this data using the famous mobile app **M-Indicator**. The app shows real time details about train timings, which we felt was the best way to retrieve the data.  
This network of railway, is imitated as a **Graph** data structure. This made it easier to add the nodes (or stops/destinations). Further, if there is any development on creating better lines for transportation, adding to the network will be very easy.
We did this project as a part of our bachelor's degree for the Applied AI subject.

## Contributions

This project has been commenced under the [MIT License](LICENSE). Thus, making it open source.  
The project is still in its development phases and the developer(s) are always looking for improvements. If you want to contribute to this project in any sort of, please make a pull-request with the improved code and/or documentation.  
If you are interested in seeing the project grow, please star the project, it will be really motivating for us!
    """)
    st.markdown("""
    #### [Github](https://github.com/ishandandekar/Bifrost)""")

with col2:
    st.markdown("""
    ### See the route for yourself!""")
    network = load_network()
    nodes = network.vertices_
    start = st.selectbox("Select a start point", nodes, index=2)
    end = st.selectbox("Select an end point", nodes, index=65)

    path, time_taken = network.a_star_algorithm(start, end)
    if path == None:
        st.error("Path Not Found!")
    else:
        st.success(path)
        st.info(
            f'Time taken by this path is: {round(time_taken/60)} hours and {time_taken%60} minutes')
