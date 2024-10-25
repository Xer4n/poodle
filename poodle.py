#Poodle attack by Simen Andersen
#Email: SimAnd48374@stud.noroff.no

from textwrap import wrap
import sys

file = sys.argv[1]

def read_file(file):
    accepted_lines = []
    with open(file, "r") as f:
        for line in f:
            line = line.split(",")
            if len(line) > 1:
                line[1] = line[1].rstrip()
                if (line[1] == "ACCEPTED"):
                    accepted_lines.append(line)
            elif len(line) == 1:
                line[0] = line[0].rstrip()
                accepted_lines.append(line)
        f.close()

    return accepted_lines


def calculate_cookie(c_rminone, block_cr_minone, block_cn_minone):
    c_nminone = len(block) - 1


    block = wrap(block, 2)
    
    for i in range(len(block)-1):
        pass
    


def main():
    traces = read_file(file)
    cookie = []
    
    ssl_size = traces[0]
    c_r = traces[1]
    
    c_rminone = int(c_r[0]) - 1

    traces.pop(0)
    traces.pop(1)

    for line in traces:
        blocks = line[0].split(" ")
        
        for i in range(len(blocks)):
            cookie.append(calculate_cookie(c_rminone, blocks[i-1][c_rminone], blocks[i-1][len(blocks[i-1]-1)]))
     




if __name__ == "__main__":
    main()
