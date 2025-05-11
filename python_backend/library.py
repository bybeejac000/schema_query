
def query(question, url="http://34.231.20.50:5000/question"):
    import requests
    payload = {
        "model": "mistral:7b-instruct-q4_K_M",
        "prompt": question,
        "stream": False
    }

    response = requests.post(url, json=payload)

    res = response.json().get("response")
    return res

