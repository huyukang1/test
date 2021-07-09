



# 一、
def test(s1):
    cover = 0
    if len(s1) == 1: return True
    i = 0
    while i <= cover:
        cover = max(i + s1[i], cover)
        if cover >= len(s1) - 1: return True
        i += 1
    return False

s1 = eval(input('请输入列表：'))
print(test(s1))

# 二、
def test2(s2):
    if len(s2) == 1:
        return s2[0]
    elif len(s2) == 2:
        return max(s2)
    dp = [0] * len(s2)
    dp[0] = s2[0]
    dp[1] = max(s2[0], s2[1])
    for i in range(2, len(s2)):
        dp[i] = max(dp[i - 2] + s2[i], dp[i - 1])
    return dp[-1]

s2 = eval(input('请输入列表：'))
print(test2(s2))
