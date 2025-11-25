
def lenlongsub(s:str)->int:
    left,answer = 0,0
    characters = set()
    i=0
    while i<len(s):
        while s[i] in characters:
            characters.remove(s[left])
            left+=1
        characters.add(s[i])
        answer = max(answer,i-left+1)
        i+=1
    return answer


#another solution

def lengthOfLongestSubstring(s: str) -> int:
    last_seen = {}  # char -> last index
    start = 0
    res = 0
    for end, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        res = max(res, end - start + 1)
        last_seen[char] = end
    return res


print(lenlongsub("pwwkew"))