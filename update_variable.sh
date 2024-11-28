#!/bin/bash
cd github_projects
python3 update_variables.py
cd numismatnettools || exit 1
git add .
git commit -m "Automated update: $(date)"
git push origin master
