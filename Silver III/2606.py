# # 전체 컴퓨터 수
# n = int(input())
# # 인접리스트 graph 선언하기
# graph = [[] for _ in range(n+1)]
# # 연결 개수
# for _ in range(int(input())):
#     x, y = map(int,input().split())
#     graph[x].append(y)
#     graph[y].append(x)
#     # print("graph : ",graph)

# # 방문처리 : 방문한 컴퓨터 수를 출력해야해서 visited에 0/1로 처리
# visited = [0] * (n+1)

# def dfs(graph, v, visited):
#     visited[v] = 1
#     # print("visited : ",visited)
#     for i in graph[v]:
#         if visited[i] == 0:
#             dfs(graph, i, visited)
#     return True

# dfs(graph,1,visited)
# print(sum(visited) - 1)

# ------------------------
n = int(input())
m = int(input())

matrix = [[0] * (n+1) for i in range(n+1)]
seen = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

result = []
def dfs(v):
    seen[v] = 1
    for i in range(1, n+1):
        if matrix[v][i] == 1 and seen[i] == 0:
            result.append(i)
            dfs(i)
    return len(result)

print(dfs(1))