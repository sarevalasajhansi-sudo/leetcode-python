class Solution(object):

    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """

        n = len(s)

        # Each node:
        # [left_char, right_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def build(node, l, r):
            if l == r:
                tree[node] = [s[l], s[l], 1, 1, 1, 1]
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def merge(left, right):
            lc, rc, lp, ls, lb, ll = left
            rlc, rrc, rp, rs, rb, rl = right

            length = ll + rl
            prefix = lp
            suffix = rs
            best = max(lb, rb)

            if rc == rlc:
                # The suffix of left + prefix of right can merge
                best = max(best, ls + rp)

                # Entire prefix becomes one repeating character
                if lp == ll:
                    prefix = ll + rp

                # Entire suffix becomes one repeating character
                if rs == rl:
                    suffix = rs + ls

            return [lc, rrc, prefix, suffix, best, length]

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = [ch, ch, 1, 1, 1, 1]
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryCharacters)):
            idx = queryIndices[i]
            ch = queryCharacters[i]

            update(1, 0, n - 1, idx, ch)

            ans.append(tree[1][4])

        return ans