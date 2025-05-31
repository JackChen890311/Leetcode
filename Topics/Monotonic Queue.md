- [[L 外商面試考題] Sliding Window Maximum - Monotonic queue 的應用 - Benger Say 班格](https://bengersay.com/sliding-window-maximum/)
# [單調佇列的應用](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q#%E5%96%AE%E8%AA%BF%E4%BD%87%E5%88%97%E7%9A%84%E6%87%89%E7%94%A8)
![image](https://hackmd.io/_uploads/Syq69Jsrkg.png)
單調隊列的主要用途是處理「滑動窗口」問題。滑動窗口是指在數列中一段固定範圍內進行計算，像找最大值或最小值。


假設數列 value = [3, 2, -3, -1, 0]，求各個滑動窗口（k = 3）的最大值。
* 初始化：
    * queue = [] # (index, value) of element
    * result = [] # sliding window maximum
* 遍歷：
    * [3, 2, -3]: queue = [(0, 3), (1, 2), (2, -3)], result = [3]
        * The value of queue is monotonic
        * Add value[0] = 3 to result
    * [2, -3, -1]: queue = [(1, 2), (3, -1)], result = [3, 2]
        * Remove (2, -3) (value[2] = -3 < value[3] = -1)
        * Remove (0, -3) (exceeding boundary)
        * Add value[1] = 2 to result
    * [-3, -1, 0]: queue = [(4, 0)], result = [3, 1, 0]
        * Remove (3, -1) (value[3] = -1 < value[4] = 0)
        * Add (4, 0) in queue for this round
        * Remove 1 for exceeding boundary
        * Add value[4] = 0 to result
* 結果：[3, 2, 0]