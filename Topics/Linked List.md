- Finding middle element:
	```python
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		fast, slow = head, head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
	
		return slow
	```
- Reverse: [[206. Reverse Linked List (E)]]