# def solve(n,x,y):
#     global result
#     if n == 2:
#         if x == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x == X and y+1 == Y:
#             print(result)
#             return
#         result += 1
#         if x+1 == X and y == Y:
#             print(result)
#             return
#         result += 1
#         if x+1 == X and y+1 == Y:
#             print(result)
#             return
#         result += 1
#         return
#     solve(n/2, x, y)
#     solve(n/2, x, y+n/2)
#     solve(n/2, x+n/2, y)
#     solve(n/2, x+n/2, y+n/2)

# result = 0
# N,X,Y = map(int, input().split())
# solve(2**N,0,0)



# ----------------------------------------------

# N, r, c = map(int, input().split())

# ans = 0

# while N != 0:

# 	N -= 1

# 	# 1사분면
# 	if r < 2 ** N and c < 2 ** N:
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 0

# 	# 2사분면
# 	elif r < 2 ** N and c >= 2 ** N: 
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 1
# 		c -= ( 2 ** N )
        
# 	# 3사분면    
# 	elif r >= 2 ** N and c < 2 ** N: 
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 2
# 		r -= ( 2 ** N )
        
# 	# 4사분면    
# 	else:
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 3
# 		r -= ( 2 ** N )
# 		c -= ( 2 ** N )
    
# print(ans)

N, r, c = map(int, input().split())

def sol(N, r, c):

	if N == 0:
		return 0
        
	return 2*(r%2)+(c%2) + 4*sol(N-1, int(r/2), int(c/2))

print(sol(N, r, c))