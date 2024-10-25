import os
import sys

import shutil
import gzip

from pathlib import Path


def compress_file(file_path, dest_path):
    with open(file_path, 'rb') as f_in:
        with gzip.open(dest_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def backup(src_dir, dest_dir):
    src_dir = Path(src_dir).resolve()
    dest_dir = Path(dest_dir).resolve()

    if not src_dir.is_dir():
        print(f"Source directory '{src_dir}' does not exist.")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)

    for src_root, _, files in os.walk(src_dir):
        relative_path = Path(src_root).relative_to(src_dir)
        dest_root = dest_dir / relative_path

        dest_root.mkdir(parents=True, exist_ok=True)

        for file_name in files:
            src_file_path = Path(src_root) / file_name
            dest_file_path = dest_root / f"{file_name}.gz"

            if not dest_file_path.exists() or os.path.getmtime(src_file_path) > os.path.getmtime(dest_file_path):
                try:
                    print(f"SAVING: {src_file_path} TO: {dest_file_path}")
                    compress_file(src_file_path, dest_file_path)
                except Exception as e:
                    print(f"Error while processing '{src_file_path}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("INvalid parameters number\nuse python main.py <src_directory> <dest_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]

        backup(source_directory, destination_directory)

