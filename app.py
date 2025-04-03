import streamlit as st
import requests
import urllib.parse

# Wikipediaからランダムな記事タイトルを取得する関数
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
        response.raise_for_status()
        data = response.json()
        return [item['title'] for item in data['query']['random']]
    except Exception as e:
        return [f"エラーが発生しました: {e}"]

st.set_page_config(page_title="三題噺お題ジェネレーター", page_icon="📚")
st.title("📚 三題噺お題ジェネレーター")

st.write("このアプリでは、Wikipediaからランダムに抽出した3つの単語やフレーズをお題として表示します。ボタンを押して生成してください。")

if st.button("お題を生成する"):
    titles = get_wikipedia_titles()
    st.write("### 🎲 3つのお題を使った話を書いてみましょう")
    combined_text = "\n".join([f"お題 {idx}: {title}" for idx, title in enumerate(titles, 1)])
    st.text_area("生成されたお題", combined_text, height=100)

    # Twitterシェアボタン
    app_link = "https://three-prompts-generator-2-r3p2f9zk4oufsh7hcifq38.streamlit.app/"
    tweet_text = f"三題噺のお題を生成しました。\n{combined_text}\nこのアプリでお題を作成できます！\n{app_link}"
    tweet_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(tweet_text)}"
    st.markdown(f'[🐦 Twitterでシェアする]({tweet_url})')
else:
    st.write("ボタンを押してお題を生成してください。")
