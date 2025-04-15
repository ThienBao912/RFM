import streamlit as st
import pandas as pd
import pickle

# Load models and data
@st.cache_data
def load_data():
    df_RFM = pd.read_csv('Data/df_RFM.csv')
    df1 = pd.read_csv('Data/Products_with_Categories.csv')
    df2 = pd.read_csv('Data/Transactions.csv')
    df = pd.merge(df2, df1, on='productId', how='inner')
    df['purchase_amount'] = df['price'] * df['items']
    return df_RFM, df

df_RFM, df = load_data()

def load_model_and_scaler():
    with open("pkl/kmeans_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("pkl/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, scaler
model, scaler = load_model_and_scaler()

def cluster_name(cluster_id):
    mapping = {
        0: "🛑 Churned - Khách đã rời bỏ",
        1: "🌟 Potential - Khách tiềm năng",
        2: "💎 Engaged - Khách thường xuyên",
        3: "⚠️ At Risk - Khách có nguy cơ rời bỏ",
        4: "👑 VIP - Khách hàng cao cấp"
    }
    return mapping.get(cluster_id, "Không xác định")

st.title("Trải nghiệm phân cụm")

input_method = st.radio("Chọn cách nhập thông tin khách hàng:", 
                       ["Nhập mã khách hàng", "Nhập thông tin khách hàng vào slider", "Tải file CSV"])

if input_method == "Nhập mã khách hàng":
    selected_customers = st.multiselect("Chọn một hoặc nhiều mã khách hàng:", 
                                      sorted(df_RFM['Member_number'].unique()))
    if selected_customers:
        result_segments = df_RFM[df_RFM["Member_number"].isin(selected_customers)]
        result_trans = df[df["Member_number"].isin(selected_customers)]
        
        st.success(f"✅ Tìm thấy {len(result_segments)} khách hàng:")
        st.dataframe(result_segments)

        try:
            rfm_values = result_segments[['Recency', 'Frequency', 'Monetary']].values[0]
            cluster_label = model.predict(scaler.transform([rfm_values]))[0]
            st.success(f"✅ Cụm khách hàng: **{cluster_name(cluster_label)}**")
        except Exception as e:
            st.error(f"Lỗi khi phân cụm: {str(e)}")
            
        st.success(f"✅ Lịch sử giao dịch:")
        st.dataframe(result_trans)

elif input_method == "Nhập thông tin khách hàng vào slider":
    st.subheader("Dự đoán phân cụm từ các giá trị R, F, M")
    cols = st.columns(3)
    with cols[0]:
        recency = st.slider("Recency (Ngày)", 0, 727, 30)
    with cols[1]:
        frequency = st.slider("Số lần mua hàng", 1, 36, 5)
    with cols[2]:
        monetary = st.slider("Tổng chi tiêu", 10, 375, 200)
    
    if st.button("Dự đoán phân cụm"):
        cluster_label = model.predict(scaler.transform([[recency, frequency, monetary]]))[0]
        st.write(f"Thông tin nhập vào: Recency: `{recency}`, Frequency: `{frequency}`, Monetary: `{monetary}`")
        st.success(f"✅ Kết quả phân cụm: **{cluster_name(cluster_label)}**")

else:  # CSV Upload
    st.subheader("Tải lên file CSV để phân cụm")
    st.markdown("""
    **Yêu cầu định dạng file:**
    - File CSV có ít nhất 3 cột: `Recency`, `Frequency`, `Monetary`
    - Cột `CustomerID` là tùy chọn (nếu có sẽ hiển thị trong kết quả)
    """)
    
    uploaded_file = st.file_uploader("Chọn file CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df_uploaded = pd.read_csv(uploaded_file)
            required_cols = {"Recency", "Frequency", "Monetary"}
            
            # Check if required columns exist
            if not required_cols.issubset(df_uploaded.columns):
                missing = required_cols - set(df_uploaded.columns)
                st.error(f"Thiếu các cột bắt buộc: {', '.join(missing)}")
            else:
                # Process the file
                df_input = df_uploaded[list(required_cols)]
                scaled_input = scaler.transform(df_input)
                clusters = model.predict(scaled_input)
                
                # Prepare results
                df_result = df_uploaded.copy()
                df_result["Cluster"] = clusters
                df_result["Phân nhóm"] = df_result["Cluster"].apply(cluster_name)
                
                st.success("✅ Phân cụm thành công!")
                
                # Show results in expandable sections
                with st.expander("Xem toàn bộ kết quả"):
                    st.dataframe(df_result)
                
                with st.expander("Xem chi tiết từng phân nhóm"):
                    for cluster_id in sorted(df_result["Cluster"].unique()):
                        st.subheader(f"Phân nhóm {cluster_id}: {cluster_name(cluster_id)}")
                        st.dataframe(df_result[df_result["Cluster"] == cluster_id])
                
                # Download button
                csv = df_result.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Tải xuống kết quả",
                    data=csv,
                    file_name='RFM_clusters_result.csv',
                    mime='text/csv'
                )
                
        except Exception as e:
            st.error(f"⚠️ Lỗi khi xử lý file: {str(e)}")