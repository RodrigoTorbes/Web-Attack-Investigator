import streamlit as st

from scripts.parser import parse_log
from scripts.attack_detector import detect_sqli, detect_traversal

df = parse_log("data/access.log")

sqli = detect_sqli(df)
traversal = detect_traversal(df)

st.title("Web Attack Investigator")

st.metric("Total Requests", len(df))
st.metric("Unique IPs", df["IP"].nunique())

st.subheader("Top IPs")
st.bar_chart(df["IP"].value_counts())

st.subheader("HTTP Status")
st.bar_chart(df["Status"].value_counts())

st.subheader("SQL Injection")
st.dataframe(sqli)

st.subheader("Directory Traversal")
st.dataframe(traversal)