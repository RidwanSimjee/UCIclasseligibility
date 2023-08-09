import unittest
import main

class PrerequisiteTree(unittest.TestCase):
    def test_base_case_empty_returns_true(self):
        self.assertTrue(main.recursive_prerequisite_breakdown('                  '))
        self.assertTrue(main.recursive_prerequisite_breakdown(''))
    def test_non_nested_and_structure(self):
        main.prereq_set.update(('testclassone','testclasstwo'))
        self.assertTrue(main.recursive_prerequisite_breakdown('{"AND": ["testclassone", "testclasstwo"]}'))
    def test_non_nested_or_structure(self):
        main.prereq_set.update(('testclassone','testclasstwo'))
        self.assertTrue(main.recursive_prerequisite_breakdown('{"OR": ["testclassone", "testclasstwo"]}'))
        self.assertTrue(main.recursive_prerequisite_breakdown('{"OR": ["testclassone", "testclassthree"]}'))
        self.assertTrue(main.recursive_prerequisite_breakdown('{"OR": ["testclassthree", "testclasstwo"]}'))


