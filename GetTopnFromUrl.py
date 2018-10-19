import sys
from urllib.request import urlopen

def fetch_content(url):
    with urlopen(url) as content:
        lines = []
        for line in content:
            line_word = line.decode('utf-8')
            lines.append(line_word)
    return lines

def select_topn(lines, N):
    result = {}
    for line in lines:
        #ignore the first line since it is a title
        if(line.startswith('name')):
            continue
        words = line.split(",")
        if((not result) or (len(result) < N)):
            result[words[2]] = line
        #if already has N line, replace the lowest line if current one is bigger in rating
        elif(len(result) == N):
            lowest = list(result.keys())[0]
            for k in result.keys():
                if(lowest > k):
                    lowest = k
            if(lowest < words[2]):
                del result[lowest]
                result[words[2]] = line

    return result.values()

def print_topn(topn_lines):
    for line in topn_lines:
        print(line)


def main(arg1, arg2):
    #https://gist.githubusercontent.com/tyrchen/32c50aadca48aee3da10a77a18479517/raw/3aa07629e61239cd26cf514584c949a98aa38d67/movies.csv
    lines = fetch_content(arg1)
    topNitems = select_topn(lines, int(arg2))
    print_topn(topNitems)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
