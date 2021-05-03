
def MaximumProfit() -> None:
    
    n = int(input())
    R = []
    for i in range(n):
        R.append(int(input()))

    #探索範囲は0--i(i = 1--(n-1))
    max_prft = R[1] -R[0]
    min_R = R[0]
    max_i = 0
    min_i = 0
    for i in range(1, n):
        tmp_prft = R[i] - min_R
        tmp_min = R[i]
        if max_prft < tmp_prft:
            max_i = i
            max_prft = tmp_prft
        if min_R > tmp_min:
            min_R = tmp_min
            min_i = i
    
    print(f'max_prft: {max_prft} max_i: {max_i} min_i: {min_i}')


#memo
#出力の仕方　print(*a)
#挿入ソートは、外側のループiの場合、a[i]をiより左の範囲でなるべく左に持っていく（自分より小さいものがみつかったらそこでwhileとめる）
#
def InsertionSort() -> None:

    n = int(input())
    a = list(map(int, input().split()))

    print(*a)

    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = v

        print(*a)

#memo
#隣接していて逆転している場所がないかの探索をやる。
#列の最左端から最右端まで逆転が発見できない状態になるまで繰り返す。

#バブルソートはとにかく逆順になっているところを一つずつ交換されることで
#sort_jより右の範囲で一番小さいものが一番左まで送られる

def BubbleSort() -> None:

    n = int(input())
    a = list(map(int, input().split()))

    is_reverse = True

    # 逆転している場所が存在している間はずっと繰り返す
    count = 0
    while is_reverse:
        #ここでFalseにしたフラグが後でTrueに変わらなければループはお終い
        is_reverse = False
        #ソートが済んだ番号
        sort_j = 0
        #iはn-1から1まで a[i]とa[i-1]を比べる
        for i in range(n - 1, sort_j, -1):
            #逆転している場合
            if a[i] < a[i-1]:
                is_reverse = True
                a[i], a[i-1] = a[i-1], a[i]
                print(*a)
                count += 1
        sort_j += 1

    print(*a)
    print(count)
