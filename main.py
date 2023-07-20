import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from csv
df = pd.read_csv("data.csv")

def filter_data(df, year, place):
    filtered_data = df[(df['Tahun'] == year) & (df['Nama Lokasi'] == place)]
    return filtered_data

# Function to plot average concentration for a given dataset
def plot_avg_concentration(filter_data, year, place):
    for parameter_value in filter_data['Parameter'].unique():
        params = filter_data[filter_data['Parameter'] == parameter_value]
        # Calculate the average concentration for each month
        avg_concentration_by_month = params.groupby('Bulan')['Konsentrasi'].mean().reset_index()

        # Create a plot using seaborn
        plt.figure(figsize=(10, 6))

        sns.barplot(x='Bulan', y='Konsentrasi', data=avg_concentration_by_month)
        plt.title(f'Average Concentration for Parameter: {parameter_value}\n At {place} Year {year}\n')
        plt.xlabel('Month')
        plt.ylabel('Average Concentration')
        plt.xticks(rotation=45)

        # for i in range(len(avg_concentration_by_month)):
        #     value = float(avg_concentration_by_month['Konsentrasi'][i])
        #     plt.text(avg_concentration_by_month['Bulan'][i], value, str(value), ha='center')

        st.pyplot(plt)  # Display the plot using Streamlit

# Streamlit app
def main():
    st.title('Concentration Distribution Dashboard by Parameter')

    # Filter unique values of 'Place' and 'Year'
    unique_years = df['Tahun'].unique()
    unique_place = df['Nama Lokasi'].unique()

    # Selectbox to choose the 'Year'
    selected_year = st.selectbox('Select Year', unique_years)
    selected_place = st.selectbox('Select Place', unique_place)

    # Filter the data based on selected 'Place' and 'Year'
    filtered_data = filter_data(df, selected_year, selected_place)

    # Display the plot for the filtered data
    plot_avg_concentration(filtered_data, selected_year, selected_place)

if __name__ == '__main__':
    main()