import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dynamic Dynamic pressure profile")

st.sidebar.title("Inputs")

k = st.sidebar.slider("permeability (md)", min_value=10, max_value=200, value=100)

mu = st.sidebar.slider("viscosity (cp)", min_value=10, max_value=50, value=15)

q = st.sidebar.slider("flow rate (stb/day)", min_value=100, max_value=500, value=200)

re = st.sidebar.number_input("outer radius of resevoir(ft)", min_value=100, max_value= 10000, value=4000)

rw = st.sidebar.number_input('Wellbore Radius (ft)',min_value=1,max_value=10,value = 1)

pe = st.sidebar.number_input('Pressure at the boundary of Reservoir(psi)',min_value = 100,max_value=10000, value =4000)

B = st.sidebar.number_input('Formation Volume Factor(bbl/stb)',min_value = 1,max_value=2, value =1)

h= st.sidebar.number_input('Net pay thickness of Reservoir (feet)',min_value = 2,max_value=500, value =30)

r = np.linspace(rw,re,1000)

P = pe - (141.2*q*mu*B*(np.log(re/r))/k/h)

y_min = P[np.where(r==rw)]

b = st.button("Show pressure Profile")

if b:
    plt.figure(figsize=(8,6))

    fig,ax = plt.subplots()

    ax.plot(r,P,linewidth =4)

    ax.grid(True)
    ax.axhline(y_min,linewidth = 4, color ="red")

    ax.set_xlabel("radius(feet)")
    ax.set_ylabel("Pressure at radius r, (PSI)")
    ax.set_title('Pressure Profile')
    ax.set_ylim(0,5000)


    st.pyplot(fig)