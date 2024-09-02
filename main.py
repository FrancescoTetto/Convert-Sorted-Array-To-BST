class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        def buildTree(left, right):
            if left > right:
                return None
            
            #Middle element
            mid = (left + right) // 2

            #TreeNode with middle element
            root = TreeNode(nums[mid])

            #Recursively build the left subtree
            root.left = buildTree(left, mid-1)

            #Recursively build the right subtree
            root.right = buildTree(mid + 1, right)

            return root
        #The entire process for the whole array
        return buildTree(0, len(nums) - 1)
        
        
solution = Solution()
nums = [-10, -3, 0, 5, 9]
bst_root = solution.sortedArrayToBST(nums)

# Function to print BST inorder traversal for verification
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

inorder_traversal(bst_root)
