import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dynamic circle")

st.sidebar.title("Input")

r=st.sidebar.slider("enter the radius of circle",min_value=0, max_value=25, value= 10)

x = np.linspace(-r,r,1000)

y_p = (r**2 - x**2)**0.5

y_n = -y_p

b = st.sidebar.button(f"create circle of radius {r}")

if b:
    st.write(f"circle creation of radius{r}")

    plt.style.use("classic")

    plt.figure(figsize=(8,8))

    fig,ax = plt.subplots()

    ax.plot(x,y_p,linewidth =4)

    ax.plot(x,y_n,linewidth =4)

    ax.set_title("circle")
    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)

    st.pyplot(fig)
