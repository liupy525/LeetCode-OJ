#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''

class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        if len(words)==1:
            return [ words[0] + ''.join([ ' ' for i in range(maxWidth-len(words[0])) ])]
        result = []
        length = len(words[0])
        result.append([words[0]])
        for i in range(1, len(words)):
            if length+1+len(words[i])<=maxWidth:
                length += 1 + len(words[i])    # add one space
                result[-1].append(words[i])
            else:
                result.append([words[i]])
                length = len(words[i])
        for i in range(len(result)):
            if i<len(result)-1:
                num = len(result[i])
                space_num = maxWidth - sum([ len(j) for j in result[i] ])
                avg_space_num = space_num / (num-1) if num>1 else space_num
                remain_space_num = space_num % (num-1) if num>1 else 0
                tmp = ''
                for j in result[i]:
                    tmp += j
                    tmp += ''.join([ ' ' for k in range(avg_space_num) ])
                    if remain_space_num:
                        tmp += ' '
                        remain_space_num -= 1
                tmp = tmp[:maxWidth]
                result[i] = tmp
            else:
                tmp = ''
                for j in result[i]:
                    tmp += j+' '
                tmp = tmp[:-1]
                tmp += ''.join([ ' ' for k in range(maxWidth - len(tmp) )])
                result[i] = tmp
        return result




words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ['']
words = ["a","b","c","d","e"]
words = ["What","must","be","shall","be."]
maxWidth = 12
t = Solution()
tmp = t.fullJustify(words, maxWidth)
print len(tmp[0])
for i in tmp:
    print i





