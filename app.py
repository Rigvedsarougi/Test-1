import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read and display data from uploaded file
def load_data(file):
    if file is not None:
        data = pd.read_csv(file)
        return data
    return None

# Function to create dashboard based on uploaded data
def create_dashboard(data):
    if data is not None:
        st.write("### Data Preview")
        st.write(data.head())

        st.write("### Data Summary")
        st.write(data.describe())

        st.write("### Data Visualization")
        # Example: Plot a histogram
        plt.figure(figsize=(8, 6))
        sns.histplot(data['column_name'])
        st.pyplot()

# Main function to run the app
def main():
    st.title("Drag and Drop File Dashboard")

    st.write("Drag and drop a file here to generate a dashboard")

    # Allow users to upload a file
    file = st.file_uploader("Upload a file", type=["csv", "txt"])

    if file is not None:
        data = load_data(file)
        create_dashboard(data)

if __name__ == "__main__":
    main()
