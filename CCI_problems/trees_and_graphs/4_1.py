from queue import Queue

def find_path(node_a, node_b):
    if node_a == node_b:
        return True

    queue = Queue()
    queue.add(node_a)
    node_a.visited = True

    while not queue.is_empty():
        children = queue.remove()

        if children:
            for child in children:
                if child.visited == False:
                    child.visited = True

                    if child == node_b:
                        return True

                    queue.add(child)

            children.visited = True


    return False
