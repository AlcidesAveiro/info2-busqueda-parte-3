import matplotlib.pyplot as plt

# Define the tree structure
tree = {
    "value": "+",
    "children": [
        {
            "value": "-",
            "children": [
                {"value": "a"},
                {"value": "4"}
            ]
        },
        {
            "value": "c"
        }
    ]
}
# Function to recursively plot the tree
def plot_tree(node, x, y, dx, dy):
    plt.text(x, y, node["value"], ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))
    if "children" in node:
        y_next = y - dy
        x_left = x - dx * len(node["children"]) / 2
        for child in node["children"]:
            x_child = x_left + dx / 2
            plt.plot([x, x_child], [y, y_next], color='black')
            plot_tree(child, x_child, y_next, dx, dy)
            x_left += dx

# Plot the tree
plt.figure(figsize=(8, 6))
plot_tree(tree, 0, 0, 2, 1.5)
plt.axis('off')
plt.show()