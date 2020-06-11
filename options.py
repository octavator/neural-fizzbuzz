import getopt
import sys

def get_opts():
    global NB_OF_BITS
    global NB_OF_SAMPLES
    global NB_OF_ITERATIONS
    global TEST_DATA_SIZE
    global MODEL_NAME

    opts, args = getopt.getopt(sys.argv[1:], 'b:s:i:t:m:',
    ['bits=', 'samples=', 'iterations=', 'test_size=', 'model_name='])
    for opt, arg in opts:
        if opt == '--bits' or opt == '-b':
            NB_OF_BITS = int(arg)
            assert(NB_OF_BITS > 4), 'Le nombre de bits doit être plus grand que 4'
        if opt == '--samples' or opt == '-s':
            NB_OF_SAMPLES = int(arg)
            assert(NB_OF_SAMPLES > 0), 'Le nombre d\'échantillons doit être strictement positif'
        if opt == '--iterations' or opt == '-i':
            NB_OF_ITERATIONS = int(arg)
            assert(NB_OF_ITERATIONS > 0), 'Le nombre d\'époques doit être strictement positif'
        if opt == '--test_size' or opt == '-t':
            TEST_DATA_SIZE = float(arg)
            assert(NB_OF_SAMPLES * (TEST_DATA_SIZE / 100) > 3), 'Le pourcentage de données test doit être plus grand'
        if opt == '--model_name' or opt == '-m':
            MODEL_NAME = arg
            assert(MODEL_NAME != ''), 'Le nom du model ne peut pas être vide'