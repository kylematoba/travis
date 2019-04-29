import random
import os
from typing import Dict


def get_paths() -> Dict[str, str]:
    tilde = os.path.expanduser('~')
    # work = os.path.join(tilde, 'Documents', 'work')
    work = os.path.join(tilde, 'work')
    paths = {
        'work': work
    }
    return paths


def get_random_hash() -> str:
    random_bits = random.getrandbits(256)
    random_hash = "%032x" % random_bits
    return random_hash


def get_tmp_work_dir() -> str:
    paths = get_paths()
    work_dir = paths['work']
    tmp_work_dir = os.path.join(work_dir, get_random_hash())
    os.makedirs(tmp_work_dir, exist_ok=True)
    return tmp_work_dir


def get_dated_dir() -> str:
    dated_dir = ''
    return dated_dir


if __name__ == "__main__":
    tmp_work_dir = get_tmp_work_dir()
