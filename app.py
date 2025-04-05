import streamlit as st

st.set_page_config(page_title="Petrophysical Calculator", layout="centered")

st.title("🛢️ Petrophysical Calculator")
st.subheader("Calculate Apparent Water Resistivity and Water Saturation")

# --- User Inputs ---
phi = st.number_input("Porosity (ϕ, fraction e.g., 0.25):", min_value=0.0, max_value=1.0, step=0.01, format="%.2f")
rt = st.number_input("Total Resistivity (Rt, ohm·m):", min_value=0.0, step=0.1, format="%.2f")
rw = st.number_input("Formation Water Resistivity (Rw, ohm·m):", min_value=0.0, step=0.01, format="%.2f")

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
