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
filter_sex = st.sidebar.multiselect('Select Sex', titanic_data['sex'].unique(), default=titanic_data['sex'].unique().tolist())
filter_class = st.sidebar.multiselect('Select Passenger Class', titanic_data['class'].unique(), default=titanic_data['class'].unique().tolist())
filter_age = st.sidebar.slider('Age Range', int(titanic_data['age'].min()), int(titanic_data['age'].max()), (10, 60))

# Apply Filters
filtered_data = titanic_data[
    (titanic_data['sex'].isin(filter_sex)) &
    (titanic_data['class'].isin(filter_class)) &
    (titanic_data['age'].between(filter_age[0], filter_age[1]))
]

# Visualization: Survival Rate by Sex
# Visualization: Survival Rate by Sex
st.subheader('Survival Rate by Sex')
st.markdown("""
This bar chart visualizes the survival rate of passengers based on their sex (male or female). The x-axis represents the 'sex' column, which has two categories: 'male' and 'female'. The y-axis represents the 'survived' column, which is a binary value (0 or 1) indicating whether the passenger survived or not.

The height of each bar corresponds to the mean value of the 'survived' column for each sex category. A higher bar indicates a higher survival rate for that particular sex. This chart can help identify if there was a significant difference in survival rates between males and females on the Titanic.
""")
fig, ax = plt.subplots()
sns.barplot(x='sex', y='survived', data=filtered_data, ax=ax)
st.pyplot(fig)

# Visualization: Survival Rate by Passenger Class
st.subheader('Survival Rate by Passenger Class')
st.markdown("""
This bar chart visualizes the survival rate of passengers based on their passenger class. The x-axis represents the 'class' column, which has three categories: 'First', 'Second', and 'Third'. The y-axis represents the 'survived' column, which is a binary value (0 or 1) indicating whether the passenger survived or not.

The height of each bar corresponds to the mean value of the 'survived' column for each passenger class category. A higher bar indicates a higher survival rate for that particular passenger class. This chart can help identify if there was a significant difference in survival rates between the different passenger classes on the Titanic.
""")
fig, ax = plt.subplots()
sns.barplot(x='class', y='survived', data=filtered_data, ax=ax)
st.pyplot(fig)

# Visualization: Age Distribution of Survivors and Non-Survivors
st.subheader('Age Distribution of Survivors and Non-Survivors')
st.markdown("""
This chart visualizes the age distribution of passengers who survived and those who did not survive using two overlaid distribution plots. The x-axis represents the 'age' column, which is a numerical value indicating the passenger's age. The y-axis represents the density or probability distribution of the ages.

The distribution plot with the label 'Survived' shows the age distribution of passengers who survived (where 'survived' == 1). The distribution plot with the label 'Not Survived' shows the age distribution of passengers who did not survive (where 'survived' == 0).

By comparing the two distributions, you can identify if there were any notable differences in the age distributions between survivors and non-survivors. For example, if one distribution is skewed towards younger or older ages compared to the other, it could indicate that age played a role in survival rates.
""")
fig, ax = plt.subplots(figsize=(10, 6))
sns.distplot(filtered_data[filtered_data['survived'] == 1]['age'], label='Survived', ax=ax)
sns.distplot(filtered_data[filtered_data['survived'] == 0]['age'], label='Not Survived', ax=ax)
ax.legend()
st.pyplot(fig)
