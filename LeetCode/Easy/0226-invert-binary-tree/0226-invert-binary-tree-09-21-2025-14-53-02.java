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
    private TreeNode invert(TreeNode curr)
    {
        if(curr == null)
        {
            return curr;
        }
        if(curr.left != null)
        {
            curr.left = invert(curr.left);
        }
        if(curr.right != null)
        {
            curr.right = invert(curr.right);
        }
        TreeNode temp = curr.left;
        curr.left = curr.right;
        curr.right = temp;
        return curr;
    }

    public TreeNode invertTree(TreeNode root) {
        return(invert(root));
    }
}