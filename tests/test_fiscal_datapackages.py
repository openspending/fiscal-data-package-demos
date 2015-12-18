import os
import glob
import json
import unittest
import datapackage_validate

class TestFiscalDataPackages(unittest.TestCase):
    def test_datapackage_files_must_be_valid(self):
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file == 'datapackage.json':
                    try:
                        with open(os.path.join(root, file), 'r') as f:
                            json.load(f)
                    except ValueError as e:
                        msg = 'File "{0}" isn\'t a valid JSON.'
                        raise ValueError(msg.format(os.path.join(root, file))) from e

    def test_datapackage_files_must_be_valid_fiscal_datapackage_files(self):
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file == 'datapackage.json':
                    with open(os.path.join(root, file), 'r') as f:
                        fdp = json.load(f)
                    try:
                        datapackage_validate.validate(fdp, 'fiscal')
                    except datapackage_validate.exceptions.DataPackageValidateException as e:
                        msg = 'File "{0}" isn\'t a valid Fiscal Data Package: {1}'
                        errs = ','.join([str(err) for err in e.errors])
                        raise ValueError(msg.format(os.path.join(root, file), errs)) from e
