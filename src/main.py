from InputParser import InputParser
from CommandCenter import CommandCenter

def process_file(filename):
    parser = InputParser()
    parsed input = parser.parse("../input/" + filename + ".in")

    output = None
    outputfile = open("../output/" + filename + ".out", 'w')
    outputfile.write(output)

if __name__ == "__main__":

    files = ["a", "b", "c", "d", "e"]

    for file in files:
        print("starting file: "+file)
        process_file(file)
