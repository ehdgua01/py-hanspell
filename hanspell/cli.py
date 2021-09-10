#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse

from spell_checker import check


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    args = parser.parse_args()
    result = check(args.text)
    print('\033[32m{}\033[0m'.format(result.checked))
