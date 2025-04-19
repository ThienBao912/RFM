import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("""
<div style="background-color: #f9d990; padding: 10px; border-radius: 20px; text-align: center; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    <h1 style="color: #222; font-weight: 900; font-size: 36px; margin: 0;">CUSTOMER SEGMENTATION PROJECT</h1>
</div>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("img/rfm.webp")


st.markdown("### Giới thiệu dự án")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Phân tích RFM là phương pháp phân khúc khách hàng dựa trên 3 yếu tố:**
    - **Recency (R)**: Thời gian kể từ lần mua hàng cuối cùng
    - **Frequency (F)**: Số lần mua hàng
    - **Monetary (M)**: Tổng chi tiêu
    """)

with col2:
    st.markdown("""
   ** Ứng dụng này giúp doanh nghiệp:**
    - Hiểu rõ hành vi khách hàng
    - Xác định nhóm khách hàng giá trị
    - Đề xuất chiến lược marketing phù hợp
    """)

with st.expander("📊 Tìm hiểu về phương pháp RFM"):
    st.markdown("#### Các thành phần RFM")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        ##### **Recency (R)**
        - Đo lường độ "mới" của khách hàng
        - Khách hàng mới mua gần đây có xu hướng phản hồi tốt hơn với các chương trình khuyến mãi
        """)

    with col2:
        st.markdown("""
        ##### **Frequency (F)**
        - Đo lường mức độ thường xuyên mua hàng
        - Khách hàng mua thường xuyên thường trung thành hơn
        """)

    with col3:
        st.markdown("""
        ##### **Monetary (M)**
        - Đo lường giá trị tài chính
        - Giúp xác định khách hàng mang lại nhiều lợi nhuận nhất
        """)

    st.markdown("""
    #### Cách tính điểm RFM:
    - Chia mỗi chỉ số thành 4 nhóm (1-4)
    - Điểm 4 là tốt nhất, 1 là kém nhất
    - Tổng hợp thành RFM Score (vd: 444, 341,...)
    """)

st.markdown("""
### Thông tin dữ liệu
Dữ liệu giao dịch từ một cửa hàng bán lẻ ở Mỹ giai từ 01/2014 đến 12/2015.
**Thuật toán:** `Manual Segmentaion`, `K-Means`, `GMM`, `KMeans PySpark`
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown("Products_with_Categories.csv")
    products = pd.read_csv('Data/Products_with_Categories.csv')
    st.dataframe(products, use_container_width=True)
with col2:
    st.markdown("Transactions.csv")
    transactions = pd.read_csv('Data/Transactions.csv')
    st.dataframe(transactions, use_container_width=True)

# Load the data
df_RFM = pd.read_csv('Data/df_RFM.csv')
st.dataframe(df_RFM, use_container_width=True)

# Tabs
tabs = st.tabs(["📊 Bussiness Overview", "👥 Customer Analysis"])
with tabs[0]:
    st.markdown("### 📊 Bussiness Overview")
    st.image('img/BO.png', use_container_width=True)

    st.markdown("### Top 5 Categories with Revenue")
    col1, col2 = st.columns(2)
    with col1:
        st.image('img/highrevenue.png', use_container_width=True, caption="High Revenue Categories")
    with col2:
        st.image('img/lowrevenue.png', use_container_width=True, caption="Low Revenue Categories")

    st.markdown("### Top 5 Categories with Number of Orders")
    col1, col2 = st.columns(2)
    with col1:
        st.image('img/highorder.png', use_container_width=True)
    with col2:
        st.image('img/loworder.png', use_container_width=True)
    
with tabs[1]:
    st.markdown("### 👥 Customer Analysis")
    st.image('img/customer.png', use_container_width=True)
    st.image('img/customer2.png', use_container_width=True)