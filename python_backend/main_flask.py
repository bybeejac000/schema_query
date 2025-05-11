#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('jupyter nbconvert --to script main_flask.ipynb')


# In[5]:


import sys
path = r'C:\Users\jakeb\Downloads\Schema_Query\python_backend\library.py'
if path not in sys.path:
    sys.path.append(path)
import library


# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/question')
def query(question):
    response = library.query(question)
    return response

if __name__ == '__main__':
    app.run(debug=True)

