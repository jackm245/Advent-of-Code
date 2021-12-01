from linked_list import * #doubly linked list

def get_data():
    with open('data.in', 'r') as f:
        L = [int(l.strip()) for l in f.readline().strip()]
    return L

def solve(is_p2):
    nums = get_data()
    X = LinkedList()
    prev = None
    for x in nums:
        prev = X.append(prev, x)
    if is_p2:
        next_ = 10
        while len(X.D) < int(1e6):
            prev = X.append(prev, next_)
            next_ += 1
        assert next_ == int(1e6)+1
    N = len(X.D)

    t = 0 
    current = X.find(nums[0])
    nmoves = int(1e7) if is_p2 else 100
    for _ in range(nmoves):
        t += 1
        current_num = current.value
        pickup = []
        pickup_node = current.next
        for _ in range(3):
            pickup.append(pickup_node.value)
            tmp = pickup_node.next
            pickup_node.erase()
            pickup_node = tmp

        dest = N if current_num==1 else current_num-1
        while dest in pickup:
            dest = N if dest==1 else dest-1

        dest_node = X.find(dest)
        for x in pickup:
            dest_node = dest_node.insert(x)
        assert current == X.find(current_num)
        current = current.next

    if is_p2:
        node_1 = X.find(1)
        return node_1.next.value*node_1.next.next.value
    else:
        values = X.to_list(1)
        return ''.join([str(x) for x in values[1:]])

print(solve(False))
print(solve(True))
