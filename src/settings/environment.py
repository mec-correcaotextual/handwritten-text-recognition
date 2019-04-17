"""Load the environment variables."""

import os

GT_DIR = "gt"
DA_DIR = "lines"
PR_DIR = "lines_preproc"
PA_DIR = "partitions"

TR_FILE = "train.txt"
VA_FILE = "validation.txt"
TE_FILE = "test.txt"

EXTENSION = "png"
IMG_SIZE = (800, 64)


class Environment():
    """Environment class."""

    def __init__(self, origin):
        self.origin = origin
        self.gt_dir = os.path.join(origin, GT_DIR)
        self.data_dir = os.path.join(origin, DA_DIR)
        self.preproc_dir = os.path.join(origin, PR_DIR)
        self.partitions_dir = os.path.join(origin, PA_DIR)

        self.train_file = os.path.join(self.partitions_dir, TR_FILE)
        self.validation_file = os.path.join(self.partitions_dir, VA_FILE)
        self.test_file = os.path.join(self.partitions_dir, TE_FILE)

        self.extension = EXTENSION
        self.img_size = IMG_SIZE