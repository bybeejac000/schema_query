#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('jupyter nbconvert --to script library.ipynb')


# In[1]:


def query(question, url="http://34.231.20.50:11434/api/generate"):
    import requests
    payload = {
        "model": "mistral:7b-instruct-q4_K_M",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=payload)

    res = response.json().get("response")
    return res

