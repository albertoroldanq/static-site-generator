import os

from config.config import PROJECT_ROOT
from src.logger.logger import debug
from src.transformations.markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.transformations.markdown_to_html_node import get_heading_tag, get_heading_content, markdown_to_html_node


def generate_page(from_path, template_path,dest_path):
    debug(f"Generating page from {os.path.relpath(from_path, PROJECT_ROOT)} to {os.path.relpath(dest_path, PROJECT_ROOT)} using {os.path.relpath(template_path, PROJECT_ROOT)}")

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
    html_title = extract_title(md_content)

    debug("Creating html from template")
    html = template_content.replace("{{ Title }}", html_title).replace("{{ Content }}", html_content)

    debug("Creating html file " + os.path.relpath(dest_path, PROJECT_ROOT))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(html)


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


