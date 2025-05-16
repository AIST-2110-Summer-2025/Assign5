from typing import Iterable, Pattern
import unittest
from unittest.mock import patch

import sys
from pathlib import Path
from io import StringIO

import re

class UnitTestUtils():

    def __init__(self, test_obj: unittest.TestCase, 
                       test_file: str,
                       script_file: str, 
                       relative: bool = True):
        self.test_obj = test_obj

        if relative:
            test_path = Path(test_file).parent.resolve()
            script_file_path = test_path / script_file
        else:
            script_file_path = Path(script_file)

        if not script_file_path.is_file():
            raise FileNotFoundError(f"Unable to find {script_file_path}")

        self.test_script = open(script_file_path).read()

    def check_one_equals( self,
                          inputs: Iterable[str],
                          expected_output: str,
                          ignore_case: bool = True ):

        # Redirect stdout to capture prints
        captured_output_stream = StringIO()
        sys.stdout = captured_output_stream
        
        # Execute script
        with(patch('builtins.input') as mock_input):
            mock_input.side_effect = inputs
            try:
                exec(self.test_script)
            except SystemExit:
                pass

        sys.stdout = sys.__stdout__
        
        # Get the output 
        actual_output = captured_output_stream.getvalue().strip()

        test_inputs = inputs
        test_expected_output = expected_output
        test_actual_output = actual_output
        if ignore_case:
            test_inputs = [s.lower() for s in test_inputs]
            test_expected_output = expected_output.lower()
            test_actual_output = actual_output.lower()

        friendly_inputs = '  • ' + '\n  • '.join(inputs)
        error_message = f'''
For input(s):
{friendly_inputs}
I expected:
    {expected_output}
but instead saw:
    {actual_output}
'''
        
        # Check the output
        self.test_obj.assertEqual(test_expected_output, test_actual_output, error_message)


    def check_one_regex( self,
                         inputs: Iterable[str],
                         expected_regex: Pattern[str],
                         expected_string: str ):

        # Redirect stdout to capture prints
        captured_output_stream = StringIO()
        sys.stdout = captured_output_stream
        
        # Execute script
        with(patch('builtins.input') as mock_input):
            mock_input.side_effect = inputs
            try:
                exec(self.test_script)
            except SystemExit:
                pass

        sys.stdout = sys.__stdout__
        
        # Get the output 
        actual_output = captured_output_stream.getvalue().strip()

        friendly_inputs = '  • ' + '\n  • '.join(inputs)
        error_message = f'''
For input(s):
{friendly_inputs}
I expected the output to look somethiong like:
    {expected_string}
but I saw:
    {actual_output}
'''
        
        # Check the output
        self.test_obj.assertRegex(actual_output, expected_regex, error_message)
    

    def check_one_contains( self,
                            inputs: Iterable[str],
                            expected_expression: str,
                            ignore_case: bool = True ):

        # Redirect stdout to capture prints
        captured_output_stream = StringIO()
        sys.stdout = captured_output_stream
        
        # Execute script
        with(patch('builtins.input') as mock_input):
            mock_input.side_effect = inputs
            try:
                exec(self.test_script)
            except SystemExit:
                pass

        sys.stdout = sys.__stdout__
        
        # Get the output 
        actual_output = captured_output_stream.getvalue().strip()

        if ignore_case:
            test_re = re.compile(re.escape(expected_expression), re.IGNORECASE)
        else:
            test_re = re.compile(re.escape(expected_expression))

        friendly_inputs = '  • ' + '\n  • '.join(inputs)
        error_message = f'''
For input(s):
{friendly_inputs}
I expected the output to contain:
    {expected_expression}
but I saw:
    {actual_output}
'''
        
        # Check the output
        self.test_obj.assertRegex(actual_output, test_re, error_message)
    