#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile


class CmakesanitizersConan(ConanFile):
    name        = 'cmake_sanitizers'
    version     = '1.0'
    license     = 'MIT'
    url         = 'https://github.com/kheaactua/cmake-sanitizers'
    description = 'Import CMake find scripts to load compiler sanitizers'

    def source(self):
        self.run('git clone https://github.com/arsenm/sanitizers-cmake.git')

    def package(self):
        self.copy(pattern='*', src=os.path.join('sanitizers-cmake', 'cmake'))

    def package_info(self):
        self.env_info.CMAKE_SANITIZERS_PATH = self.package_folder

# vim: ts=4 sw=4 expandtab ffs=unix ft=python foldmethod=marker :
