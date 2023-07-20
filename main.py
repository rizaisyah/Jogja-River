import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
df = pd.read_csv("data.csv")

def filter_data(df, parameter, year):
    filtered_data = df[(df['Parameter'] == parameter) & (df['Tahun'] == year)]
    return filtered_data

# Function to plot average concentration for a given dataset
def plot_avg_concentration(filtered_data, parameter, year):
    # Calculate the average concentration for each month
    avg_concentration_by_month = filtered_data.groupby('Bulan')['Konsentrasi'].mean().reset_index()

    # Create a plot using seaborn
    plt.figure(figsize=(10, 6))

    sns.barplot(x='Bulan', y='Konsentrasi', data=avg_concentration_by_month)
    plt.title(f'Average Concentration for Parameter: {parameter}, Year: {year}')
    plt.xlabel('Month')
    plt.ylabel('Average Concentration')
    plt.xticks(rotation=45)

    st.pyplot(plt)  # Display the plot using Streamlit

# Streamlit app
def main():
    st.title('Concentration Dashboard')

    # Filter unique values of 'Year'
    unique_years = df['Tahun'].unique()

    # Selectbox to choose the 'Year'
    selected_year = st.selectbox('Select Year', unique_years)

    # Filter the data based on selected 'Parameter' and 'Year'
    filtered_data = filter_data(df, selected_year)

    # Display the plot for the filtered data
    plot_avg_concentration(filtered_data, selected_year)

if __name__ == '__main__':
    main()