def solution(n,m,k,data:list) -> int:
    data.sort() # 정렬, 마지막 인덱스 
    first_large = data[n-1]
    second_large = data[n-2]
    sol = 0
    tmp_k = k
    while(m>0):
        if(tmp_k>0):
            sol+=first_large
            tmp_k -=1
        else:
            sol+=second_large
            tmp_k=k
        m-=1
    return sol




if __name__ == "__main__":
    n, m, k = map(int,input().split())
    data = list(map(int,input().split()))
    answer = solution(n,m,k,data)
    print(answer)
