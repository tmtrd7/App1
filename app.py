import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Portfolio cá nhân", page_icon="👤", layout="wide")

# Custom CSS để làm app trông chuyên nghiệp hơn
st.markdown("""
    <style>
    /* Font và màu sắc chủ đạo */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Glassmorphism hiệu ứng cho sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
    }

    /* Tiêu đề chính */
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    /* Các thẻ kỹ năng */
    .skill-tag {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        background: #f0f2f6;
        color: #31333F;
        margin: 5px;
        font-weight: 500;
        border: 1px solid #ddd;
    }

    /* Hiệu ứng hover cho các mục */
    .section-card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e6e9ef;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .section-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=150, caption="Coder / Developer")
    st.title("Họ và Tên Của Bạn")
    st.write("📍 Thành phố Hà Nội, Việt Nam")
    st.write("📧 tmtrd7@gmail.com")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("💻 [GitHub](https://github.com)")
    
    st.divider()
    st.write("👋 Chào mừng bạn đến với trang cá nhân của tôi!")

# --- MAIN CONTENT ---
st.markdown('<p class="main-title">Xin chào, tôi là [NGUYỄN HOÀNG TÙNG]</p>', unsafe_allow_html=True)
st.subheader("Logisticts Expert| Data Enthusiast | Tech Blogger")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Giới thiệu bản thân")
    st.write("""
    Tôi là một lập trình viên đam mê công nghệ với niềm yêu thích đặc biệt trong việc xây dựng các ứng dụng web thông minh và xử lý dữ liệu. 
    Với kinh nghiệm làm việc với các dự án Python, tôi luôn tìm kiếm những giải pháp tối ưu cho người dùng.
    """)

    st.markdown("### 💼 Kinh nghiệm làm việc")
    st.markdown("""
    <div class="section-card">
        <strong>Công ty ABC - Software Developer Intern</strong><br>
        <em>Tháng 1/2023 - Hiện tại</em>
        <ul>
            <li>Phát triển và bảo trì các module backend bằng Python.</li>
            <li>Tối ưu hóa truy vấn cơ sở dữ liệu giúp tăng 20% tốc độ tải trang.</li>
        </ul>
    </div>
    <div class="section-card">
        <strong>Dự án Freelance - Web Dev</strong><br>
        <em>2022</em>
        <ul>
            <li>Xây dựng landing page cho các doanh nghiệp nhỏ.</li>
            <li>Triển khai CMS đơn giản cho quản trị viên.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🛠️ Kỹ năng")
    skills = ["Python", "Streamlit", "JavaScript", "SQL", "Git", "Docker", "Machine Learning"]
    skill_html = "".join([f'<span class="skill-tag">{s}</span>' for s in skills])
    st.markdown(skill_html, unsafe_allow_html=True)

    st.markdown("### 🎓 Học vấn")
    st.write("""
    **Đại học Công nghệ thông tin**  
    *Cử nhân Khoa học Máy tính*  
    (2020 - 2024)
    """)

st.divider()

# --- CONTACT FORM ---
st.markdown("### 📩 Liên hệ với tôi")
with st.form("contact_form"):
    name = st.text_input("Tên của bạn")
    email = st.text_input("Email")
    message = st.text_area("Lời nhắn")
    submit = st.form_submit_button("Gửi tin nhắn")
    
    if submit:
        st.success(f"Cảm ơn {name}! Tin nhắn của bạn đã được gửi.")

# Footer
st.markdown("<br><hr><center>Author: Nguyễn Hoàng Tùng</center>", unsafe_allow_html=True)
