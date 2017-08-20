from combinations import combination as comb

if __name__ == "__main__":
    input_str = input('Enter the string: ')
    comb.comb_fn(input_str, 0, len(input_str)-1)
    for output in comb.output_list:
        print(output)
