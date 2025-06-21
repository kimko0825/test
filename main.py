import streamlit as st
import random

# MBTI별 직업 추천 리스트
mbti_jobs = {
    "INTJ": ["전략 컨설턴트 🧠", "데이터 과학자 📊", "연구원 🔬"],
    "INTP": ["이론 물리학자 🧪", "프로그래머 👨‍💻", "UX 디자이너 🎨"],
    "ENTJ": ["CEO 🏢", "변호사 ⚖️", "프로젝트 매니저 📋"],
    "ENTP": ["스타트업 창업가 🚀", "마케팅 전문가 📢", "발명가 💡"],
    "INFJ": ["상담사 🧘", "작가 ✍️", "심리학자 🧠"],
    "INFP": ["시인 📝", "아티스트 🎨", "NGO 활동가 🌍"],
    "ENFJ": ["교사 🍎", "HR 매니저 👥", "사회 운동가 ✊"],
    "ENFP": ["여행 작가 🌏", "콘텐츠 크리에이터 🎥", "홍보 담당자 📣"],
    "ISTJ": ["회계사 🧾", "군인 🎖️", "법무사 📚"],
    "ISFJ": ["간호사 💉", "초등학교 교사 🏫", "사회복지사 ❤️"],
    "ESTJ": ["경찰관 🚓", "경영 관리자 📈", "감독관 🛠️"],
    "ESFJ": ["행사 기획자 🎉", "보육 교사 🧸", "의료 관리자 🏥"],
    "ISTP": ["기계 엔지니어 🔧", "항공 기술자 ✈️", "응급 구조사 🚑"],
    "ISFP": ["플로리스트 💐", "요리사 🍳", "디자이너 👗"],
    "ESTP": ["세일즈 전문가 💼", "스턴트 배우 🎬", "스포츠 트레이너 🏋️"],
    "ESFP": ["배우 🎭", "가수 🎤", "이벤트 호스트 🎈"]
}

# Streamlit 웹 앱 시작
st.set_page_config(page_title="MBTI 직업 추천✨", page_icon="🌟", layout="wide")

st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #FF69B4;
    }
    .subtitle {
        text-align: center;
        font-size: 30px;
        color: #9370DB;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💖 MBTI 직업 추천 사이트 💼</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격에 딱 맞는 직업을 찾아보세요! ✨</div>', unsafe_allow_html=True)

st.write("\n")

# MBTI 선택 박스
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("👉 당신의 MBTI는 무엇인가요?", mbti_list, index=0)

if selected_mbti:
    st.markdown(f"## 🧬 {selected_mbti} 유형에게 어울리는 직업은?")
    recommended_jobs = random.sample(mbti_jobs[selected_mbti], k=len(mbti_jobs[selected_mbti]))
    for job in recommended_jobs:
        st.markdown(f"- 🌟 {job}")

    st.markdown("---")
    st.success("💡 나에게 맞는 직업을 찾았나요? 진로는 언제든지 바뀔 수 있어요! 💖")
    st.balloons()
