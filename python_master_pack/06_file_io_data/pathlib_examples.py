"""Pathlib and file utilities"""
from pathlib import Path
p = Path('06_file_io_data/subdir')
p.mkdir(parents=True, exist_ok=True)
(p / 'hello.txt').write_text('hello')
print((p / 'hello.txt').read_text())
