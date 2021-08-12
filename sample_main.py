# -*- coding: utf-8 -*-

from ggltrendwordcloud import *

def main():
    FONTPATH = '/usr/share/fonts/truetype/biz/BIZ-UDGothicR.ttc'

    # 画像作成
    wordcloud =  GglTrendWordCloud(
                    font_path=FONTPATH,
                    background_color="white",
                    prefer_horizontal=1,
                    random_state=42
                )
    wordcloud.generate_from_trend_word()
    
    # 画像保存
    wordcloud.to_file("result.png")

if __name__ == '__main__':
    main()
