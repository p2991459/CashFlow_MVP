import streamlit as st
import pandas as pd

st.title('Past Due Prediction')
uploaded_file = st.file_uploader("Upload CSV file for the Customer", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    total_current_amount = df['Current'].sum()
    past_due_ranges = [col for col in df.columns if 'Past Due' in col]
    frequency_counter = df[past_due_ranges].apply(lambda x: x.gt(0)).sum()
    most_frequent_range = frequency_counter.idxmax()
    total_count = frequency_counter.sum()
    probabilities = frequency_counter / total_count
    max_probability_value = probabilities.max()
    st.write("From the given dataset probable month in which the user will pay is: ")
    data = {'month_range': past_due_ranges, 'current amount': [0] * len(past_due_ranges)}
    df_output = pd.DataFrame(data)
    df_output.loc[df_output['month_range'] == most_frequent_range, 'current amount'] = total_current_amount
    print(df_output)
    # Streamlit app
    st.title("Past Due Ranges")
    # Display the DataFrame
    st.write(df_output)
    st.write(most_frequent_range)
    # st.write("Probability of the Past Due Month is:")
    # st.write(f"{max_probability_value * 100:.2f} %")

else:
    st.info("Please upload a CSV file for a customer")




