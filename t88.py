import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():


    not_p = []
e = []
lim = 545

def primo(num):
   if num != 1:
         t = True
         for i in range(2,num):
             if num % i == 0:
                 t = False
                 break
         return t
 
for num in range(2, lim + 1):
   test = primo(num)
   if (test):
       e.append(num)
   else:
       not_p.append(num)

print ("Números primos: ", e)


    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
