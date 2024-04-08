import argparse

parser = argparse.ArgumentParser(
    prog="argparsetest.py",
    description="test code for argparse",
    epilog="this is test code for argparse",
)
parser.add_argument('--foo', help='foo help')
parser.add_argument('--bar', help='bar help')
args = parser.parse_args()

print(args.foo)
print(args.bar)

# argparseのtestコード　
# このスクリプトを--foo 1 --bar 2という引数で実行すると、1と2が出力される

# PS C:\cityscope_methods\CS_CityScoPy-master\CS_CityScoPy-master> python argparsetest.py --foo 1
# 1
# None
# PS C:\cityscope_methods\CS_CityScoPy-master\CS_CityScoPy-master> python argparsetest.py --foo 1 --bar 3
# 1
# 3


# PS C:\cityscope_methods\CS_CityScoPy-master\CS_CityScoPy-master> python argparsetest.py -h
# usage: argparsetest.py [-h] [--foo FOO] [--bar BAR]

# test code for argparse

# optional arguments:
#   -h, --help  show this help message and exit
#   --foo FOO   foo help
#   --bar BAR   bar help

# this is test code for argparse