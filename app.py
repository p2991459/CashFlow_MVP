import streamlit as st
import pandas as pd

st.title('Past Due Prediction')
uploaded_file = st.file_uploader("Upload CSV file for the Customer", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    past_due_ranges = [col for col in df.columns if 'Past Due' in col]
    frequency_counter = df[past_due_ranges].apply(lambda x: x.gt(0)).sum()
    most_frequent_range = frequency_counter.idxmax()
    total_count = frequency_counter.sum()
    probabilities = frequency_counter / total_count
    max_probability_value = probabilities.max()
    st.write("From the given dataset probable month in which the user will pay is: ")
    st.write(most_frequent_range)
    st.write("Probability of the Past Due Month is:")
    st.write(f"{max_probability_value * 100:.2f} %")

else:
    st.info("Please upload a CSV file for a customer")




