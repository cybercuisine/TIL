a = []

def f(lis):
    ans_list = []

    pi = lis[0]
    for j in range(1,len(lis)):
        pj = lis[j]
        bij = a[pi][pj]

        if len(lis)>2:
            sub_list = lis[1:j]+lis[j+1:]

            sub_ans_list = f(sub_list)

            for sa in sub_ans_list:
                ans_list.append(sa^bij)
        else:
            ans_list.append(bij)

    return ans_list

def main():
    n = int(input())

    for i in range(2*n-1):
        a_row = list(map(int, input().split()))
        a_row = [0]*(i+1) + a_row
        a.append(a_row)

    lis = list(range(2*n))

    ans_list2 = f(lis)
    print(max(ans_list2))

main()
