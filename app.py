import random
import requests

# Wikipediaの記事タイトルからランダムで取得（日本語版）
def get_wikipedia_titles(n=3):
    url = "https://ja.wikipedia.org/w/api.php"
    params = {
        'format': 'json',
        'action': 'query',
        'list': 'random',
        'rnnamespace': 0,
        'rnlimit': n
    }
    response = requests.get(url, params=params).json()
    titles = [item['title'] for item in response['query']['random']]
    return titles

# 三題噺のお題生成
def generate_japanese_prompts():
    titles = get_wikipedia_titles()
    print("🖋 三題噺のお題（Wikipediaから）🖋")
    for idx, title in enumerate(titles, 1):
        print(f"{idx}. {title}")

# 実行
generate_japanese_prompts()
