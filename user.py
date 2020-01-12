from draw import *

example = Tree(0, [Tree(0, [Tree(9), Tree(5, [Tree(0, [Tree(9), Tree(5, [Tree(1), Tree(2), Tree(3), Tree(4)]), Tree(7), Tree(6)])]), 
	 Tree(7), Tree(6), Tree(10)]), Tree(0, [Tree(9, [Tree(0, [Tree(9, [Tree(0, [Tree(9, [Tree(1, [Tree(0), Tree(2), Tree(4), Tree(6), Tree(8), Tree(10), Tree(12)])]), 
	 Tree(5), Tree(5)])]), Tree(5), Tree(5)])]), Tree(5), Tree(5)]), Tree(1, [Tree(4), Tree(5, [Tree(2, [Tree(5, [Tree(0, [Tree(9), Tree(5, [Tree(1), Tree(2), Tree(3), 
	 Tree(4)]), Tree(7), Tree(6)])]), Tree(7), Tree(6), Tree(10, [Tree(6), Tree(2)]), Tree(11)])]), Tree(6), Tree(9, [Tree(12, [Tree(13), Tree(14, [Tree(16), Tree(24), 
	 Tree(17, [Tree(4), Tree(5, [Tree(7), Tree(9)])])])])])])])

#reassign tree to any tree you want to draw
tree = example

'''
DON'T CHANGE ANY OF THE SETTING CODE
'''
set_parents(tree)
set_levels(tree)
set_repr_occurrences(tree)
set_coords(tree, width*0.5, height*0.75, radius, h_offset, v_offset)			
set_circles(tree, radius)
set_texts(tree)

#set animate to True if you want to see the tree drawn step-by-step
#set draw_with_error to True if you want to draw the tree even if it goes beyond the screen or there is overlap of text and nodes
visualize(tree, animate=True, draw_with_error=False)


						









