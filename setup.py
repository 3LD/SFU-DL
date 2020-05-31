import sys
import os
from distutils.core import setup

setup(
    name='sfu_dl', 
    version='0.0.1',
    packages=['sfu_dl'],
    package_dir={'browsercookie' : '.'},
    author='3LD',
    description='Butchered youtube-dl to work with SFU media servers, and bolted on auto chrome cookie decryption',
    install_requires=['pycryptodome', 'keyring', 'lz4', 'pywin32'],
    license='lgpl'
)