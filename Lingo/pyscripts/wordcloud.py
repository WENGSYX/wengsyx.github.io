import pyecharts.options as opts
from pyecharts.charts import WordCloud
import json
from collections import Counter

stop_words = {'the', '(the', 'that', 'to', 'is', 'a', 'of', '?', '0000', '0001', 'was', 'were', ',', 'did'}
cnt = Counter()
texts = json.load(open('/Users/sjx/Desktop/lab/MYWORK/KQA Pro/corpus/v1.0/rewrite118k.json'))
for text in texts:
    text = text['rewrite']
    cnt.update(filter(lambda x: x not in stop_words, text.lower().strip().replace('(', ' ').replace(')', ' ').replace('?', ' ').replace(',', ' ').split()))

data = cnt.most_common(200)


(
    WordCloud()
    .add(series_name="", data_pair=data, word_size_range=[15, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Question Word Cloud", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("tmp.html")
)
