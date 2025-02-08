import streamlit as st


st.title("My first app")
st.write("Hello, world!")


# st.title("Greeting App")
# name = st.text_input("Enter your name")
# if name:
#     st.write(f"Hello, {name}! 👋")


# st.title("Number Multiplier")
# num = st.slider("Select a number:",1,10)
# calculate = st.button("calculate")
# if calculate:
#     square = num * num 
#     st.write("the square of the number is:",square)


# import pandas as pd
# import numpy as np

# st.title("Simple line chart")
# data = pd.DataFrame({
#     'x': np.arange(1,11),
#     'y': np.random.randn(10)
# })
# st.line_chart(data, x='x', y='y')


# import pandas as pd
# st.title("file upload")
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     st.dataframe(data.head)