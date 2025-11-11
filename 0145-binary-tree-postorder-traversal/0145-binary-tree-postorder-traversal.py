# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        # def traversal(curr):
        #     if not curr:
        #         return
        #     traversal(curr.left)
        #     traversal(curr.right)
        #     ans.append(curr.val)
        
        # traversal(root)
        # return ans
        if not root:
            return []
        s1 = [root]
        s2 =[]

        while s1:
            curr = s1.pop()
            s2.append(curr.val)
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)
        return s2[::-1]
        # ans =[]
        # while s2:
        #     ans.append(s2.pop().val)
        # return ans