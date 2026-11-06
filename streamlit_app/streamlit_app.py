import streamlit as st

st.set_page_config(page_title="Santa's Dream House", page_icon="🎅", layout="centered")

st.title("🎅 Santa's Dream House")
st.subheader("Lesson 6. What's in the Kitchen?")
st.write("산타의 드림하우스에 있는 방들을 탐색하며 물건을 찾아보세요!")

if 'current_room' not in st.session_state:
    st.session_state.current_room = 'Kitchen'

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🍳 Kitchen"):
        st.session_state.current_room = 'Kitchen'
with col2:
    if st.button("🛏️ Bedroom"):
        st.session_state.current_room = 'Bedroom'
with col3:
    if st.button("📺 Living Room"):
        st.session_state.current_room = 'Living Room'
with col4:
    if st.button("🪞 Bathroom"):
        st.session_state.current_room = 'Bathroom'

st.divider()

room = st.session_state.current_room
st.header(f"📍 Room: {room}")

if room == 'Kitchen':
    st.write("Q: What's in the kitchen?")
    if st.button("Check Item 1"):
        st.success("A: There is a stove. 🔥")
    if st.button("Check Item 2"):
        st.info("A: There is a table. 🪑")

elif room == 'Bedroom':
    st.write("Q: What's in the bedroom?")
    if st.button("Check Item 1"):
        st.success("A: There is a bed. 🛏️")
    if st.button("Check Item 2"):
        st.info("A: There are two lamps. 💡💡")

elif room == 'Living Room':
    st.write("Q: What's in the living room?")
    if st.button("Check Item 1"):
        st.success("A: There are two TVs. 📺📺")
    if st.button("Check Item 2"):
        st.info("A: There is a sofa. 🛋️")

elif room == 'Bathroom':
    st.write("Q: What's in the bathroom?")
    if st.button("Check Item 1"):
        st.success("A: There is a mirror. 🪞")

st.divider()

if st.button("🎉 Complete Mission!"):
    st.balloons()
    st.subheader("🎊 Congratulations! You found all the items for Santa!")
    st.write("완료 화면을 캡처해서 패들렛(Padlet)에 업로드하세요!")
