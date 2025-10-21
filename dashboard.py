import streamlit as st
import json
from ai_generator import generate_marketing_content
from crm_newsletter import send_newsletters
from performance_analysis import analyze_performance

st.title("NovaMind AI Marketing Dashboard")

# 1️⃣ AI 内容生成
st.header("1. Generate Marketing Content")
prompt = st.text_area("Enter your marketing topic:")
if st.button("Generate Content"):
    content = generate_marketing_content(prompt)
    st.text_area("Generated Content", content, height=300)

# 2️⃣ 发送 Newsletter
st.header("2. Send Newsletter")
if st.button("Send Newsletters"):
    send_newsletters()
    st.success("✅ Newsletters simulated successfully!")

# 3️⃣ Performance 分析
st.header("3. View Performance Data & AI Insights")
if st.button("Analyze Performance"):
    summary, data = analyze_performance()
    st.json(data)
    st.subheader("AI Performance Summary")
    st.text(summary)
