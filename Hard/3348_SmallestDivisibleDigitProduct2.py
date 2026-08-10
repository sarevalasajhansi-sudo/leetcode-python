class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """

        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i in range(4):
            while t % primes[i] == 0:
                need[i] += 1
                t //= primes[i]

        if t != 1:
            return "-1"

        fac = [
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (2, 0, 0, 0),
            (0, 0, 1, 0),
            (1, 1, 0, 0),
            (0, 0, 0, 1),
            (3, 0, 0, 0),
            (0, 2, 0, 0)
        ]

        A, B = need[0], need[1]
        INF = 10 ** 9

        dp = [[INF] * (B + 1) for _ in range(A + 1)]
        dp[0][0] = 0

        for a in range(A + 1):
            for b in range(B + 1):
                for d in range(2, 10):
                    na = min(A, a + fac[d][0])
                    nb = min(B, b + fac[d][1])

                    if dp[na][nb] > dp[a][b] + 1:
                        dp[na][nb] = dp[a][b] + 1

        def sub(req, d):
            return (
                max(0, req[0] - fac[d][0]),
                max(0, req[1] - fac[d][1]),
                max(0, req[2] - fac[d][2]),
                max(0, req[3] - fac[d][3])
            )

        def possible(req, slots):
            return dp[req[0]][req[1]] + req[2] + req[3] <= slots

        n = len(num)

        req = tuple(need)
        valid = True

        for ch in num:
            d = int(ch)
            if d == 0:
                valid = False
                break
            req = sub(req, d)

        if valid and req == (0, 0, 0, 0):
            return num

        pref = [tuple(need)]
        good = [True]

        for ch in num:
            d = int(ch)

            if d == 0:
                pref.append(pref[-1])
                good.append(False)
            else:
                pref.append(sub(pref[-1], d))
                good.append(good[-1])

        for i in range(n - 1, -1, -1):
            if not good[i]:
                continue

            cur = int(num[i])

            for d in range(cur + 1, 10):
                req = sub(pref[i], d)
                left = n - i - 1

                if not possible(req, left):
                    continue

                ans = num[:i] + str(d)

                for j in range(left):
                    remain = left - j - 1

                    for x in range(1, 10):
                        nr = sub(req, x)

                        if possible(nr, remain):
                            ans += str(x)
                            req = nr
                            break

                return ans

        req = tuple(need)
        min_len = dp[A][B] + need[2] + need[3]

        length = max(n + 1, min_len)

        ans = ""

        for pos in range(length):
            left = length - pos - 1

            for d in range(1, 10):
                nr = sub(req, d)

                if possible(nr, left):
                    ans += str(d)
                    req = nr
                    break

        return ans