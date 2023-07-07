# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        res = []

        def preorder(node):
            if not node:
                res.append('N')
                return

            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        ls = data.split(',')
        self.i = 0

        def preorder():
            if self.i >= len(ls):
                return None

            val = ls[self.i]
            self.i += 1

            if val != 'N':
                new_node = TreeNode(int(val))
                new_node.left = preorder()
                new_node.right = preorder()
                return new_node

        return preorder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
