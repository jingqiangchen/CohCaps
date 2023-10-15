import logging
import os
import random
import re
from typing import Dict

import numpy as np
import pymongo
import torch

from PIL import Image
from pymongo import MongoClient
from tqdm import tqdm

import sys, json

from pycocoevalcap.rouge.rouge import Rouge

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name

class DailyMailStatistics:

    def __init__(self,
                 image_dir: str = "/home/test/images_processed_dailymail",
                 mongo_host: str = 'localhost',
                 mongo_port: int = 27017) -> None:
        self.client = MongoClient(host=mongo_host, port=mongo_port)
        self.db = self.client.dailymail
        self.image_dir = image_dir

        self.rouge_scorer = Rouge()
        
        random.seed(1234)
        self.rs = np.random.RandomState(1234)

        roberta = torch.hub.load('pytorch/fairseq:2f7e3f3323', 'roberta.base')
        self.bpe = roberta.bpe
        self.indices = roberta.task.source_dictionary.indices

    def compute(self):
        if split not in ['train', 'valid', 'test']:
            raise ValueError(f'Unknown split: {split}')
        
        sample_cursor = self.db.articles.find({
            'split': split, 'n_images': {"$lte": 10, "$gte": 1}
        }, projection=['_id']).sort('_id', pymongo.ASCENDING)
        ids = np.array([article['_id'] for article in tqdm(sample_cursor)])
        if split == "valid":
            ids = ids[:len(ids)//6]
        elif split == "test":
            ids = ids[:len(ids)//2]
        sample_cursor.close()
        self.rs.shuffle(ids)

        

if __name__ == '__main__':
    DailyMailStatistics().compute()















