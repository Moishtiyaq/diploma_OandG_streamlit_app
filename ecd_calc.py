import streamlit as st
import numpy as np
import pandas as pd

st.subheader("ECD Calculator")
st.sidebar.title("User Inputs")
mw = st.sidebar.number_input("enter the mud weight value (ppg): ", value=9)
apl = st.sidebar.number_input("enter the annular pressure loss value(psi): ", value=350)
tvd = st.sidebar.number_input("enter the true vertical depth (ft): ", value=6000)
ecd = ((apl/(0.052*tvd))+mw)
b = st.button("Run ECD Calculator")
if b:
   st.write(f"the equivalent circulating density on this tvd {tvd}ft is {ecd}")