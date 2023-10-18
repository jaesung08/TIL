def dfs(month, acc_cost):
    global ans

    # 기저조건
    if month > 12:
        ans = min(ans, acc_cost)
        return

    if acc_cost > ans:
        return

    # 1일 이용권으로 모두 구입
    dfs(month + 1, acc_cost + (months[month] * cost_day))

