import streamlit as st
import numpy as np
import pandas as pd

st.subheader("ECD Calculator")
mw = st.sidebar.number_input("enter the mud weight value (ppg): ")
apl = st.sidebar.number_input("enter the annular pressure loss value(psi): ")
tvd = st.sidebar.number_input("enter the true vertical depth (ft): ")
ecd = ((apl/(0.052*tvd))+mw)
st.write(f"the equivalent density on this tvd {tvd}ft is {ecd}")