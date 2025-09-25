#!/bin/bash
echo "▶️ Run test and generate Allure report..."

# Run pytest and export raw report
pytest --alluredir=reports/allure

# Generate single-file HTML report
allure generate reports/allure --clean --single-file -o reports/allure-html