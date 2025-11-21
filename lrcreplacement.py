# longest repeating character replacement

def charrep(s: str, k: int) -> int:
    count = [0] * 26
    left, answer, maxCount = 0, 0, 0

    for right in range(len(s)):
        count[ord(s[right]) - ord('A')]+=1
        maxCount = max(maxCount,count[ord(s[right]) - ord('A')] )
        if right - left + 1 - maxCount > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1

        answer = max(answer, right - left + 1)
    return answer


print(charrep('ABAB', 2))
