def split_and_join(line):
    # write your code here
    SplitList  = line.split(" ")
    JoinString = "-".join(SplitList)
    return JoinString

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)