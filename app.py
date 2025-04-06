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
rw = st.number_input("Formation Water Resistivity (Rw, Ohm·m)", min_value=0.01, max_value=10.0, value=0.1, step=0.01, format="%.2f")

# Optional Archie parameters
with st.expander("Advanced Settings (Archie parameters)"):
    a = st.number_input("a (Tortuosity factor)", value=1.0)
    m = st.number_input("m (Cementation exponent)", value=2.0)
    n = st.number_input("n (Saturation exponent)", value=2.0)

# Calculations
rwa = calculate_rwa(rt, phi)
sw = calculate_sw_archie(rw, rt, phi, a, m, n)
bvw = calculate_bvw(phi, sw)

# Output
st.header("Results")
st.write(f"**Apparent Water Resistivity (Rwa):** {rwa:.4f} Ohm·m")
st.write(f"**Water Saturation (Sw):** {sw:.4f} (fraction)")
st.write(f"**Bulk Volume Water (BVW):** {bvw:.4f}")

# Optional Effective Porosity
st.header("Optional: Effective Porosity from Density")
use_density = st.checkbox("Calculate Effective Porosity?")
if use_density:
    rho = st.number_input("Formation Bulk Density (g/cc)", min_value=1.0, max_value=3.0, value=2.3, step=0.01)
    eff_phi = calculate_effective_porosity(rho)
    st.write(f"**Effective Porosity:** {eff_phi * 100:.2f}%")

st.markdown("---")
st.info("Formulas used:\n- Rwa = Rt × φ²\n- Sw = ((a × Rw) / (Rt × φ^m)) ^(1/n)\n- BVW = φ × Sw")
