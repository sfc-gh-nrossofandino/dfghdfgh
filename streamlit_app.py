import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns


def main():
    st.title("Welcome to Streamlit!")

    st.write("This is a simple Streamlit app that welcomes you.")
    df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(df)

    name = st.text_input("What's your name?")
    if name:
        st.write(f"Hello, {name}! Welcome to your first Streamlit app.")


if __name__ == "__main__":
    sns.set(style="whitegrid")
    main()
