import streamlit as st
import numpy as np

st.title("Petrophysics Calculator")
st.subheader("Calculate Apparent Water Resistivity (Rwa) and Water Saturation (Sw)")

# Input: Porosity (%)
porosity_percent = st.slider("Porosity (%)", min_value=0.0, max_value=35.0, value=15.0, step=0.1)

# Input: Total Resistivity (Rt) - Logarithmic scale
rt_log = st.slider("Total Resistivity (Rt, Ohm·m)", min_value=0.2, max_value=200, value=15.0, step=0.1)
rt = 10 ** rt_log

# Input: Formation Water Resistivity (Rw)
rw = st.number_input("Formation Water Resistivity (Rw, Ohm·m)", min_value=0.01, max_value=10.0, value=0.1, step=0.01, format="%.2f")

# Convert Porosity to fraction
phi = porosity_percent / 100.0

# Calculate Rwa and Sw
rwa = rt * phi**2
sw = np.sqrt(rwa / rw)
sw = min(max(sw, 0.0), 1.0)

# Results
st.markdown("### Results:")
st.write(f"**Apparent Water Resistivity (Rwa):** {rwa:.4f} Ohm·m")
st.write(f"**Water Saturation (Sw):** {sw:.4f} (fraction)")

# Notes
st.markdown("---")
st.info("Formulas used:  \nRwa = Rt × φ²  \nSw = √(Rwa / Rw), limited between 0 and 1")
