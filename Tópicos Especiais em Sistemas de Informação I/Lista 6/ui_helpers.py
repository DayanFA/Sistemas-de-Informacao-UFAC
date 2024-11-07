import tkinter as tk
from tkinter import ttk

def create_treeview_with_scrollbars(parent):
    tree_frame = tk.Frame(parent)
    tree_frame.pack(fill=tk.BOTH, expand=True)

    tree_scroll_y = tk.Scrollbar(tree_frame, orient=tk.VERTICAL)
    tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

    tree_scroll_x = tk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
    tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

    tree = ttk.Treeview(tree_frame, show='headings', yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
    tree.pack(fill=tk.BOTH, expand=True)

    tree_scroll_y.config(command=tree.yview)
    tree_scroll_x.config(command=tree.xview)

    return tree