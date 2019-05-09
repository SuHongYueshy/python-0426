#  查询一篇英文文章的最长单词

f=open('captain.txt','r')
longest=''
for word in f:
    if len(word)>len(longest):
            longest = word
print(longest)
