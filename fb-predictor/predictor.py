from myparser import MyParser
from model import Model
from cli import Cli
import sys
import os

#DEFAULT PARAMETERS
NB_OF_BITS = 18
MODEL_NAME = None

#GET OPTIONS
dir_path = os.path.dirname(os.path.realpath(__file__))
full_path = os.path.join(dir_path, '../options.py')
exec(open(full_path).read())
get_opts()

model = Model()
model.load(MODEL_NAME)

parser = MyParser()
cli = Cli(parser, model, NB_OF_BITS)
cli.run()