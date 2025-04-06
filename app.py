import streamlit as st
import numpy as np

# Calculation Functions
def calculate_rwa(rt, phi):
    return rt * phi ** 2

def calculate_sw_archie(rw, rt, phi, a=1.0, m=2.0, n=2.0):
    if phi == 0 or rw == 0 or rt == 0:
        return 0.0
    f = a / phi**m
    sw = (f * rw / rt) ** (1/n)
    return min(max(sw, 0.0), 1.0)

def calculate_bvw(phi, sw):
    return phi * sw

def calculate_effective_porosity(density_log, matrix_density=2.65, fluid_density=1.0):
    return (matrix_density - density_log) / (matrix_density - fluid_density)

# Streamlit UI
st.title("🛢️ Petrophysics Calculator")
st.markdown("Calculate Rwa, Water Saturation (Sw), BVW, and optional Effective Porosity")

st.header("Input Parameters")

# Inputs
phi_percent = st.slider("Porosity (%)", min_value=0.0, max_value=35.0, value=15.0, step=0.1)
phi = phi_percent / 100

rt = st.slider("Total Resistivity (Rt, Ohm·m)", min_value=0.2, max_value=200.0, value=20.0, step=0.1)
rw = st.number_input("Formation Water Resistivity (Rw,_
