
def validpalindrome(s:str)->bool:

    s = [k for k in s if k.isalnum()]
    s = "".join(s)
    s = s.lower()
    end = len(s) - 1
    for i in range(len(s)):
        if s[i]!= s[end]:
            return False
        end-=1

    return True


print(validpalindrome("0P"))