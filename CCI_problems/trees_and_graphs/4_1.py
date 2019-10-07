from queue import Queue

def find_path(node_a, node_b):
    queue = Queue()
    queue.add(node_a)
    node_a.visited = True

    while not queue.is_empty():
        children = queue.remove()

        for child in children:
            if child.visited == False:
                child.visited = True

                if child == node_b:
                    return True

                queue.add(child)


        return False
