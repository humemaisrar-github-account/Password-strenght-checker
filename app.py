import streamlit as st
import re

# 🌟 Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# 🔐 App Title
st.title("🔐 Ultimate Password Strength Meter")
st.caption("Secure your online presence with strong, reliable passwords.")

# 📘 Description
st.markdown("""
Create passwords that protect you. This tool checks for:
- 🔢 Minimum 8 characters
- 🔡 Uppercase & lowercase letters
- 🔢 At least one number
- 🔣 Special characters (!@#$%^&*)

**➡️ Enter your password below to check its strength.**
""")

# 🔑 Password Input
password = st.text_input("Enter your password", type="password", placeholder="Type your secure password here...")

# 🛡️ Password Strength Logic
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Your password should be **at least 8 characters** long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔴 Use **both uppercase and lowercase** letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔴 Add at least **one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🔴 Include **at least one special character (!@#$%^&*)**.")

    return score, feedback

# 🔍 Check Button
if st.button("🔍 Check Password"):
    if password:
        score, feedback = check_password_strength(password)
        st.subheader("🔎 Result:")

        if score == 4:
            st.success("✅ Excellent! Your password is strong and secure.")
        elif score == 3:
            st.warning("⚠️ Good! But you can make it stronger.")
        elif score == 2:
            st.warning("⚠️ Weak! Your password needs improvement.")
        else:
            st.error("❌ Very Weak! Please improve your password immediately.")

        if feedback:
            st.info("🛠️ Suggestions to improve your password:")
            for tip in feedback:
                st.markdown(f"- {tip}")
    else:
        st.error("🚨 Please enter a password to check.")

 # 🌍 Footer
st.markdown("""
---
<div style='text-align: center; font-size: 16px;'>
    © Created by <strong>Humema Israr</strong>
</div>
""", unsafe_allow_html=True)


