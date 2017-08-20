#import pdb
output_list = []

def comb_fn (str, start, end):
    # pdb.set_trace()
    global output_list

    if start == end-1:
        output_list.append(str)

        str = swap(str, start, end)
        output_list.append(str)
    else:
        for i in range(start, end+1):
            comb_fn(move_to_first(str, i), start+1, end)


def swap (s, start, end):
    l = len(s)
    if any([l <= start-1, start >= end, l <= end]):
        return s
    else:
        return s[:start] + s[end] + s[start+1:end] + s[start] + s[end+1:]


def move_to_first (s, index):
    return s[index] + s[:index] + s[index+1:]
