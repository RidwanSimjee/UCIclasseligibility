import unittest
import main


class PrerequisiteTree(unittest.TestCase):
    #def test_base_case_empty_returns_true(self):
    #   self.assertTrue(main.recursive_prerequisite_breakdown('                  '))
    #    self.assertTrue(main.recursive_prerequisite_breakdown(''))
    def test_non_nested_and_structure(self):
        main.user_prereqs.clear()
        main.user_prereqs.update(('testclassone','testclasstwo'))
        self.assertTrue(main.recursive_prerequisite_breakdown({"AND": ["testclassone", "testclasstwo"]}))
    def test_multiple_courses_in_and_structure(self):
        main.user_prereqs.clear()
        main.user_prereqs.update(('testclassone', 'testclasstwo', 'testclassthree', 'testclassfour'))
        self.assertTrue(main.recursive_prerequisite_breakdown({"AND": ["testclassone", "testclasstwo", "testclassthree", "testclassfour"]}))
        self.assertFalse(main.recursive_prerequisite_breakdown({"AND": ["testclassone", "testclasstwo", "testclassthree", "testclasseight"]}))
    def test_nested_and_structure(self):
        main.user_prereqs.clear()
        self.assertFalse(main.recursive_prerequisite_breakdown({"AND": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.add('I&C SCI 61')
        self.assertFalse(main.recursive_prerequisite_breakdown({"AND": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.add('I&C SCI 33')
        self.assertFalse(main.recursive_prerequisite_breakdown({"AND": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.add('MATH 3A')
        self.assertFalse(main.recursive_prerequisite_breakdown({"AND": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.add('I&C SCI 6N')
        self.assertTrue(main.recursive_prerequisite_breakdown({"AND": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
    def test_non_nested_or_structure(self):
        main.user_prereqs.clear()
        main.user_prereqs.update(('testclassone','testclasstwo'))
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["testclassone", "testclasstwo"]}))
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["testclassone", "testclassthree"]}))
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["testclassthree", "testclasstwo"]}))
    def test_multiple_courses_in_or_structure(self):
        main.user_prereqs.clear()
        main.user_prereqs.update(('testclassone', 'testclasstwo', 'testclassthree'))
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["testclassone", "testclasstwo", "testclassthree"]}))
        self.assertFalse(main.recursive_prerequisite_breakdown({"OR": ["testclassfour", "testclasseight", "testclassten"]}))
    def test_nested_or_structure(self):
        main.user_prereqs.clear()
        self.assertFalse(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"OR": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.add("I&C SCI 6N")
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"OR": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.clear()
        main.user_prereqs.add("MATH 3A")
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"OR": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.clear()
        main.user_prereqs.add("I&C SCI 61")
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"OR": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.clear()
        main.user_prereqs.add("I&C SCI 33")
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"OR": ["MATH 3A", "I&C SCI 6N"]}]}))
    def test_nested_and_or_structure(self):
        main.user_prereqs.add("I&C SCI 33")
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.clear()
        main.user_prereqs.add("I&C SCI 61")
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.clear()
        main.user_prereqs.add("I&C SCI 6N")
        self.assertFalse(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
        main.user_prereqs.add("MATH 3A")
        self.assertTrue(main.recursive_prerequisite_breakdown({"OR": ["I&C SCI 33", "I&C SCI 61", {"AND": ["MATH 3A", "I&C SCI 6N"]}]}))
