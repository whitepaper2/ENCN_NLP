# jieba分词&&FP
import sys
import jieba
import xlrd

sys.path.append('D:/code/python/kaggle/chineseNlp')
from fpGrowth import *

input_file = "./data/4月28日自动问答明细 (1).xlsx"
column_id = 3
xls_data = xlrd.open_workbook(input_file)
input_data = xls_data.sheets()[0]
nrows = input_data.nrows  # 行数
ncols = input_data.ncols  # 列数
all_split_words = []
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '，', ' ', '？',
                        '/', '！', '（', '）', '“', '”', '：', '-']
stop_words = [line.rstrip() for line in open('./data/stopwords.txt')]
output_file = open('./data/segwords.txt', 'a')
for row_i in range(1, nrows):
    row = input_data.row_values(row_i)
    if row:
        app = [i for i in jieba.cut(row[column_id], cut_all=False) if i not in stop_words and i not in english_punctuations]
        if len(app) >= 1:
            all_split_words.append(app)
            output_file.write(str(app) + "\n")
            # print(list4)
output_file.close()

initSet = createInitSet(all_split_words)
# print(initSet)
myFPtree, myHeaderTab = createTree(initSet, 300)
# # 创建条件模式基
freqItemList = []
mineTree(myFPtree, myHeaderTab, 3, set([]), freqItemList)
print("freq:", freqItemList)

# print(myHeaderTab)
