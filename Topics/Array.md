# Interval
## Determine if 2 interval is overlapped

```python
def is_overlapping(a: List[int], b: List[int]) -> bool:
	return a[0] <= b[1] and b[0] <= a[1]
```

既然「不重疊」的條件是：
- `end₁ < start₂` OR `start₁ > end₂`
那「重疊」就是把上面的條件**全部反過來（加個「不」字）**：
- `end₁ < start₂` 反過來 ➡️ `end₁ >= start₂`（意即：A 撐得夠久，有機會碰到 B 的開頭）
- `start₁ > end₂` 反過來 ➡️ `start₁ <= end₂`（意即：A 開始得夠早，有機會在 B 結束前碰到）
當這兩個反過來的條件**同時成立**（AND）時，它們就一定塞在同一個區間內，也就是重疊了！

## Merge 2 interval
- Check if overlap first
- Then take min and max
```python
def merge_two_intervals(a, b): 
	# Step 1: Check if they actually overlap 
	if a <= b and b <= a: 
	# Step 2: Combine boundaries 
		return [min(a, b), max(a, b)] 
	return None
```