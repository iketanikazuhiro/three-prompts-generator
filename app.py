import streamlit as st
import requests

def get_wikipedia_titles(n=3):
    url = "https://ja.wikipedia.org/w/api.php"
    params = {
        'format': 'json',
        'action': 'query',
        'list': 'random',
        'rnnamespace': 0,
        'rnlimit': n
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # HTTPエラーをチェック
        data = response.json()
        return [item['title'] for item in data['query']['random']]
    except Exception as e:
        return [f"エラーが発生しました: {e}"]

# Streamlitの表示設定
st.set_page_config(page_title="三題噺お題ジェネレーター", page_icon="📚")
st.title("📚 三題噺のお題ジェネレーター")

st.write("このアプリでは、Wikipediaからランダムに抽出した3つの単語やフレーズをお題として表示します。")

# ボタンを押してお題を生成
if st.button("お題を生成する"):
    titles = get_wikipedia_titles()
    st.write("### 🎲 ランダム三題噺のお題")
    for idx, title in enumerate(titles, 1):
        st.write(f"**お題 {idx}:** {title}")
else:
    st.write("ボタンを押してお題を生成してください。")
