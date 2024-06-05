# Titanic Survival Analysis App

This is a Streamlit app that provides an exploratory analysis of the Titanic Survival Dataset. The dataset contains information about passengers aboard the Titanic, including their survival status, age, sex, passenger class, and more.

## Features

- Interactive data filtering using sidebar widgets
 - Filter data by sex (male or female)
 - Filter data by passenger class (First, Second, or Third)
 - Filter data by age range
- Visualizations
 - Survival rate by sex (bar chart)
 - Survival rate by passenger class (bar chart)
 - Age distribution of survivors and non-survivors (overlaid distribution plots)
- Explanatory markdown descriptions for each visualization

## Requirements

- Python 3.x
- Streamlit
- Pandas
- Matplotlib
- Seaborn

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required packages using pip:
```
pip install streamlit pandas matplotlib seaborn
```

or Install the required dependencies via ``` pip install -r requirements.txt ```
## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the Streamlit app using the following command:
   
```
streamlit run app.py
```

4. The app will open in your default web browser.
5. Use the sidebar widgets to filter the data based on sex, passenger class, and age range.
6. Explore the visualizations, which will update based on the applied filters.
7. Read the markdown descriptions for each visualization to better understand the insights they provide.

## Data Source

The Titanic Survival Dataset used in this app is provided by the Seaborn library. It is a well-known dataset commonly used for exploratory data analysis and machine learning tasks.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Titanic Survival Dataset is provided by the Seaborn library.
