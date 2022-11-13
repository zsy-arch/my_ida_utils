import idautils
import idaapi
import idc


class gnustd_map_node:
    def __init__(self, left, right, data) -> None:
        self.left = left
        self.right = right
        self.data = data

    def __str__(self) -> str:
        return str(self.left) + ' ' + str(self.right) + ' ' + str(self.data)


def get_gnustd_map_node(addr):
    left_addr = addr + 0x010
    right_addr = addr + 0x018
    data_addr = addr + 0x020
    return gnustd_map_node(
        idc.read_dbg_qword(left_addr),
        idc.read_dbg_qword(right_addr),
        data_addr
    )


def get_gnustd_map_nodes(addr):
    res = []
    cur = get_gnustd_map_node(addr)
    res += [cur]
    if cur.left != 0:
        res += get_gnustd_map_nodes(cur.left)
    if cur.right != 0:
        res += get_gnustd_map_nodes(cur.right)
    return res


def get_gnustd_map(addr):
    return get_gnustd_map_nodes(idc.read_dbg_qword(addr + 0x10))


def get_gnustd_map2(addr):
    nodes = [idc.read_dbg_qword(addr + 0x10)]
    res = []
    while len(nodes) > 0:
        cur = nodes.pop()
        cur_node = get_gnustd_map_node(cur)
        res.append(cur_node)
        if cur_node.left != 0:
            nodes.append(cur_node.left)
        if cur_node.right != 0:
            nodes.append(cur_node.right)
    return res


for i, v in enumerate(get_gnustd_map(0x00007FFF250824B0)):
    print(hex(v.data), end=' ')

print()
