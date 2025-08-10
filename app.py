import streamlit as st

# メインタイトル
st.title("サンプルアプリ①: 簡単なWebアプリ")
st.write("文字数をカウントするシンプルなアプリです。")

# ユーザー入力
input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")

# 文字数計算
text_count = len(input_message)

# 実行ボタンと結果表示
if st.button("実行"):
    if input_message:
        st.write(f"文字数: **{text_count}**")
        st.success("カウント完了！")
        
        # 追加の統計情報
        st.info(f"""
        📊 詳細情報:
        - 全体文字数: {len(input_message)}
        - 空白を除く: {len(input_message.replace(' ', ''))}
        - 単語数: {len(input_message.split())}
        """)
    else:
        st.warning("テキストを入力してください。")
        # Streamlit test
