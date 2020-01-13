from draw import *
import random

def make_tree(n, max_branches=4):
	'''
	Returns a Tree object with 'n' nodes and at most max_branches branches per node. Labels are integers.

	Entering a large 'n' (around 35 or greater) or a large 'max_branches' (around 7 or greater) will likely
	result in error since the tree will not fit on the window.     
	'''
	assert n > 0, 'A Tree must have at least 1 node.'
	assert max_branches > 0, 'Cannot have max_branches <= 0.'
	
	t = Tree(n)
	n = n - 1
	d = {0: [t]}
	level = 1	
	
	while n > 0:
		d[level] = []
		for tree in d[level - 1]:
			i = max_branches - random.randint(0, max_branches)
			while i < max_branches or d[level] == []:
				i = i + 1
				a = Tree(n)
				tree.branches.append(a)
				d[level].append(a)
				n = n - 1
				if n <= 0:
					break
			if n <= 0:
				break
		level += 1

	return t

#reassign tree to any tree you want to draw, or use make_tree() to create a random tree 
tree = make_tree(12)

#DO NOT CHANGE THIS LINE
set_all(tree, width, height, radius, h_offset, v_offset)

#set animate to True if you want to see the tree drawn step-by-step
visualize(tree, animate=True)


						









