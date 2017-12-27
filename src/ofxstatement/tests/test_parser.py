#!/usr/bin/env python3
import unittest

# from ofxstatement import plugin
from ofxstatement.plugins.unicredit import UnicreditParser

class ParserTest(unittest.TestCase):
    def test_no_stmt(self):
        """no statements make parser raise an exception, in CLI, it looks like
        the following:
        $ ofxstatement convert -t unicredit-06  ./src/ofxstatement/tests/STATEMENT_12345678_20171130_no_stmt.xml no.ofx
        Traceback (most recent call last):
          File "bin/ofxstatement", line 11, in <module>
            load_entry_point('ofxstatement', 'console_scripts', 'ofxstatement')()
          File "lib/python3.6/site-packages/ofxstatement-0.6.1-py3.6.egg/ofxstatement/tool.py", line 150, in run
          File "lib/python3.6/site-packages/ofxstatement-0.6.1-py3.6.egg/ofxstatement/tool.py", line 128, in convert
          File "lib/python3.6/site-packages/ofxstatement-0.6.1-py3.6.egg/ofxstatement/parser.py", line 23, in parse
          File "ofxstatement/plugins/unicredit.py", line 59, in split_records
            stmt = self._pick_matching_statement(stmts)
          File "ofxstatement/plugins/unicredit.py", line 35, in _pick_matching_statement
            raise Exception("No statement data in the file")
        Exception: No statement data in the file
        """
        with self.assertRaises(Exception) as no_stmt_error:
            filename = "./src/ofxstatement/tests/STATEMENT_12345678_20171130_no_stmt.xml"
            uc_parser = UnicreditParser(filename)
            uc_parser.parse()

        self.assertEqual(str(no_stmt_error.exception), "No statement data in the file")
