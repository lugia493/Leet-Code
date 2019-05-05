'''
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

'''

import collections as c

def solution(beginWord, endWord, wordList):
    
    if not endWord or not beginWord or endWord not in wordList or not wordList:
        return 0
    
    L = len(beginWord)

    adj = c.defaultdict(list)
    for word in wordList:
        for i in range(L):
            # Key - generic word
            # Value list of words which have same intermediate gen word
            adj[word[:i] + "*" + word[i+1:]].append(word)
    
    print(adj)
    
    queue = c.deque()
    queue.append((beginWord, 1))
    visited = set(beginWord)

    while queue:
        current_word, level = queue.popleft()
        for i in range(L):
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            for word in adj[intermediate_word]:
                if word == endWord:
                    return level + 1
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level+1))
            adj[intermediate_word] = []
    return 0

beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
print(solution(beginWord, endWord, wordList))