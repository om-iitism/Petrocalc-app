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

# Input Fields# --- User Inputs ---
phi_percent = st.slider("Porosity (ϕ) in %:", min_value=0, max_value=50, step=1)
rt = st.slider("Total Resistivity (Rt) in ohm·m:", min_value=0, max_value=200, step=1)
rw = st.number_input("Formation Water Resistivity (Rw) in ohm·m:", min_value=0.0, step=0.1, format="%.1f")

# Convert porosity from % to fraction
phi = phi_percent / 100


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
