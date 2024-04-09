import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic Survival Dataset
titanic_data = sns.load_dataset('titanic')

# Title and Overview
st.title('Titanic Survival Analysis')
st.markdown("""
This app provides an exploratory analysis of the Titanic Survival Dataset.

The dataset contains information about passengers aboard the Titanic, including their survival status, age, sex, passenger class, and more.

You can use the sidebar widgets to filter the data and explore various visualizations.
""")

# Sidebar Filters
st.sidebar.subheader('Filter Data')
filter_sex = st.sidebar.multiselect('Select Sex', titanic_data['sex'].unique(), default=titanic_data['sex'].unique())
filter_class = st.sidebar.multiselect('Select Passenger Class', titanic_data['class'].unique(), default=titanic_data['class'].unique())
filter_age = st.sidebar.slider('Age Range', int(titanic_data['age'].min()), int(titanic_data['age'].max()), (10, 60))

# Apply Filters
filtered_data = titanic_data[
    (titanic_data['sex'].isin(filter_sex)) &
    (titanic_data['class'].isin(filter_class)) &
    (titanic_data['age'].between(filter_age[0], filter_age[1]))
]

# Visualization: Survival Rate by Sex
st.subheader('Survival Rate by Sex')
fig, ax = plt.subplots()
sns.barplot(x='sex', y='survived', data=filtered_data, ax=ax)
st.pyplot(fig)

# Visualization: Survival Rate by Passenger Class
st.subheader('Survival Rate by Passenger Class')
fig, ax = plt.subplots()
sns.barplot(x='class', y='survived', data=filtered_data, ax=ax)
st.pyplot(fig)

# Visualization: Age Distribution of Survivors and Non-Survivors
st.subheader('Age Distribution of Survivors and Non-Survivors')
fig, ax = plt.subplots(figsize=(10, 6))
sns.distplot(filtered_data[filtered_data['survived'] == 1]['age'], label='Survived', ax=ax)
sns.distplot(filtered_data[filtered_data['survived'] == 0]['age'], label='Not Survived', ax=ax)
ax.legend()
st.pyplot(fig)
