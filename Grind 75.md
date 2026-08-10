### [[1. Two Sum (E)]]
### [[20. Valid Parentheses (E)]]
### [[21. Merge Two Sorted Lists (E)]]
### [[121. Best Time to Buy and Sell Stock (E)]]
最佳解：對於所有當下價格找歷史最低價
### [[125. Valid Palindrome (E)]]
### [[226. Invert Binary Tree (E)]]
### [[242. Valid Anagram (E)]]
### [[704. Binary Search (E)]]
### [[733. Flood Fill (E)]]
### [[235. Lowest Common Ancestor of a Binary Search Tree (M)]]
想了一下，用 BST 的性質來做
### [[110. Balanced Binary Tree (E)]]
卡住了QQ Traverse + return depth + -1 for invalid
### [[141. Linked List Cycle (E)]]
### [[232. Implement Queue using Stacks (E)]]

---
### [[278. First Bad Version(E)]]
Binary Search 基本題，分析了一下 base case
### [[383. Ransom Note (E)]]
### [[70. Climbing Stairs (E)]]
### [[409. Longest Palindrome (E)]]
### [[206. Reverse Linked List (E)]]
### [[169. Majority Element (E)]]
### [[67. Add Binary (E)]]
### [[543. Diameter of Binary Tree (E)]]
卡住，但就是針對每個 node 算 lh + rh，然後取最大就好
### [[876. Middle of the Linked List (E)]]
### [[104. Maximum Depth of Binary Tree (E)]]
dfs 找最長路徑（最深）
### [[217. Contains Duplicate (E)]]
### [[53. Maximum Subarray (M)]]
Kadane's Algorithm，注意細節，像是 local 要取 max(nums[i], nums[i] + local)，因為必選至少一個

---
### [[57. Insert Interval (M)]]
卡了一陣子，最後用 binary search 先找出插入點，再把它變成 [[56. Merge Intervals (M)]] 檢查每個 interval merge 起來
關於 interval 的一些操作可以看 [[Array]]
### [[542. 01 Matrix (M)]]
Multi-source BFS，將所有 0 都加入初始節點，並在 traverse 時加入距離，重複就不用再走
### [[973. K Closest Points to Origin (M)]]
### [[3. Longest Substring Without Repeating Characters (M)]]
### [[15. 3Sum (M)]]
原本用 [[Two Pointers]]，看來沒辦法掃過所有情況，應該只能用在“當確定前面的元素不會再用到的 case”？
感覺是個爛題目 @@
### [[102. Binary Tree Level Order Traversal (M)]]
### [[133. Clone Graph (M)]]
先 traverse 一遍把 graph 的狀態用 adjacency list 記下來
然後再依據他建一個新 graph
### [[150. Evaluate Reverse Polish Notation (M)]]
不要從尾開始，這樣會超久
從頭開始，遇到數字先記到 stack，遇到運算元再 pop 出來運算，然後把結果推回去

---
### [[207. Course Schedule (M)]]
兩種方法：
- 檢查圖有無 cycle：Traverse + 灰白黑 marking
- Topological Sort with Kahn's Algorithm (Refer to [[210. Course Schedule II (M)]])
### [[208. Implement Trie (Prefix Tree) (M)]]
記得不要覆蓋掉原本的紀錄
### [[322. Coin Change (M)]]
還在擔心暴力dp會不會太慢
### [[238. Product of Array Except Self (M)]]
第一次寫，注意不能用除的
### [[155. Min Stack (M)]]
Original Stack + Monotonic Stack
### [[98. Validate Binary Search Tree (M)]]
### [[200. Number of Islands (M)]]
### [[994. Rotting Oranges (M)]]
跟 [[542. 01 Matrix (M)]] 類似，只是換成三種狀態

---
### [[33. Search in Rotated Sorted Array (M)]]
分兩段判斷：前半 / 後半，可以用比較大小 or 減去第一項的方式來看，再根據在哪一半決定怎麼移動
### [[39. Combination Sum (M)]]
正常來說應該要用 backtracking，但我覺得他長得很像前幾天做的 [[518. Coin Change II (M)]]
Think of this problem as "Unbounded Knapsack Problem" but the result we want is the item in the knapsack. Same approach with a little tweak will do the work.
### [[46. Permutations (M)]]
### [[56. Merge Intervals (M)]]
前面做 [[57. Insert Interval (M)]] 的時候做過
### [[236. Lowest Common Ancestor of a Binary Tree (M)]]
前面做過
### [[981. Time Based Key-Value Store (M)]]
### [[721. Accounts Merge (M)]]
基本上就是用 [[Union Find]] 的概念來解，只是要處理一些麻煩的東西，像是 sorted result、dedup 等等，就可以了
要複習一下 UF 的寫法！（在 union 的時候更新的是兩個的 root，同時可以用 size 來判斷誰合進去誰，還有 find 寫法）
### [[75. Sort Colors (M)]]
第二次做，明明知道概念但一直做不出來 ==

---
### [[139. Word Break (M)]]
第一次做，原本想用 graph + traversal 的方式，但這樣時間複雜度會太高，還要處理 "aaaaa" 這種問題
DP 的方式很漂亮，針對每個位置，每個字，去看這個位置剪掉這個字的長度的地方，是否可以抵達，好聰明！
反正我們不關心走法，只關心能不能抵達
### [[416. Partition Equal Subset Sum (M)]]
卡住了，沒啥頭緒，可以用背包問題來解（放入等於總價值一半的物品）
！！！一維 DP + 用 set 紀錄可以到達的所有數字，如果一半中途出現就是可以抵達，真是高明...
### [[8. String to Integer (atoi) (M)]]
### [[54. Spiral Matrix (M)]]
 要注意超出邊界 & 碰到重複的都要轉向
### [[78. Subsets (M)]]
用 bitmask 來做不錯
### [[199. Binary Tree Right Side View (M)]]
### [[5. Longest Palindromic Substring (M)]]
好難喔忘光了，用二維 DP 來做
還有其他更快的方法，但我放棄理解了 QQ
### [[62. Unique Paths (M)]]
### [[105. Construct Binary Tree from Preorder and Inorder Traversal (M)]]
---
### [[11. Container With Most Water (M)]]
原本在想用 monotonic stack 做，覺得怪怪的，結果不是，就 [[Two Pointers]] 移動模擬計算就好
裡面有證明可以看
### [[17. Letter Combinations of a Phone Number (M)]]
經典 [[Backtracking]] 題目！第三次做輕鬆解決～
### [[79. Word Search (M)]]
原本用 dfs 搭配紀錄走過的地方來做，很慢（visited set 要 copy），去看才又發現可以用 backtracking 來做比較快（精神是因為走過的不能再走所以可以用 backtracking?）
### [[438. Find All Anagrams in a String (M)]]
### [[310. Minimum Height Trees (M)]]
笑死我上次也只留了 TODO 在裡面
解答：用撥洋蔥的方式，每次都把所有的 leaves 全部丟掉，剩下的就是最長路徑的中間那幾點了（因為最晚被撥洋蔥去掉）
### [[621. Task Scheduler (M)]]
 用數學就可以算出來了，點進去看細節
### [[146. LRU Cache (M)]]
點進去看，Hash + Doubly Linked List

---
### [[230. Kth Smallest Element in a BST (M)]]
### [[76. Minimum Window Substring (H)]]
有點像 [[438. Find All Anagrams in a String (M)]]
用 idx 來紀錄結果，不要複製字串，會比較快
用一個 counter 檢查是不是 freq 剪掉後都 <= 0 就好，就不用比兩個 freq