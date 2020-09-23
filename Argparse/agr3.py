import argparse 
parser = argparse.ArgumentParser('Example with non-optional args')

parser.add_argument('counts', action="store", type=int)
parser.add_argument('units', action="store")


print parser.parse_args()
