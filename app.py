import streamlit as st  

def main():
    st.title('嵌入 Grafana 面板示例')
    
    # 替换以下 URL 为您 Grafana 面板的 URL
    grafana_url = "http://16.170.252.74:3000/d-solo/adf5982t4su80f/new-dashboard?orgId=1&refresh=10s&from=1709990357727&to=1709992157727&panelId=2"
    
    st.markdown(f'<iframe src="{grafana_url}" width="1000" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
