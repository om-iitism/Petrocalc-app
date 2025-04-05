import streamlit as st
import numpy as np

st.set_page_config(page_title="Petrophysical Calculator", layout="centered")
st.title("Petrophysical Calculator")

st.markdown("""
**Calculates:**
- Apparent Water Resistivity (Rwa)
- Archie Water Saturation (Sw)
- Compares Rwa to given Rw
""")

st.sidebar.header("Input Parameters")

# Input Fields
phi = st.sidebar.number_input("Porosity (\u03d5) [fraction, e.g., 0.25]", min_value=0.0, max_value=1.0, value=0.25)
rt = st.sidebar.number_input("Total Resistivity (Rt) [ohm·m]", min_value=0.01, value=10.0)
rw = st.sidebar.number_input("Water Resistivity (Rw) [ohm·m]", min_value=0.001, value=0.05)

# Archie Constants
a = st.sidebar.number_input("Archie 'a' constant", value=1.0)
m = st.sidebar.number_input("Archie 'm' exponent", value=2.0)
n = st.sidebar.number_input("Archie 'n' exponent", value=2.0)

# Calculations
rwa = phi**2 * rt
try:
    sw = ((a / (phi ** m)) * (rw / rt)) ** (1/n)
except ZeroDivisionError:
    sw = np.nan

# Display Outputs
st.subheader("Results")
st.metric("Apparent Water Resistivity (Rwa)", f"{rwa:.3f} ohm·m")
st.metric("Water Saturation (Sw)", f"{sw:.3f}")

# Interpretation
st.subheader("Interpretation")
if abs(rwa - rw) / rw < 0.2:
    st.success("Rwa is close to Rw: likely water-bearing zone.")
elif rwa > rw:
    st.warning("Rwa is significantly higher than Rw: possible hydrocarbon presence.")
else:
    st.info("Rwa is lower than Rw: check inputs or zone may be unusual.")
