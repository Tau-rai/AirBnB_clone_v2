import unittest
from console import HBNBCommand
from models.user import User
from models import storage
from io import StringIO
import sys

class TestCreate(unittest.TestCase):
    def setUp(self):
        self.cli = HBNBCommand()

    def test_create_no_args(self):
        capturedOutput = StringIO()          
        sys.stdout = capturedOutput
        self.cli.onecmd("create")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(),\
                          "** class name missing **")

    def test_create_invalid_class(self):
        capturedOutput = StringIO()          
        sys.stdout = capturedOutput
        self.cli.onecmd("create InvalidClass")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(),\
                          "** class doesn't exist **")
    def test_create_valid_class_no_attrs(self):
        self.cli.onecmd("create User")
        self.assertTrue(isinstance(list(storage.all().values())[-1], User))

    def test_create_valid_class_with_attrs(self):
        self.cli.onecmd('create User first_name="test" last_name="One"')
        obj = list(storage.all().values())[-1]
        self.assertTrue(isinstance(obj, User))
        self.assertEqual(obj.first_name, "test")
        self.assertEqual(obj.last_name, "One")

if __name__ == "__main__":
    unittest.main()
