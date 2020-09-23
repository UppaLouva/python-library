import argparse 
import arg6

parser = argparse.ArgumentParser(parents=[arg6.parser])

parser.add_argument('--local-arg', action="store_true", default=False)

print parser.parse_args()
