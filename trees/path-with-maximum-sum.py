import math


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class MaximumPathSum:

  def find_maximum_path_sum(self, root):
    self.globalMaximumSum = -math.inf
    self.find_maximum_path_sum_recursive(root)
    return self.globalMaximumSum

  def find_maximum_path_sum_recursive(self, currentNode):
    if currentNode is None:
      return 0

    maxPathSumFromLeft = self.find_maximum_path_sum_recursive(
      currentNode.left)
    maxPathSumFromRight = self.find_maximum_path_sum_recursive(
      currentNode.right)

    # ignore paths with negative sums, since we need to find the maximum sum we should
    # ignore any path which has an overall negative sum.
    maxPathSumFromLeft = max(maxPathSumFromLeft, 0)
    maxPathSumFromRight = max(maxPathSumFromRight, 0)

    # maximum path sum at the current node will be equal to the sum from the left subtree +
    # the sum from right subtree + val of current node
    localMaximumSum = maxPathSumFromLeft + maxPathSumFromRight + currentNode.val

    # update the global maximum sum
    self.globalMaximumSum = max(self.globalMaximumSum, localMaximumSum)

    # maximum sum of any path from the current node will be equal to the maximum of
    # the sums from left or right subtrees plus the value of the current node
    return max(maxPathSumFromLeft, maxPathSumFromRight) + currentNode.val


def main():
  maximumPathSum = MaximumPathSum()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()
