from Solution import Solution, TreeNode
from typing import Optional

def main():
    input = list(input().split())
    root:Optional[TreeNode] = Optional[TreeNode]
    
    res = Solution.invertTree(root)
    print(res)

if __name__ == '__main__':
    main()