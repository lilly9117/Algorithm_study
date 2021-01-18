def solution(board, moves):
    bucket = []
    delete = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] > 0:
                bucket.append(board[i][m-1])
                board[i][m-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    delete.append(bucket[-1:])
                    bucket = bucket[:-2]
                break
    answer = len(delete) *2
    return answer