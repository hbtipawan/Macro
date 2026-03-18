import streamlit as st
import datetime

st.set_page_config(page_title="Test App", page_icon="✅")

st.title("✅ Streamlit Cloud Test App")

st.write(
    "If you can see this page, "
    "Streamlit Cloud successfully installed requirements and ran the app."
)

st.write("Current time (server):", datetime.datetime.now())

st.subheader("Simple chart")
st.line_chart([1, 5, 2, 6, 3, 8])

st.info(
    "Next step: once this test works, "
    "put back your real `app.py` for the macro dashboard."
)
