def read_list(filename, all_nums=False):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    if all_nums:
        for idx in range(len(content)):
            content[idx] = int(content[idx])
    return content
