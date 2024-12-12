#기본적인 Streamlit 페이지 예제

# streamlit_app.py
import streamlit as st
import pandas as pd

# 1. 제목
st.title("김영준의 교육")

# 2. 부제목
st.subheader("이런 학생이?!")

# 3. 판다스 데이터프레임 기반 표 출력
df = pd.DataFrame({
    "이름": ["손하람", "Bob", "Charlie"],
    "나이": [18, 30, 29],
    "나라": ["Korea", "USA", "UK"]
})
st.write("데이터프레임 예제")
st.dataframe(df)

# 4. HTML 활용 예제
st.write("HTML 예제")
st.markdown(
    """
    <div style="color: blue; font-size: 20px;">
        HTML을 활용한 예시 텍스트입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 5. HTML과 CSS 활용 예제
st.write("HTML과 CSS 예제")
st.markdown(
    """
    <style>
    .styled-box {
        padding: 10px;
        margin: 5px;
        background-color: lightgreen;
        border-radius: 5px;
        color: darkgreen;
    }
    </style>
    <div class="styled-box">
        HTML과 CSS를 함께 사용하여 스타일링한 박스입니다.
    </div>
    """,
    unsafe_allow_html=True
)

# 6. 이미지 표시
st.write("이미지 표시 예제")
st.image("https://mblogthumb-phinf.pstatic.net/MjAyMzAzMjRfMjY0/MDAxNjc5NjY0NzA4OTY1.jNaCcAtWCOIOI9DkkO-rh7qJbcK9JnoopNiHlnjKkLIg.-YVOnacHmfpc3cMObzDH9Layy1bVbiJVEWLQNN_5Z-Yg.JPEG.sangho0322/IMG_3779.JPG?type=w800", caption="Streamlit 로고")

# 7. 유튜브 링크 (썸네일 표시)
st.write("유튜브 동영상 예제")
st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")

