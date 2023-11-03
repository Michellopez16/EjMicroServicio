from fastapi import FastAPI, Request
import httpx

#http://127.0.0.1:8001/suma
data={'a': 2,"b":5}
r = httpx.post('http://localhost:8000/suma', json=data)
r.read()

print("-"*20)
print("suma")
print(r)
print(r.text)


