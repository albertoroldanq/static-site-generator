import os
import pathlib

from config.config import PROJECT_ROOT
from src.logger.logger import debug, error
from src.transformations.markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.transformations.markdown_to_html_node import get_heading_tag, get_heading_content, markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    debug(__name__)
    debug(
        f"Generating page from {os.path.relpath(from_path, PROJECT_ROOT)} to {os.path.relpath(dest_path, PROJECT_ROOT)} using {os.path.relpath(template_path, PROJECT_ROOT)}")

    debug("Copying markdown content")
    with open(from_path) as file:
        md_content = file.read()

    debug("Copying html template")
    with open(template_path) as file:
        template_content = file.read()

    debug("Transforming markdown to html node")
    html_node = markdown_to_html_node(md_content)

    debug("Transforming html nodes to html")
    html_content = html_node.to_html()

    debug("Extracting h1 title")
    try:
        html_title = extract_title(md_content)
    except ValueError as e:
        error(f"[{__name__}] - An error occurred when trying to extract the title from {os.path.relpath(from_path, PROJECT_ROOT)}: {str(e)}")
        raise ValueError(f"An error occurred when trying to extract the title from {os.path.relpath(from_path, PROJECT_ROOT)}: {str(e)}")

    debug("Creating html from template")
    html = template_content.replace("{{ Title }}", html_title).replace("{{ Content }}", html_content)

    debug("Creating html file " + str(os.path.relpath(dest_path, PROJECT_ROOT)))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    debug(__name__)
    debug(f"Attempting to generate pages recursively from [{os.path.relpath(dir_path_content, PROJECT_ROOT)}] to [{os.path.relpath(dest_dir_path, PROJECT_ROOT)}] using [{os.path.relpath(template_path, PROJECT_ROOT)}]")

    if not os.path.exists(dir_path_content):
        error(f"Directory not found: {os.path.relpath(dir_path_content, PROJECT_ROOT)}")
        raise ValueError(f"Directory not found: {os.path.relpath(dir_path_content, PROJECT_ROOT)}")

    if os.path.isdir(dir_path_content):
        source_entries = os.listdir(dir_path_content)
        for entry in source_entries:
            source_path = os.path.join(dir_path_content, entry)
            is_markdown = is_markdown_file(str(entry))

            if is_markdown:
                filename = os.path.splitext(os.path.basename(source_path))[0]
                dest_path = os.path.join(dest_dir_path, f"{filename}.html")
                try:
                    generate_page(source_path, template_path, dest_path)
                except ValueError as e:
                    error(f"[{__name__}] - {str(e)}")
                    raise ValueError(f"An error occurred when trying to generate page from {os.path.relpath(source_path, PROJECT_ROOT)}: {str(e)}")
            else:
                dest_path = os.path.join(dest_dir_path, entry)
                debug(f"Creating directory {os.path.relpath(dest_path, PROJECT_ROOT)}")
                os.makedirs(dest_path)
                generate_pages_recursive(source_path, template_path, dest_path)


def is_markdown_file(path):
    return pathlib.Path(path).suffix == ".md"


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            heading = block.split(" ", 1)
            tag = get_heading_tag(heading)
            if tag == "h1":
                return get_heading_content(heading)
    raise Exception("No h1 found in markdown document")
