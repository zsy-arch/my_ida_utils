import idaapi


class Node:
    def __init__(self, bts, data, left, right) -> None:
        self.bts = bts
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return '{{\'data\': {0}, \'left\': {1}, \'right\': {2}}}'.format(str(self.data), str(self.left), str(self.right))


class BinaryTreeStruct:
    def __init__(self, data_offset, data_size, left_offset, right_offset) -> None:
        self.is_64bit = False
        if idaapi.get_inf_structure().is_64bit():
            self.is_64bit = True
        self.data_offset = data_offset
        self.data_size = data_size
        self.left_offset = left_offset
        self.right_offset = right_offset

    def readData(self, ea: int):
        return idaapi.get_bytes(ea + self.data_offset, self.data_size)

    def readXNode(self, ea, offset):
        if self.is_64bit:
            addr = idaapi.get_qword(ea + offset)
        else:
            addr = idaapi.get_dword(ea + offset)
        return addr

    def readLeftNode(self, ea):
        addr = self.readXNode(ea, self.left_offset)
        return addr

    def readRightNode(self, ea):
        addr = self.readXNode(ea, self.right_offset)
        return addr


def buildTree(bts: BinaryTreeStruct, ea: int) -> Node:
    data = bts.readData(ea)
    left_ea = bts.readLeftNode(ea)
    print(left_ea)
    right_ea = bts.readRightNode(ea)
    if not (None == left_ea or 0 == left_ea):
        leftNode = buildTree(bts, left_ea)
    else:
        leftNode = None
    if not (None == right_ea or 0 == right_ea):
        rightNode = buildTree(bts, right_ea)
    else:
        rightNode = None
    node = Node(bts, data, leftNode, rightNode)
    return node


def run():
    bts = BinaryTreeStruct(0, 4, 8, 16)
    root = buildTree(bts, 0x0000028A72FD3FD0)
    print(root)
    pass


run()
