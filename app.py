# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",  # centered, wide
    initial_sidebar_state="auto",
    menu_items=None
)

st.title("🐧 Penguins Explorer")

df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

st.write(df)

# Create a scatter plot
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species", ax=ax)
ax.set_title("Penguin Bill Measurements")
ax.set_xlabel("Bill Length (mm)")
ax.set_ylabel("Bill Depth (mm)")

# Display the plot in Streamlit
st.pyplot(fig)
