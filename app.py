import streamlit as st

st.set_page_config(page_title="Petrophysical Calculator", layout="centered")

st.title("🛢️ Petrophysical Calculator")
st.subheader("Calculate Apparent Water Resistivity and Water Saturation")

# --- User Inputs ---
phi_percent = st.slider("Porosity (ϕ) in %:", min_value=0, max_value=50, step=1)
rt = st.slider("Total Resistivity (Rt) in ohm·m:", min_value=0, max_value=200, step=1)
rw = st.number_input("Formation Water Resistivity (Rw) in ohm·m:", min_value=0.0, step=0.1, format="%.1f")

# Convert porosity from % to fraction
phi = phi_percent / 100

# --- Constants ---
a = 1
m = 2
n = 2

# --- Calculate Results ---
if phi > 0 and rt > 0:
    rw_app = phi**2 * rt

    try:
        sw = ((rw / (phi**m * rt)) ** (1 / n)) if rw > 0 else None

        # --- Output ---
        st.markdown("### 📊 Results")
        st.success(f"**Apparent Water Resistivity (Rw_app):** {rw_app:.4f} ohm·m")
        if sw is not None:
            st.success(f"**Water Saturation (Sw):** {sw:.4f} (fraction)")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Please enter valid values for porosity and Rt.")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
