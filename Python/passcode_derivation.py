from collections import defaultdict, deque

passcode_attempts = [
    319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710,
    629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290,
    719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362,
    319, 760, 316, 729, 380, 319, 728, 716
]

def find_passcode(passcode_attempts):
    graph = defaultdict(set) 
    in_degree = defaultdict(int)  

 
    for attempt in passcode_attempts:
        digits = str(attempt)
        for i in range(len(digits) - 1):
            if digits[i+1] not in graph[digits[i]]:
                graph[digits[i]].add(digits[i+1])
                in_degree[digits[i+1]] += 1
                in_degree[digits[i]]  

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    passcode = ''

    while queue:
        node = queue.popleft()
        passcode += node
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return passcode

print(find_passcode(passcode_attempts))
