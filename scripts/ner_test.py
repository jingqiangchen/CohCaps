
import functools
from datetime import datetime
from multiprocessing import Pool

import ptvsd
import spacy
from docopt import docopt
from pymongo import MongoClient
from schema import And, Or, Schema, Use
from tqdm import tqdm


def test():
    title = "The spacecraft Juno will take 5 five years to reach orbit around Jupiter" + \
            "and then spend about one year gathering information on Jupiter' magnetic field, " + \
            "atmosphere and interior."
    nlp = spacy.load("/home/test/mic/softwares/en_core_web_lg-2.1.0")
    doc = nlp(title)
    for ent in doc.ents:
        changed = True
        ent_info = {
            'start': ent.start_char,
            'end': ent.end_char,
            'text': ent.text,
            'label': ent.label_,
        }
        print(ent_info)


if __name__ == '__main__':
    test()
