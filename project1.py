import streamlit as st
import pandas as pd
import seaborn as sns

# Define the pages
Overview = st.Page("Overview.py", title="Overview", icon="🎈")
Result = st.Page("Result.py", title="Kết quả phân cụm", icon="❄️") 
Interaction = st.Page("Interaction.py", title="Trải nghiệm phân cụm", icon="🎉")

# Set up navigation
pg = st.navigation([Overview, Result, Interaction])

# Run the selected page
pg.run()

with st.sidebar:

    # Phần thông tin nhóm
    st.subheader("👨‍💻 Thực hiện bởi:")

    col1, col2 = st.columns(2)
    with col1:
        st.image("img/TBao.jpg", use_container_width=True)
        st.markdown("- Hồ Nguyễn Thiên Bảo")
    with col2:
        st.image("img/Khoa.jpg", use_container_width=True)
        st.markdown("- Nguyễn  \n  Anh Khoa") 
    
    # Add a horizontal line
    st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
    
    # Thông tin giảng viên
    st.subheader("👩‍🏫 Giảng viên hướng dẫn:")
    st.markdown("- Cô Khuất Thùy Phương")
    
    # Add another horizontal line
    st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
    
    # Ngày báo cáo
    st.subheader("📅 Ngày báo cáo:")
    st.markdown(f"<p style='font-size: 18px'>19/04/2024</p>", unsafe_allow_html=True)
