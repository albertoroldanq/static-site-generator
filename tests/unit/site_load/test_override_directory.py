import os
import shutil
import tempfile
import unittest

from src.site_load.override_directory import override_directory
from tests.TestCase import TestCase


class TestOverrideDirectory(TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.source_dir = os.path.join(self.test_dir, "static")
        self.destination_dir = os.path.join(self.test_dir, "public")

        os.mkdir(self.source_dir)
        os.mkdir(os.path.join(self.source_dir, "images"))

        with open(os.path.join(self.source_dir, "test.css"), "w") as f:
            f.write("test content")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_override_directory(self):
        override_directory(self.source_dir, self.destination_dir)

        self.assertTrue(os.path.exists(os.path.join(self.destination_dir, "test.css")))
        self.assertTrue(os.path.isdir(os.path.join(self.destination_dir, "images")))

    def test_nested_directory_copy(self):
        nested_dir = os.path.join(self.source_dir, "images")

        test_file = os.path.join(nested_dir, "test.png")
        with open(test_file, "w") as f:
            f.write("test png content")

        override_directory(self.source_dir, self.destination_dir)

        self.assertTrue(os.path.exists(os.path.join(self.destination_dir, "images", "test.png")))

    def test_empty_directory_copy(self):
        empty_dir = os.path.join(self.source_dir, "empty")
        os.mkdir(empty_dir)

        override_directory(self.source_dir, self.destination_dir)

        self.assertTrue(os.path.exists(os.path.join(self.destination_dir, empty_dir)))

    def test_source_directory_not_found(self):
        non_existent_dir = os.path.join(self.source_dir, "non_existent")

        with self.assertRaises(ValueError) as context:
            override_directory(non_existent_dir, self.destination_dir)
            self.assertIn("Directory not found", str(context.exception))


if __name__ == "__main__":
    unittest.main()
