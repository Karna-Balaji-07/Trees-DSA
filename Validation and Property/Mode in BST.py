# Find the mode in a binary search tree


def soln(root):
    dicts = {}
    def sol(root, dicts):
        if root is None:
            return
        sol(root.left)
        dicts[root.data] = dicts.get(root.data,0)+1
        sol(root.right)
        return dicts
    for key,value in dicts.items():
        if value > 1:
            return key
        