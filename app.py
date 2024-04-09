import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from torchvision.datasets import MNIST

# Load the MNIST dataset
mnist = MNIST(root='data', download=True)

# Prepare the data
X = mnist.data.numpy().reshape(-1, 28 * 28) / 255
y = mnist.targets.numpy()
data = pd.DataFrame(X, columns=[f'pixel_{i}' for i in range(28 * 28)])
data['label'] = y

# Streamlit app
st.title('MNIST Dataset Visualization')
st.markdown('This web app allows you to explore and visualize the MNIST dataset.')

# Filter data by label
label_filter = st.sidebar.selectbox('Select Label', sorted(data['label'].unique()))
filtered_data = data[data['label'] == label_filter]

# Display a random image from the filtered data
if not filtered_data.empty:
    random_index = np.random.choice(filtered_data.index)
    st.subheader(f'Random Image from Label {label_filter}')
    st.image(filtered_data.loc[random_index, filtered_data.columns[:-1]].values.reshape(28, 28), cmap='gray')

# Visualize the distribution of labels
st.subheader('Label Distribution')
fig, ax = plt.subplots()
sns.countplot(data=data, x='label', ax=ax)
st.pyplot(fig)

# Visualize the pixel intensity distributions
st.subheader('Pixel Intensity Distributions')
selected_pixels = st.multiselect('Select Pixels', data.columns[:-1], default=['pixel_0'])
fig, ax = plt.subplots()
for pixel in selected_pixels:
    sns.distplot(data[pixel], ax=ax, label=pixel)
ax.legend()
st.pyplot(fig)
