import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Santa's Dream House Game", page_icon="🎅", layout="centered")

# CSS로 디자인 살짝 꾸미기 (카드 느낌)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎅 산타의 드림하우스 꾸미기 대작전!")
st.subheader("Lesson 6. What's in the Kitchen?")
st.write("방마다 숨겨진 물건을 찾고 영어 문장을 완성해서 산타의 집을 멋지게 꾸며주세요!")

# 세션 상태 초기화 (찾은 물건들 저장)
if "found_items" not in st.session_state:
    st.session_state.found_items = []

# 방과 물건 데이터 정의
rooms = {
    "🍳 Kitchen (부엌)": {"item": "stove", "sentence": "There is a stove.", "desc": "요리를 할 수 있는 뜨거운 난로예요!"},
    "🛏️ Bedroom (침실)": {"item": "bed", "sentence": "There is a bed.", "desc": "산타가 잠을 자는 아늑한 침대예요!"},
    "📺 Living Room (거실)": {"item": "TVs", "sentence": "There are two TVs.", "desc": "거실에 있는 두 대의 커다란 TV예요!"},
    "🌳 Garden (정원)": {"item": "flowers", "sentence": "There are five flowers.", "desc": "알록달록 예쁜 꽃들이 피어있어요!"}
}

# 상단 진행 상황 (인벤토리 개념)
st.markdown("### 🎒 나의 탐색 가방 (Inventory)")
progress_cols = st.columns(4)
all_room_keys = list(rooms.keys())

for idx, (room_name, data) in enumerate(rooms.items()):
    with progress_cols[idx]:
        if data["item"] in st.session_state.found_items:
            st.success(f"✅ {data['item'].upper()}")
        else:
            st.info(f"🔒 ???")

st.markdown("---")

# 방 선택 메뉴
st.markdown("### 🚪 탐색할 공간을 고르세요!")
selected_room = st.selectbox("어느 방으로 갈까요?", ["방을 선택하세요!"] + all_room_keys)

if selected_room != "방을 선택하세요!":
    data = rooms[selected_room]
    st.markdown(f"## 📍 {selected_room}")
    st.write(f"💡 **힌트**: {data['desc']}")
    
    # 물건 찾기 버튼
    if data["item"] not in st.session_state.found_items:
        if st.button(f"🔍 방 안을 살펴보기 (Click!)"):
            st.success(f"정답! 짝짝짝 🎉")
            st.balloons()
            st.session_state.found_items.append(data["item"])
            st.rerun()
    else:
        st.info(f"👍 이미 찾은 물건이에요!")
    
    # 발견한 문장 출력
    if data["item"] in st.session_state.found_items:
        st.markdown(f"### 💬 영어 문장 익히기:")
        st.code(data["sentence"], language="text")

# 모든 미션 완료 체크
st.markdown("---")
if len(st.session_state.found_items) == len(rooms):
    st.balloons()
    st.success("🏆 MISSION COMPLETE! 모든 방을 완벽하게 꾸몄습니다! 산타가 아주 기뻐해요!")
    st.balloons()
    if st.button("🔄 게임 다시하기"):
        st.session_state.found_items = []
        st.rerun()

