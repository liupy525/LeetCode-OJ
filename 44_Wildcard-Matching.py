#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p, flag=True):
        print 's: ',s, 'p: ',p
        print len(s)
        if len(p)-p.count('*')>len(s):
            return False
        if not s and not p:
            return True
        if not p:
            return False
        if len(s)==0:
            if len(p)-p.count('*')==0:
                return True
            else:
                return False
        if flag:
            pp = []
            for i in p:
                pp.append(i) if not pp or not (pp[-1]=='*' and i=='*') else None
            p = ''.join(pp[:])

        if p[0]=='?':
            return self.isMatch(s[1:], p[1:], False)
        elif p[0]=='*':
            if len(p)==1:
                return True
            else:
                te = p[1:].find('*')
                t = s.find(p[1:te])
                while t>=0:
                    if self.isMatch(s[t:], p[1:], False):
                        return True
                    else:
                        temp = s[t+te:].find(p[1:te])
                        t = -1 if temp==-1 else temp+t+1
                return False


#                t = s.find(p[1])
#                while t>=0:
#                    if self.isMatch(s[t:], p[1:], False):
#                        return True
#                    else:
#                        temp = s[t+1:].find(p[1])
#                        t = -1 if temp==-1 else temp+t+1
#                return False
        else:
            te = p.find('*')
            print 'te:  ', te, s[:te], p[:te]
            if te==-1:
                return True if p==s else False
            if p[:te]==s[:te]:
                return self.isMatch(s[te:], p[te:], False)
            else:
                return False


t = Solution()
#print t.isMatch("aa","a")
#print t.isMatch("aa","aa")
#print t.isMatch("aaa","aa")
#print t.isMatch("aa", "*")
#print t.isMatch("aa", "a*")
#print t.isMatch("ab", "?*")
#print t.isMatch("aab", "c*a*b")
#print t.isMatch('aaa', 'a*a')
#print t.isMatch('abbbcd', 'ab*bbbcd')
#print t.isMatch('afafaaafffafaffaffafafffafaffaaffafaaffaaafafafaaaaaffffaffaafafaaafafaaafffafaffaffafafffafaffaaffafaaffaaafafafaafafaaafafaaafffafaffaffafafffafaffaaffafaaffaaafafafafafaaafafaaafffafaffaffafafffafaffaaffafaaffaaafafafaaaaafafafaaafffafaffaffafafffafaffaaffafaaffaaafafafaaaaaffffaffafafa', 'a*a***a*f*a*a*f*a*a*f*a*a*f*a*a*f*a*a*f*a*a*f*aa*f*a')
#print t.isMatch("babbabbabaaaaabaabaaaaabbabaabbbaaaabbaabbbbbaabbabaabbbbaabbbabaabbaaabbbbabbbabbababaababbaaaaaabaabababbbaaabbaaaaaabbbabbbbabaabaaaabbabbaabaababbaaaababaaaaababbbaabaababbbaaabaababbabbabaaabbbbaa", "*a*ab*b*ab*a*bb**bb**a**abb*bb*ab*a*bbbb***ba***aa**ba*b*ab*ba***aaabbbaa*ba*ba*b****baabb**b*aa*aaab*a")
print t.isMatch("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb", "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb")


