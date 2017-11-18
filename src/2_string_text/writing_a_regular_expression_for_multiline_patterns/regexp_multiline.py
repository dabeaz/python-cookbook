# example.py
#
# Regular expression that matches multiline patterns

import re

text = '''/* this is a
              multiline comment */
'''

# 匹配/**/之间的字符串
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text))
