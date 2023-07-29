#!/usr/bin/env python
# coding=utf-8
"""
This module contains the base config classes.

We can define separate config classes for different modules, e.g., data, model, trainer, etc.
They will be automatically registered in the BaseConfig class.

Copyright (C) 2023 Bang Liu - All Rights Reserved.
This source code is licensed under the license found in the LICENSE file
in the root directory of this source tree.
"""
import os
import re
import json
import yaml
import pprint


class BaseConfig:
    subclasses = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseConfig.subclasses[cls.__name__] = cls

    @classmethod
    def from_dict(cls, data: dict):
        try:
            return cls(**data)
        except TypeError as e:
            invalid_keys = [key.strip("'") for key in re.findall(r"'(\w+)'", str(e))]
            raise ValueError(f"Invalid config keys provided: {invalid_keys}. Details: {e}")

    @classmethod
    def from_json(cls, json_path: str):
        with open(json_path, "r") as json_file:
            data = json.load(json_file)
        return cls.from_dict(data)

    @classmethod
    def from_yaml(cls, yaml_path: str):
        with open(yaml_path, "r") as yaml_file:
            data = yaml.safe_load(yaml_file)
        return cls.from_dict(data)

    @classmethod
    def from_json_or_yaml(cls, file_path: str):
        _, file_extension = os.path.splitext(file_path)
        if file_extension == ".json":
            return cls.from_json(file_path)
        elif file_extension == ".yaml" or file_extension == ".yml":
            return cls.from_yaml(file_path)
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}. Please use .json or .yaml")

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    def to_json(self, filepath: str):
        with open(filepath, 'w') as json_file:
            json.dump(self.to_dict(), json_file, indent=4)

    def to_yaml(self, filepath: str):
        with open(filepath, 'w') as yaml_file:
            yaml.dump(self.to_dict(), yaml_file)

    def __str__(self):
        return pprint.pformat(self.to_dict(), indent=4)
