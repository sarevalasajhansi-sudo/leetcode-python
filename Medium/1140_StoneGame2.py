class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            # If we can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                stones_taken = suffix[i] - suffix[i + X]

                # Opponent starts at i + X
                opponent = dp(i + X, max(M, X))

                # Current player's total
                current = stones_taken + (
                    suffix[i + X] - opponent
                )

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)