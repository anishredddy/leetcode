class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.ans = 0

        # Step 1: compute total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        # Step 2: compute subtree sums and maximize product
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subtree_sum = node.val + left + right

            # try cutting here
            self.ans = max(self.ans, subtree_sum * (total - subtree_sum))

            return subtree_sum

        dfs(root)
        return self.ans % MOD
