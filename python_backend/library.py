
def query(question, url="http://52.204.141.248:5000/question"):
    import requests
    payload = {
        "model": "mistral:7b-instruct-q4_K_M",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=payload)

    res = response.json().get("response")
    return res

