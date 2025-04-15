import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

rfm_agg2 = pd.read_csv('Data/rfm_agg2.csv')
df_gmm = pd.read_csv('Data/GMM.csv')
df_pyspark = pd.read_csv('Data/PySpark.csv')

st.title("Kết quả mô hình phân cụm")
st.subheader("🌟 Kết quả tối ưu nhất: K-Means Scikit")

# Elbow Section
st.markdown("### Elbow Method")
col1, col2 = st.columns(2)
with col1:
    st.image('img/Elbow.png', use_container_width=True)
with col2:
    st.markdown("**Số cụm tối ưu:** 5")

# Các cụm
st.markdown("### 🧑‍🤝‍🧑 Các nhóm khách hàng")
st.dataframe(rfm_agg2[['Cluster','Count','Percent']], use_container_width=True)

# K-Means Section
st.markdown("### 📊 K-Means Scikit")
col1, col2 = st.columns(2)
with col1:
    st.image('img/KMeans3D.png', use_container_width=True)
with col2:
    st.image('img/KMeans.png', use_container_width=True)

tabs = st.tabs(["🛑 Churned", "🌟 Potential", "💎 Engaged", "⚠️ At risk", "👑 VIP"])
with tabs[0]:
    st.write("**Đặc điểm:**")
    st.write("""
    - Khách hàng đã rời bỏ, ít tương tác.
    - Tần suất mua hàng thấp, chi tiêu ít.
    - Cần chiến lược tái thu hút mạnh mẽ.
    """)

    st.write("**Chiến lược:**")
    st.write("""
    - Giảm giá mạnh để thu hút lại.
    - Cắt giảm chi phí marketing cho nhóm này.
    - Tập trung vào nhóm khách hàng tiềm năng hơn.
    """)

with tabs[1]:
    st.write("**Đặc điểm:**")
    st.write("""
    - Khách hàng tiềm năng, có khả năng mua hàng cao.
    - Tần suất mua hàng trung bình, chi tiêu vừa phải.
    - Cần chiến lược khuyến mãi hấp dẫn.
    """)

    st.write("**Chiến lược:**")
    st.write("""
    - Tăng cường quảng cáo và khuyến mãi cho nhóm này.
    - Cung cấp các ưu đãi đặc biệt để giữ chân họ.
    """)

with tabs[2]:
    st.write("**Đặc điểm:**")
    st.write("""
    - Khách hàng thường xuyên, có tần suất mua hàng cao.
    - Chi tiêu trung bình, có khả năng trung thành cao.
    - Cần duy trì mối quan hệ tốt với họ.
    """)

    st.write("**Chiến lược:**")
    st.write("""
    - Cung cấp chương trình khách hàng thân thiết.
    - Tạo ra các ưu đãi độc quyền cho nhóm này.
    """)

with tabs[3]:
    st.write("**Đặc điểm:**")
    st.write("""
    - Khách hàng có nguy cơ rời bỏ, ít tương tác.
    - Tần suất mua hàng giảm, chi tiêu thấp.
    - Cần chiến lược tái thu hút mạnh mẽ.
    """)

    st.write("**Chiến lược:**")
    st.write("""
    - Gửi email nhắc nhở và ưu đãi đặc biệt.
    - Tạo ra các chương trình khuyến mãi hấp dẫn.
    """)

with tabs[4]:
    st.write("**Đặc điểm:**")
    st.write("""
    - Khách hàng cao cấp, có tần suất mua hàng cao.
    - Chi tiêu lớn, có khả năng trung thành cao.
    - Cần duy trì mối quan hệ tốt với họ.
    """)

    st.write("**Chiến lược:**")
    st.write("""
    - Cung cấp chương trình khách hàng thân thiết.
    - Tạo ra các ưu đãi độc quyền cho nhóm này.
    """)
    
st.divider()

st.subheader("📊 Các thuật toán còn lại")
tabs = st.tabs(["Manual Segmentation", "GMM", "KMeans PySpark"])

with tabs[0]:
    st.image('img/RFM.png', use_container_width=True)
    st.markdown("**Số cụm:** 6")

with tabs[1]:
    col1, col2 = st.columns(2)
    with col1:
        st.image('img/AICBIC.png', use_container_width=True)
    with col2:
        st.markdown("**Số cụm tối ưu:** 5")

    col1, col2 = st.columns(2)
    with col1:
        st.image('img/GMM.png', use_container_width=True)
    with col2:
        st.image('img/GMM3D.png', use_container_width=True)
    
    st.dataframe(df_gmm[['Group','Count','Percent']], use_container_width=True)

with tabs[2]:
    col1, col2 = st.columns(2)
    with col1:
        st.image('img/sil.png', use_container_width=True)
    with col2:
        st.markdown("**Số cụm tối ưu:** 4")

    col1, col2 = st.columns(2)
    with col1:
        st.image('img/pyspark.png', use_container_width=True)
    with col2:
        st.image('img/pyspark2.png', use_container_width=True)
    
    st.dataframe(df_pyspark[['prediction','Count','Percentage']], use_container_width=True)
