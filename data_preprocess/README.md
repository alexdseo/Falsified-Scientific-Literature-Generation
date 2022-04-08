*Requirements*

```python
import os
import shutil
import json
import math
import random
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# https://www.thepythoncode.com/article/extract-pdf-images-in-python
import fitz # PyMuPDF
import io
from PIL import Image

# https://github.com/joke2k/faker
from faker import Faker
fake = Faker()
```

- Numpy: `pip install numpy`
- Pandas: `pip install pandas`
- Requests: `pip install requests`
- Beautiful Soup: `pip install beautifulsoup4`
- Selenium: `python -m pip install selenium`
	- ChromeDriver: [https://chromedriver.chromium.org](https://chromedriver.chromium.org) - Download the appropriate version for your device. Make sure `chromedriver.exe` is saved to the same directory. Version in this directory is for Mac64 M1, Chrome 98.
	- webdriver-manager: `pip install webdriver-manager`
- Faker: `pip install Faker`

*Load data from `Bik_v2.tsv`. Update filepath as needed.*

*214 PDFs saved to `PDFS`.*
- USC VPN required for specific journals:
	- Wiley [119:121], Cancer [135:143], SciDirect [144:177], Science [178:180], Nature [181:187]

*Updated TSV saved as `Bik_v2_updated.tsv`.*
- Generate all features in `data_preprocess.ipynb`
	- These features will be used for LaTeX generation
- Run `discrimination/get_probs.ipynb` to import Grover discrimination feature into this Notebook (`h_probs` and `m_probs` for 214 Bik papers and 500 fake papers, respectively)