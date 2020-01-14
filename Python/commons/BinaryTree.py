from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_node(lst: List[int]) -> TreeNode:
    """
    Create a Binary Tree using BFS according to the per-layer list
    """
    if len(lst) == 0:
        return None
    forest = [TreeNode(item) for item in lst]
    count = len(forest)
    for i, tree in enumerate(forest):
        left_index = 2 * i + 1
        if left_index < count:
            tree.left = forest[left_index]

        right_index = 2 * i + 2
        if right_index < count:
            tree.right = forest[right_index]

    return forest[0]  # root


def get_list(node: TreeNode) -> List[int]:
    """
    Get the list of values by level under the node
    """
    res = []
    curr_level = [node]
    while len(curr_level) != 0:
        next_level = []
        for curr in curr_level:
            if curr is not None:
                res.append(curr.val)
                if curr.left:
                    next_level.append(curr.left)
                if curr.right:
                    next_level.append(curr.right)
        curr_level = next_level
    return res


if __name__ == "__main__":
    node = create_node([1, 2, 3, 4, None, None, 5])
    print(get_list(node))
