
# coding: utf-8

# In[83]:

get_ipython().system(u'ls /tensorflow')


# In[3]:

get_ipython().system(u'pip install jieba')


# In[120]:

import jieba
import re
from collections import Counter


# In[121]:

my_file = open("./happiness.txt").read().decode("utf-8")


# In[122]:

# 正则表达式，匹配并找出文章中所有中文
re_str = u"([\u4e00-\u9fff]+)"
re_pattern = re.compile(re_str)
re_list = re_pattern.findall(my_file)


# In[123]:

# 使用jieba分词对匹配到的每一个中文内容进行分词，最终存到result_words列表中
result_words = []
for words in re_list:
    one_word = jieba.lcut(words)
    result_words.extend(one_word)

# 进行词频统计
counter = Counter(result_words).most_common(10)

print (str(counter).decode("unicode-escape"))


# In[ ]:




# In[ ]:
