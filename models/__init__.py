#!/usr/bin/python3
"""This initializes the package"""
from engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
