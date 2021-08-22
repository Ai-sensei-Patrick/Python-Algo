"""
Tree
----

This file contains the tree data structure that will be used for interacting
with our coloured nodes.
The tree contains a "root" node, which is the topmost node of the tree.
It is interconnected through children and finally ends at external nodes ending
at the leaves.

*** Assignment Notes ***

This is the main file that will be tested, you must implement the related
functions with a TODO annotated.

Your task is to implement these methods.
"""

from node import Node
from colours import Colour
from colours import Colours


class Tree:
    """
    Tree Class
    ----------

    Contains the data structure of a tree, where each node of the tree has a
    parent and children.
    If a node has no parent, it is considered the "root" of the tree.
    If a node has zero (0) children, it is a leaf (or is "external").

    Each node in the tree has the type `Node`, which is defined in `node.py`.

    ====== Functions ======

    - __init__ : Sets up the tree with a specified root.
    - put(node, child) : Adds the `child` to the `node`.
    - swap(subtree_a, subtree_b) : Swaps the position of the subtrees.
    - is_coloured_to_depth_k(node, colour, k) : Checks that the subtree rooted
        at `node` has the same colour until `k` levels deep.

    == Things to note ==

    1. Every node given as an argument WILL be in the tree, you do not have to
        check whether it exists in the tree.
    2. Every node will be initialised with a parent (unless it is the root node
        of the tree).
    3. The ordering of the children does not matter.
    """

    def __init__(self, root: Node) -> None:
        """
        Initialises the tree with a root of type `Node` from `node.py`

        :param root: The root node of our tree.
        """

        self.root = root

    def update_node_colour(self, n: Node, new_colour: Colour) -> None:
        """
        Update the colour of a node.

        :param n: The node to change the colour of.
        :param new_colour: The new colour to change to.
        """
        # Call update_colour() on the node
        # TODO implement me please.
        n.update_colour(new_colour)
        self.update_prop_parent_ori(n)
        self.update_prop_colour(n)

    def update_prop_parent_ori(self, n: Node):
        
        n.propagated_colour = n.colour

        if n.parent != None:
            self.update_prop_parent_ori(n.parent)

    def update_prop_colour(self, n: Node):
        current_propcolour = n.propagated_colour
        children = n.get_children()
        for i in children:
            child_propcolour = i.propagated_colour
            if current_propcolour.cmp(child_propcolour) == -1:
                n.propagated_colour = child_propcolour
                current_propcolour = child_propcolour
        
        if n.parent != None:
            self.update_prop_colour(n.parent)
    
        
    def put(self, parent: Node, child: Node) -> None:
        """
        Inserts a node into the tree.
        Adds `child` to `parent`.

        :param parent: The parent node currently in the tree.
        :param child: The child to add to the tree.
        """
        # TODO implement me please.
        parent.add_child(child)
        self.update_prop_colour(parent)


    def rm(self, child: Node) -> None:
        """
        Removes child from parent.

        :param child: The child node to remove.
        """
        # TODO implement me please.
        parent = child.parent
        parent.remove_child(child)
        self.update_prop_parent_ori(parent)  
        self.update_prop_colour(parent)  

    def swap(self, subtree_a: Node, subtree_b: Node) -> None:
        """
        Swaps subtree A with subtree B

        :param subtree_a : Root of the subtree A.
        :param subtree_b : Root of the subtree B.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D

        SWAP(D, C)

            A
           / \
          D  B
              \
               C
              / \
             J   K
        """
        # TODO implement me please.
        parent_A = subtree_a.parent
        parent_B = subtree_b.parent
        self.rm(subtree_a)
        self.rm(subtree_b)
        self.put(parent_A,subtree_b)
        self.put(parent_B,subtree_a)

    def is_coloured_to_depth_k(self, start_node: Node, colour: Colour, k: int) -> bool:
        """
        Checks whether all nodes in the subtree (up and including level `k`
            starting from the start node) have the same colour!

        (This checks node.colour)

        :param start_node : The node to start checking.
        :param colour: The colour to compare a node's colour to.
        :param k: The depth we should check until.

        === Examples ===

        (start)---> G
                   / \
                  G   G
                 /|   |
                G R   G
                  |
                  R

        is_coloured_to_depth_k(start, Colour.GREEN, 0) => True
        is_coloured_to_depth_k(start, Colour.RED, 0) => False
        is_coloured_to_depth_k(start, Colour.GREEN, 1) => True
        is_coloured_to_depth_k(start, Colour.GREEN, 2) => False
        """

        # TODO implement me please.
        Final = True
        if k == 0:
            if start_node.colour.cmp(colour) == -1 or start_node.colour.cmp(colour) == 1:
                return False
            return True
        
        for i in start_node.children:
            if i.colour.cmp(colour) == -1 or i.colour.cmp(colour) == 1:
                return False
            Final = Final and self.is_coloured_to_depth_k(i, colour,k-1)

        return Final