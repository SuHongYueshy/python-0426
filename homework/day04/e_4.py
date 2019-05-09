#  找出一片英文文章的最高频单词

import re
from collections import Counter

with open("captain.txt", "r", encoding="utf-8") as fd:
    texts = fd.read()
    count = Counter(re.split(r"\W+", texts))

result = count.most_common(1)
print(result)

