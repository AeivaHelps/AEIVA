#!/usr/bin/env python
# coding=utf-8
""" This module contains the base class for all trainer classes.

Copyright (C) 2023 Bang Liu - All Rights Reserved.
This source code is licensed under the license found in the LICENSE file
in the root directory of this source tree.
"""
from abc import ABC


class BaseTrainer(ABC):
    """ This class is the base class for all trainer classes.
    """
    
    def __init__(self, *args, **kwargs):
        pass

    def reset(self, *args, **kwargs):
        """ Reset the trainer.
        """
        pass

    def train(self, *args, **kwargs):
        """ Train the trainer.
        """
        pass

    def eval(self, *args, **kwargs):
        """ Evaluate the trainer.
        """
        pass

    def infer(self, *args, **kwargs):
        """ Infer the trainer.
        """
        pass
