import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(PROJECT_ROOT, "static")
PUBLIC_DIR = os.path.join(PROJECT_ROOT, "public")
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content")
TEMPLATES_DIR = os.path.join(PROJECT_ROOT, "templates")

TEMPLATE_HTML_PATH = os.path.join(TEMPLATES_DIR, "template.html")
INDEX_MD_PATH = os.path.join(CONTENT_DIR, "index.md")
INDEX_HTML_PATH = os.path.join(PUBLIC_DIR, "index.html")

STORAGE_DIR = os.path.join(PROJECT_ROOT, 'storage')
LOGS_DIR = os.path.join(STORAGE_DIR, 'logs')