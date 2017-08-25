# coding: utf-8

from nltk.tokenize.stanford_segmenter import StanfordSegmenter

segmenter = StanfordSegmenter(path_to_jar="./stanford-segmenter/stanford-segmenter-3.4.1.jar",
                              path_to_sihan_corpora_dict="./stanford-segmenter/data",
                              path_to_model="./stanford-segmenter/data/pku.gz",
                              path_to_dict="./stanford-segmenter/data/dict-chris6.ser.gz",
                              path_to_slf4j="./stanford-segmenter/slf4j-api.jar")
sent = u'这是斯坦福中文分词器测试'
# print(segmenter.segment(sent))
filename = "./data/5月4日自动问答明细.xlsx"
# cols = ["用户ID","用户问题"]
# df = pd.read_excel(filename)
# df_selected = df[cols]
# print(df[cols].head(2))

# df_segment = segmenter.segment(df_selected["用户问题"].head(1))
# print(df_segment)
import xlrd

xls_data = xlrd.open_workbook(filename)
table = xls_data.sheets()[0]
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
list2 = []
for rownum in range(1, 100):
    row = table.row_values(rownum)
    if row:
        list2.append(segmenter.segment(row[2]).split(" "))
print(list2)

# In[5]:



# In[1]:

import nltk

text = nltk.word_tokenize("And now for something compeletely differently")
print(nltk.pos_tag(text))


# In[ ]:
