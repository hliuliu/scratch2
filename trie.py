

class trie_node(object):
	def __init__(self):
		self.leaf = False
		self.value = None
		self.count = 0
		self.children = {}

	def __nonzero__(self):
		return True



class trie_dict(object):
	def __init__(self):
		self.root = trie_node()

	def __len__(self):
		return self.root.count

	def __nonzero__(self):
		return len(self)>0

	def add(self, key, value=None):
		curr = self.root
		stack = [curr]
		for ch in key:
			if ch not in curr.children:
				curr.children[ch] = trie_node()
			curr = curr.children[ch]
			stack.append(curr)

		has = curr.leaf
		curr.value = value
		curr.leaf = True
		
		if not has:
			while stack:
				stack.pop().count += 1
		

	def contains(self, key):
		node = self._findnode(key)
		return bool(node) or node.leaf

	def _findnode(self, key):
		curr = self.root
		for ch in key:
			if ch not in curr.children:
				return None
			curr = curr.children[ch]
		return curr

	def __contains__(self, key):
		return self.contains(key)

	def get_value(self,key):
		node = self._findnode(key)
		if node and node.leaf:
			return node.value
		raise KeyError('Invalid key: {}'.format(key))

	def _iter_by_node(self, node):
		if node is not None:
			q = [('',node)]
			while q:
				seq, node = q.pop(0)
				if node.leaf:
					yield seq
				for char, child in node.children.iteritems():
					q.append(seq+char, child)

	def iter_by_prefix(self, prefix):
		for seq in self._iter_by_node(self._findnode(key)):
			yield prefix+seq

	def count_by_prefix(self, prefix):
		node = self._findnode(prefix)
		return 0 if node is None else node.count






