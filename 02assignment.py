import streamlit as st

# 🔧 Set custom background color using HTML
page_bg_color = """
<style>
body {
    background-color: #f2f2f2;
    color: #333333;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# 🎯 Title and Subheading with Style
st.markdown("<h1 style='color:#2E86C1;'>⚙ Universal Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#555555;'>Because time is precious—convert Length, Weight, and Time without wasting any!</h4>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

# 📢 Intro Text
st.markdown("#### 👋 Welcome!")
st.write("Ready to convert? Pick a category, enter your number, and get real-time results!")

# 🧭 Layout Columns for cleaner interface
col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("📁 Choose a category", ["Length", "Weight", "Time"])

with col2:
    value = st.number_input("✍️ Enter the value to convert", min_value=0.0)

# 🔁 Unit options based on category
if category == "Length":
    unit = st.selectbox("📏 Pick a Conversion Option", ["Miles to Kilometers", "Kilometers to Miles"])

elif category == "Weight":
    unit = st.selectbox("⚖️ Pick a Conversion Option", ["Kilograms to Pounds", "Pounds to Kilograms"])

elif category == "Time":
    unit = st.selectbox("⏱️ Pick a Conversion Option", [
        "Seconds to minutes", "Minutes to seconds",
        "Minutes to hours", "Hours to minutes",
        "Hours to days", "Days to hours"
    ])

# 🧠 Conversion Logic
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
    return None

# ✅ Convert Button
if st.button("🔄 Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"✅ The result is **{result:.2f}**")
    else:
        st.error("Something went wrong with the conversion.")

# 🧾 Footer
st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
st.markdown("<small style='color:gray;'>Made with ❤️ using Python & Streamlit</small>", unsafe_allow_html=True)
