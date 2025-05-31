- [Leetcode刷題學習筆記 – Monotonic Stack](https://hackmd.io/@meyr543/rkjS-x6wY)
- [【LeetCode】Monotonic Stack](https://ithelp.ithome.com.tw/articles/10263564?sc=iThelpR)
- 元素 push 上 stack 前，會把破壞此 stack 單調性質（遞增或遞減）的元素移除
- 可以找到已遍歷元素中，最靠近且比目前元素小 (遞增) / 大 (遞減)的元素 (previous / next  greater / less element)
- 可以找到目前為止最小(遞增)/大(遞減)的元素
# [單調堆疊的應用](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q#%E5%96%AE%E8%AA%BF%E9%81%9E%E6%B8%9B%E5%A0%86%E7%96%8A%EF%BC%88Monotonically-Decreasing-Stack%EF%BC%89)
單調堆疊的主要應用是快速處理「最近相關」的問題，特別是數列中每個元素的上一個/下一個更大值/更小值。

假設數列 value = [6, 2, 5, 7]，求每個數的「下一個更大值」。
* 初始化：
    * stack = [] # (index, value) of element
    * result = [-1, -1, -1, -1] # next greater element
* 遍歷：
    * 6: stack = [(0, 6)], result = [-1, -1, -1, -1]
    * 2: stack = [(0, 6), (1, 2)], result = [-1, -1, -1, -1]
    * 5: stack = [(0, 6), (2, 5)], result = [-1, 5, -1, -1]
        * Remove (1, 2) (value[1] = 2 < value[2] = 5)
        * result[1] = value[2] = 5
    * 7: stack = [(3, 7)], result = [7, 5, 7, -1]
        * Remove (2, 5) (value[2] = 5 < value[3] = 7)
        * result[2] = value[3] = 7
        * Remove (0, 6) (value[0] = 6 < value[3] = 7)
        * result[0] = value[3] = 7
* 結果：[7, 5, 7, -1]