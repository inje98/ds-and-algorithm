import random

class TreeNode():
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
dataAry = ['바나나맛우유', '래쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']

sellAry = [random.choice(dataAry) for _ in range(20)]
print(sellAry)

node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for name in sellAry[1:]:
    # 중복 체크 추가
    is_duplicate = False
    current = root
    while True:
        if name == current.data:
            is_duplicate = True
            break
        elif name < current.data:
            if current.left is None:
                break
            current = current.left
        else:
            if current.right is None:
                break
            current = current.right

    if not is_duplicate:
        node = TreeNode()
        node.data = name

        current = root
        while True:
            if name < current.data:
                if current.left is None:
                    current.left = node
                    memory.append(node)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    memory.append(node)
                    break
                current = current.right

def preorder(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)

preorder(root)