def sort_by_end(jobs):   #終了時刻が早い順にソート
    n = len(jobs)
    for i in range(n - 1):
        for j in range(n -1 - i):
            if jobs[j][1] > jobs[j+1][1]:
                jobs[j], jobs[j+1] = jobs[j+1], jobs[j]
    #print("sorted jobs:", jobs)

def is_not_overlapped(job, jobs):#jobs内の要素同士は重なっていない
    return (len(jobs) == 0 or jobs[-1][1] <= job[0])

def q(j, jobs):
    returner = -1
    for k in range(j-1, -1, -1):
        if jobs[k][1] <= jobs[j][0]:
            returner = k
            break
    return returner#-1なら存在しない
def opt(j, jobs, opts):#opt_j-1までは埋まってる想定
    if j == -1:
        return 0
    return max(opts[q(j, jobs)] + jobs[j][2], opts[j-1])#j = 0の時でも値が決まる前のopts[n] = 0にアクセスするから平気なはず
def find_opt_select(jobs, opts):
    returner = []
    j = len(jobs) - 1
    while j >= 0:
        if opts[j] != opts[j-1]:
            returner.append(j)
            j = q(j, jobs)
        else:
            j -= 1
    #何か適切な処理を加えなきゃ?

    return returner
n = int(input())
jobs = []
for i in range(n):
    jobs.append([int(x) for x in input().split()])
sort_by_end(jobs)
# for i in range(n):
#     print("q", i + 1, "=", q(i, jobs) + 1)
opts = [0 for _ in range(n+1)]#opts[-1]を扱いたいためn+1
for i in range(n):
    opts[i] = opt(i, jobs, opts)
# for i in range(n):
#     print("opt", i+1, "=", opts[i])

answer = find_opt_select(jobs, opts)
#answer.sort()
print(list(map(lambda x: x+1, answer)))