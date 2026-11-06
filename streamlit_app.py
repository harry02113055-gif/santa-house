import os
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Santa's Dream House Quiz", page_icon="🎅", layout="centered")

# CSS 스타일링
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .stImage > img {
        border-radius: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎅 산타의 드림하우스 포토 퀴즈!")
st.subheader("Lesson 6. What's in the Kitchen?")
st.write("방 사진을 보고 수수께끼를 풀어 올바른 영어 문장을 완성해 주세요!")

# 세션 상태 초기화 (클리어한 방 추적)
if "cleared_rooms" not in st.session_state:
    st.session_state.cleared_rooms = []

# 4가지 장소와 퀴즈 데이터 정의 (경로 자동 탐색 목록 포함)
rooms_quiz = {
    "🍳 Kitchen": {
        "filenames": ["kitchen.png", "streamlit_app/kitchen.png"],
        "visual": "🍳 🍳 🪑 🪑",
        "question": "What's in the kitchen? 요리를 할 수 있는 뜨거운 이것은 무엇일까요?",
        "options": ["There is a stove.", "There is a bed.", "There is a sofa."],
        "answer": "There is a stove.",
    },
    "🛏️ Bedroom": {
        "filenames": ["bedroom.png", "streamlit_app/bedroom.png"],
        "visual": "🛏️ 💡 💡 🛏️",
        "question": "What's in the bedroom? 잠을 자는 아늑한 공간에 있는 이것은?",
        "options": ["There are two TVs.", "There is a bed.", "There are five flowers."],
        "answer": "There is a bed.",
    },
    "📺 Living Room": {
        "filenames": ["living_room.png", "streamlit_app/living_room.png", "living.png"],
        "visual": "📺 📺 🛋️ 🛋️",
        "question": "What's in the living room? 거실에 두 대가 있는 이것은?",
        "options": ["There is a stove.", "There are two TVs.", "There is a bed."],
        "answer": "There are two TVs.",
    },
    "🌳 Garden": {
        "filenames": ["garden.png", "streamlit_app/garden.png"],
        "visual": "🌸 🌺 🌻 🌳",
        "question": "What's in the garden? 정원에 알록달록 피어있는 이것은?",
        "options": ["There are five flowers.", "There is a sofa.", "There are two TVs."],
        "answer": "There are five flowers.",
    }
}

# 상단 진행 상황 (미션 현황)
st.markdown("### 🎒 나의 미션 현황 (Mission Status)")
progress_cols = st.columns(4)
all_room_keys = list(rooms_quiz.keys())

for idx, room_name in enumerate(all_room_keys):
    with progress_cols[idx]:
        if room_name in st.session_state.cleared_rooms:
            st.success(f"✅ {room_name.split()[1]}")
        else:
            st.warning(f"🔒 {room_name.split()[1]}")

st.markdown("---")

# 방 선택 메뉴
st.markdown("### 🚪 도전할 방을 선택하세요!")
selected_room = st.selectbox("탐색할 장소를 고르세요:", ["선택하세요!"] + all_room_keys)

if selected_room != "선택하세요!":
    quiz = rooms_quiz[selected_room]
    st.markdown(f"## 📍 {selected_room} 퀴즈 미션")
    
    # 💡 핵심: 현재 폴더나 하위 폴더(streamlit_app/) 중 파일이 있는 곳을 알아서 찾아냄!
    image_path = None
    for fname in quiz["filenames"]:
        if os.path.exists(fname):
            image_path = fname
            break
            
    if image_path:
        st.image(image_path, use_column_width=True)
    else:
        # 혹시라도 파일이 없으면 예쁜 이모지 카드가 대신 나와서 절대 에러가 안 남!
        st.info(f"✨ [{selected_room}] 미션 일러스트 카드")
        st.markdown(f"<h2 style='text-align: center;'>{quiz['visual']}</h2>", unsafe_allow_html=True)
    
    # 이미 클리어한 방인지 확인
    if selected_room in st.session_state.cleared_rooms:
        st.success(f"🎉 이미 정답을 맞춘 방입니다! 정답: **{quiz['answer']}**")
    else:
        # 퀴즈 문제 출제
        st.info(f"💡 **문제**: {quiz['question']}")
        
        # 보기 선택
        selected_option = st.radio("알맞은 영어 문장을 고르세요:", quiz["options"], key=f"radio_{selected_room}")
        
        if st.button("정답 제출하기 🚀", key=f"btn_{selected_room}"):
            if selected_option == quiz["answer"]:
                st.success("정답입니다! 짝짝짝 🎉")
                st.balloons()
                st.session_state.cleared_rooms.append(selected_room)
                st.rerun()
            else:
                st.error("아쉽네요! 다시 한번 생각해 볼까요? 🤔")

# 모든 미션 완료 체크
st.markdown("---")
if len(st.session_state.cleared_rooms) == len(rooms_quiz):
    st.balloons()
    st.success("🏆 MISSION COMPLETE! 모든 퀴즈를 맞추고 산타의 집을 완성했습니다!")
    st.balloons()
    if st.button("🔄 게임 다시하기"):
        st.session_state.cleared_rooms = []
        st.rerun()
