def solution(cake):
    return max([cake.count(cake[:index]) if cake.count(cake[:index]) > 1 and len(cake.replace(cake[:index], '')) == 0 else 1 for index in range(len(cake))])