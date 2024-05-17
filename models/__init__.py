#!/usr/bin/python3
"""Instatiate an object storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
