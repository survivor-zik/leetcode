numer = [100,4,200,1,3,2]

def lcs(nums: list):
    if len(nums) == 0:
        return 0
    num_set = set(nums)
    lcs_ = 1
    for nu in num_set:
        if nu - 1 in num_set:
            continue
        else:
            currentnum = nu
            currentsub = 1
            while currentnum + 1 in num_set:
                currentsub += 1
                currentnum += 1
            lcs_ = max(lcs_, currentsub)

    return lcs_

print(lcs(numer))