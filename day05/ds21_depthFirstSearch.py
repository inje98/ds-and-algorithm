# file : ds21_depthFirstSearch.py
# desc : 그래프 깊이 우선 탐색 구현


# 그래프 클래스 선언
class Graph():
    SIZE = graph = None  # 멤버변수

    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]

# 전역변수 선언
G1 = None
stack = []
visited = []
MAX = 4

# 메인코드
G1 = Graph(MAX)
G1.graph[0][2] = G1.graph[2][0] = 1 #(A, C)
G1.graph[0][3] = G1.graph[3][0] = 1 #(A, D)
G1.graph[1][2] = G1.graph[2][1] = 1 #(B, C)
G1.graph[2][3] = G1.graph[3][2] = 1 #(C, D)

print('무방향 그래프 > ')

for row in range(MAX):
    for col in range(MAX):
        print(G1.graph[row][col], end='  ')
    print()

## 탐색 시작
curr = 0 # 시작 정점 Vertex
stack.append(curr)
visited.append(curr)

while len(stack) != 0:
    next = None # 다음 정점을 초기화
    for vertex in range(MAX):
        if G1.graph[curr][vertex] == 1:
            if vertex in visited:
                pass
            else:
                next = vertex
                break

    if next != None: # 다음 정점이 있으면
        curr = next
        stack.append(curr) # 스택에 방문한 정점 push
        visited.append(curr) # 방문기록 등록
    else:
        curr = stack.pop() # 스택에서 현재 정점 pop

print('방문순서 --> ', end='')
for i in visited:
    print(chr(ord('A') + i), end='')
