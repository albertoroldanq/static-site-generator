import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(PROJECT_ROOT, "static")
PUBLIC_DIR = os.path.join(PROJECT_ROOT, "public")

STORAGE_DIR = os.path.join(PROJECT_ROOT, 'storage')
LOGS_DIR = os.path.join(STORAGE_DIR, 'logs')