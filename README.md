# Codespeed Deployments on stefan-marr.de

This repository contains the customization and scripts for deploying codespeed
instances on stefan-marr.de.

[Codespeed](https://github.com/tobami/codespeed) is an "application to monitor and analyze the performance of your code".

Basic Setup Instructions

```bash
git clone --recurse-submodules https://github.com/smarr/codespeed-sm-deploy codespeed
cd codespeed
virtualenv --python=python3 venv
source venv/bin/activate
cd source
pip install -r requirements.txt
python setup.py install

pip install gunicorn
```

