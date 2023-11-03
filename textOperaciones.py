#from fastapi import FastAPI, Request
import httpx


#http://127.0.0.1:8001/suma

data={'a': 2,"b":5}
r = httpx.post('http://localhost:8001/suma', json=data)


print("-"*20)
print("suma")
print(r)
print(r.text)

print("-"*20)
print("resta")
data={'a': 2,"b":5}
r = httpx.post('http://localhost:8002/resta', json=data)

print(r)
print(r.text)

print("-"*20)
print("multiplica")
data={'a': 2,"b":5}
r = httpx.post('http://localhost:8003/multiplica', json=data)

print(r)
print(r.text)

print("-"*20)
print("divide")
data={'a': 2,"b":5}
r = httpx.post('http://localhost:8004/divide', json=data)

print(r)
print(r.text)