import unittest
from unittest.mock import patch, call
import Jane_the_ripper as c
HASH_FILE = 'test_hashes.txt'
WORDLIST_FILE = 'test_wordlist.txt'

class TestPasswordCracker(unittest.TestCase):
    
    @patch('builtins.print')
    def test_01_cracking_results(self, mock_print):
        """
        Tests the core cracking logic, checking for correct cracks and failures.
        """
        c.crack_passwords(HASH_FILE, WORDLIST_FILE)
        
        printed_output = [c[0][0] for c in mock_print.call_args_list if c[0]]
       
        self.assertEqual(
            sum('[+] Cracked:' in line for line in printed_output), 
            4, 
            "Expected 4 successful cracks based on test files."
        )
        expected_crack_output = '[+] Cracked: e10adc3949ba59abbe56e057f20f883e  -->  123456'
        self.assertIn(
            expected_crack_output, 
            printed_output,
            "Must correctly report the crack for '123456'."
        )
        
        self.assertIn(
            '[!] Cracked 4 out of 6 total hashes.', 
            printed_output,
            "Final reporting of cracked vs. total hashes is incorrect."
        )
        self.assertIn(
            '[-] FAILED: 11111111111111111111111111111111', 
            printed_output,
            "Must report the specific uncrackable hash."
        )

    @patch('builtins.print')
    def test_02_file_not_found_handling(self, mock_print):
        """
        Tests that the script handles missing files gracefully and reports an error.
        """
       
        c.crack_passwords('missing_hashes.txt', WORDLIST_FILE)
        
        self.assertIn(
            'ERROR: Hash file not found at \'missing_hashes.txt\'', 
            [c[0][0] for c in mock_print.call_args_list if c[0]],
            "Should print error when hash file is missing."
        )
        mock_print.reset_mock() 

        c.crack_passwords(HASH_FILE, 'missing_wordlist.txt')
        
        self.assertIn(
            'ERROR: Wordlist file not found at \'missing_wordlist.txt\'', 
            [c[0][0] for c in mock_print.call_args_list if c[0]],
            "Should print error when wordlist file is missing."
        )


if __name__ == '__main__':
  
    unittest.main()