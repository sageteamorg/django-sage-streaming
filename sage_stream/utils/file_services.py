import os

def file_iterator(file_name, request_index, chunk_size=8192, offset=0, length=None):
    """iterate file chunk by chunk in generator mode"""
    with open(file_name, "rb") as f:
        f.seek(offset, os.SEEK_SET)
        remaining = length
        while True:
            bytes_length = chunk_size if remaining is None else min(remaining, chunk_size)
            data = f.read(bytes_length)
            if not (data and request_index.is_current()):
                break
            if remaining:
                remaining -= len(data)
            yield data
