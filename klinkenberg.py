import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Reservoir Engineering Application")
st.sidebar.title( "klinkenberg Effect")

st.sidebar.title("User Inputs")


kg = st.sidebar.number_input("Enter Gas Permeability(md)", min_value=15, max_value=200, value=20)
pm = st.sidebar.number_input("Enter the mean Pressure(psi)", min_value=1, max_value=10, value=4)
k = st.sidebar.number_input("Enter the intial guess of absolute permeability(md)", min_value=1, max_value=1000, value=100)

b = st.button("Run klinkenberg Effect") 

if b:

        count = 0
        st.write(f"The value of kl_{count} is {k}")

        while (abs(6.9*(k**0.64)+pm*k-pm*kg)>0.000000000001):
            st.write("========================")
            updated_value = (6.9*(k**0.64)+pm*k-pm*kg)/(4.416*(k**(-0.36)) + pm) #f(k_l)/f'(k_l)
            k = k - updated_value
            count = count+1
            st.write(f"The value of kl_{count} is {k}")
            

        st.write(f"The final value of Perm K is : {k}")

        m = (kg-k)/((1/pm)-0)
        x_axis = np.linspace(0,1,200)
        y_axis = m*x_axis+k

        plt.style.use("classic")
        plt.figure(figsize=(10,8))

        fig,ax = plt.subplots()

        ax.plot(x_axis, y_axis,label="klinkerberg curve")

        ax.scatter(1/pm,kg,s=10,color="red",label ="lab condition reading")
        ax.axhline(k,color="black",lw=4,label = f"absolute permeability: {k} md")  

        ax.set_xlim(0,1.02)
        ax.set_ylim(0,100)

        ax.set_xlabel("1/mean_pressure (psi^-1)")
        ax.set_ylabel("measured gas permeability(md)") 
        ax.legend()
        ax.set_title("the klinkenberg effect")
        ax.grid(True)

        st.pyplot(fig)