# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import feedparser

class GglTrendWordCloud(WordCloud):
    RSS_URL = 'https://trends.google.co.jp/trends/trendingsearches/daily/rss?geo='
    frequencies={}
    geo=''
    def __init__(self, font_path=None, width=400, height=200, margin=2, ranks_only=None, prefer_horizontal=0.9, mask=None, scale=1, color_func=None, max_words=200, min_font_size=4, stopwords=None, random_state=None, background_color='black', max_font_size=None, font_step=1, mode='RGB', relative_scaling='auto', regexp=None, collocations=True, colormap=None, normalize_plurals=True, contour_width=0, contour_color='black', repeat=False, include_numbers=False, min_word_length=0, collocation_threshold=30, geo='JP'):
        super().__init__(
            font_path=font_path,
            width=width,
            height=height,
            margin=margin,
            ranks_only=ranks_only,
            prefer_horizontal=prefer_horizontal,
            mask=mask,
            scale=scale,
            color_func=color_func,
            max_words=max_words,
            min_font_size=min_font_size,
            stopwords=stopwords,
            random_state=random_state,
            background_color=background_color,
            max_font_size=max_font_size,
            font_step=font_step,
            mode=mode,
            relative_scaling=relative_scaling,
            regexp=regexp,
            collocations=collocations,
            colormap=colormap,
            normalize_plurals=normalize_plurals,
            contour_width=contour_width,
            contour_color=contour_color,
            repeat=repeat,
            include_numbers=include_numbers,
            min_word_length=min_word_length,
            collocation_threshold=collocation_threshold
        )
        self.geo=geo
    
    def get_trend_word(self):
        self.url = self.RSS_URL + self.geo

        d = feedparser.parse(self.url)
        self.frequencies.clear
        for entry in d.entries:
            traffic=str(entry.ht_approx_traffic)
            traffic=traffic.replace('+','')
            traffic=traffic.replace(',','')
            traffic=traffic.replace('.','')
            self.frequencies[entry.title]=int(traffic)
        return self.frequencies
    
    def generate_from_trend_word(self, max_font_size=None):
        frequencies=self.get_trend_word()
        return super().generate_from_frequencies(frequencies, max_font_size=max_font_size)
