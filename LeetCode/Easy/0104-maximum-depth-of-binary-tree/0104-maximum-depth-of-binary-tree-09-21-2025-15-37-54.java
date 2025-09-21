/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int getDepth(TreeNode x)
    {
        if(x == null)
        {
            return 0;
        }
        int myDepth = Math.max(getDepth(x.left) + 1,getDepth(x.right) + 1);
        return myDepth;
    }

    public int maxDepth(TreeNode root) {
        return getDepth(root);
    }
}