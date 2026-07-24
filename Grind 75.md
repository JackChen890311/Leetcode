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
### [[57. Insert Interval (M)]]
卡了一陣子，最後用 binary search 先找出插入點，再把它變成 [[56. Merge Intervals (M)]] 檢查每個 interval merge 起來
關於 interval 的一些操作可以看 [[Array]]
### [[542. 01 Matrix (M)]]
Multi-source BFS，將所有 0 都加入初始節點，並在 traverse 時加入距離，重複就不用再走
### [[973. K Closest Points to Origin (M)]]
### [[3. Longest Substring Without Repeating Characters (M)]]
### [[15. 3Sum (M)]]
原本用 [[Two Pointers]]，看來沒辦法掃過所有情況，應該只能用在“當確定前面的元素不會再用到的 case”？