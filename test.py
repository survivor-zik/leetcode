def get_spotting_metric(results):
    rk = [k for k in results if k!=0]
    k=3
    if len(rk) < k:
        return 0
    minimum_average = 100000
    for i in range(len(rk)-k+1):
        slid_win = rk[i:i+k]
        print(slid_win)
        avg = sum(slid_win)/k
        minimum_average = min(avg,minimum_average)
    return minimum_average


if __name__ == "__main__":
    print(get_spotting_metric([ 2, 1, 3, 0, 1, 5, 0, 0, 6, 7 ])) # should print ~1.667