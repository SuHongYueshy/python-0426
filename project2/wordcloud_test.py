# 导入了画图的库，词云生成库和jieba的分词库
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
font_path=r'C:\Windows\Fonts\simsun.ttc'
# 使用jieba进行分词，并对分词的结果以空格隔开
text_from_file_apath = open('wordcloud.txt',encoding='UTF-8').read()
wordlist_after_jieba = jieba.cut(text_from_file_apath,cut_all = True)
wl_space_split = "".join(wordlist_after_jieba)
# 对分词后的文本生成词云
my_wordcloud = WordCloud().generate(wl_space_split)
# pyplot展示词云图
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()