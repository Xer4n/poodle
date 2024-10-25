#Poodle attack by Simen Andersen
#Email: SimAnd48374@stud.noroff.no

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
                    print(line[1])
        


def main():
    read_file(file)




if __name__ == "__main__":
    main()
