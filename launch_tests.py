#!/usr/bin/python
import json
import sys
import subprocess
import unittest

__author__ = "Antonio Sanchez <asanchez@plutec.com>"

YARABIN = "../yara/yara"

"""
    Aux method to run yara from command line
"""
def command_line(yararule, binary):
    args = [YARABIN, yararule, binary]
    value, _ = subprocess.Popen(args, stdout = subprocess.PIPE).communicate()
    value = value.split('\n')
    to_ret = list()
    for i in value:
        if len(i) > 0:
            to_ret.append(i.split(' ')[0])

    return to_ret


"""
Test r2yara
"""
class TestR2Yara(unittest.TestCase):
    
    def test_lib(self):
        rule = "tests/rules/lib.yar"
        rules = ["rule_lib_s", "rule_lib_r"]
        matches = command_line(rule, "tests/bins/ls")
        total_rules = len(rules)
        for match in matches:
            if match in rules:
                total_rules -= 1


        self.assertTrue(total_rules == 0)

    def test_section_array(self):
        rule = "tests/rules/sections.yar"
        rules = ["sections"]
        matches = command_line(rule, "tests/bins/ls")
        total_rules = len(rules)
        for match in matches:
            if match in rules:
                total_rules -= 1


        self.assertTrue(total_rules == 0)

    def test_imports(self):
        rule = "tests/rules/imports.yar"        
        rules = ["rule_import_isss_1",
                 "rule_import_isss_2",
                 "rule_import_ssr",
                 "rule_import_srs",
                 "rule_import_srr",
                 "rule_import_rss",
                 "rule_import_rsr",
                 "rule_import_rrs",
                 "rule_import_rrr"]

        matches = command_line(rule, "tests/bins/ls")
        total_rules = len(rules)
        for match in matches:
            if match in rules:
                total_rules -= 1


        self.assertTrue(total_rules == 0)
    


if __name__ == '__main__':
    unittest.main()
