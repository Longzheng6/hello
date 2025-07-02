import streamlit as st

st.title("加法器")
a = st.text_input("输入第一个数字")
b = st.text_input("输入第二个数字")
ab_sum = a + b
st.write(f"结果是{ab_sum}")