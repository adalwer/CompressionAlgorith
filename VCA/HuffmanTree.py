
class HuffmanTree:

    def __init__(self):
        self.nodes = []
        self.leafs = []
        self.root = 0

    def add_leaf(self, name):
        identity = len(self.nodes)
        self.nodes.append(Node(identity=identity, name=name))
        self.leafs.append(identity)
        return identity

    def join(self, a, b):
        self.root = len(self.nodes)
        v1 = self.nodes[a]
        v2 = self.nodes[b]
        self.nodes.append(Node(identity=self.root, left=v1.identity, right=v2.identity))
        return self.root

    def get_left_child(self, v):
        return self.nodes[v].left

    def get_right_child(self, v):
        return self.nodes[v].right

    def get_children(self, v):
        return self.nodes[v].left, self.nodes[v].right

    def generate_codes(self, v, code=""):
        self.nodes[v].code = code

        l, r = self.get_children(v)

        if (not l == -1) and (not r == -1):
            self.generate_codes(l, code + "0")
            self.generate_codes(r, code + "1")

    def get_leafs(self):
        return [self.nodes[x] for x in self.leafs]


class Node:

    def __init__(self, identity=-1, left=-1, right=-1, name=-1):
        self.identity = identity
        self.left = left
        self.right = right
        self.code = ""
        self.name = name
