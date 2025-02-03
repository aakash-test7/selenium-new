import pandas as pd
import requests
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import base64
import time
import streamlit as st

st.set_page_config(layout="wide")

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=options)
    return driver
def automate_Cultivated_task(tid):
    driver = web_driver()
    driver.get("https://cegresources.icrisat.org/cicerseq/?page_id=3605")
    time.sleep(3)

    gene_id_dropdown = Select(driver.find_element(By.NAME, "select_crop"))
    gene_id_dropdown.select_by_value("cultivars")

    radio_button = driver.find_element(By.ID, "gene_snp")
    radio_button.click()

    gene_id_dropdown = Select(driver.find_element(By.NAME, "key1"))
    gene_id_dropdown.select_by_value("GeneID")

    intergenic_dropdown = Select(driver.find_element(By.NAME, "key4"))
    intergenic_dropdown.select_by_value("intergenic")

    input_field = driver.find_element(By.ID, "tmp1")
    input_field.clear()
    input_field.send_keys(tid) #Ca_00004

    search_button = driver.find_element(By.NAME, "submit")
    search_button.click()

    time.sleep(5)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    driver.quit()

    return page_source




from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

automate_Cultivated_task("Ca_00004")
clicked = st.button("Load Page Content",type="primary")
if clicked:
    with st.container(border=True):
        with st.spinner("Loading page website..."):
            content = automate_Cultivated_task("Ca_00004")
            st.write(content)