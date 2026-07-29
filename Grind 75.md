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