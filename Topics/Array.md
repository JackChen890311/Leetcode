# Interval
## Determine if 2 interval is overlapped

```python
def checkOverlap(int1: List[int], int2: List[int]) -> bool:
	return int1[0] <= int2[1] and int2[0] <= int1[1]
```
### 直覺理解
「不重疊」的條件是：
- `end₁ < start₂` OR `start₁ > end₂`（意即：A 結束的比 B 早或 A 開始的比 B 晚）
那「重疊」就是把上面的條件**全部反過來（加個「不」字）**：
- `end₁ < start₂` 反過來 ➡️ `end₁ >= start₂`（意即：A 撐得夠久，有機會碰到 B 的開頭）
- `start₁ > end₂` 反過來 ➡️ `start₁ <= end₂`（意即：A 開始得夠早，有機會在 B 結束前碰到）
當這兩個反過來的條件**同時成立**（AND）時，它們就一定塞在同一個區間內，也就是重疊了！

## Merge 2 interval
- Check if overlap first
- Then take min and max
```python
def mergeInterval(int1: List[int], int2: List[int]) -> Optional[List[int]]:
	if checkOverlap(int1, int2):
		return [min(int1[0], int2[0]), max(int1[1], int2[1])]
	return None
```

## Union of 2 interval
- Check if overlap first
- Then take max and min
```python
def unionOfInterval(int1: List[int], int2: List[int]) -> Optional[List[int]]:
	if checkOverlap(int1, int2):
		return [max(int1[0], int2[0]), min(int1[1], int2[1])]
	return None
```