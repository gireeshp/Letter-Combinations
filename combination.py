#import pdb

def comb_fn (str, start, end):
    # pdb.set_trace()
    if start == end-1:
        print (str)
        str = swap(str, start, end)
        print (str)
    else:
        for i in range(start, end+1):
            comb_fn(move_to_first(str, i), start+1, end)

def swap (s, start, end):
    l = len(s)
    if l <= start-1 or start >= end or l<=end:
        return s
    else:
        return s[:start] + s[end] + s[start+1:end] + s[start] + s[end+1:]

def move_to_first (s, index):
    return s[index] + s[:index] + s[index+1:]
