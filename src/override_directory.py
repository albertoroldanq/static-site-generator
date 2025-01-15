import os
import shutil

from config.config import PROJECT_ROOT
from src.logger.logger import debug, error


def override_directory(source_dir, destination_dir):

    dest_rel = os.path.relpath(destination_dir, PROJECT_ROOT)

    if not os.path.exists(source_dir):
        error("Directory not found: " + source_dir)
        raise ValueError("Directory not found: " + source_dir)

    debug(f"Overriding /{dest_rel} directory in process...")

    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
        debug(f"Directory successfully DELETED: /{dest_rel}")

    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)
        debug(f"Directory successfully CREATED: /{dest_rel}")

    __copy_from_source_to_destination_directory(source_dir, destination_dir)


def __copy_from_source_to_destination_directory(source_dir, destination_dir):
    source_rel = os.path.relpath(source_dir, PROJECT_ROOT)
    dest_rel = os.path.relpath(destination_dir, PROJECT_ROOT)

    source_entries = os.listdir(source_dir)

    debug(f"Attempting to clone /{source_rel} content into /{dest_rel}")
    for entry in source_entries:
        source_path = os.path.join(source_dir, entry)
        source_path_rel = os.path.relpath(source_path, PROJECT_ROOT)
        dest_path = os.path.join(destination_dir, entry)
        dest_path_rel = os.path.relpath(dest_path, PROJECT_ROOT)

        if os.path.isfile(source_path):
            debug(f"Copying file: {source_path_rel}")
            shutil.copy(source_path, dest_path)
            debug(f"File successfully COPIED: from {source_path_rel} to {dest_path_rel}")
        else:
            os.mkdir(dest_path)
            debug(f"Directory successfully CREATED: {dest_path_rel}")
            __copy_from_source_to_destination_directory(source_path, dest_path)


