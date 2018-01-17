# Groupie-Wellman
This is an implementation of the Diffie Hellman Key Exchange Algorithm.

# How to Run?
``` 
pip install -r requirements.txt
python3 cage.py
python3 cage2.py
```

`cage.py` acts as server, `cage2.py` acts as a client.

# Diffie Hellman Algorithm
DHA is an algorithm for exchanging public keys over a public domain, the 
underlying Mathematics is pretty easy to understand, all you need to understand is modulo arithmetic.

If prime numbers came to your mind when you read this, then you are right all we need is just a `big prime numbers`.

## Understanding with an example:
Let us meet our friends Jorik and Swapnil, further referred as J and S, now
they want to exchange cryptographic keys, pretty easy print them off and share them right? The issue here is J and S live in different countries Malawi and 
Zimbabwe respectively, anyway so they need to exchange keys. That's where this algorithm comes into play.

|J|Public Domain|S|
|:---:|:---:|:---:|
|Generates a relatively big prime number `a`|Two prime numbers in the public domain `p`, `g`|Generates a relatively big prime number `b`|
|Calculates `h = p^a mod g`| | Calculates `j = p^b mod g`|
|Sends the result| `p^a mod g` & `p^b mod g` go through the public domain|Sends the result
|Calculates `j^a mod g`| | Calculates `h^b mod g`|

That's it! Pretty easy eh? If you pay attention the number that both J and S
calculate at the end is the key, `p^ab mod g`. You can try to construct the key
from the stuff that is available in the public domain, but you wouldn't be able
to owing to the fact that prime numbers are pretty hard to factorize especially 
big ones.

### Why this project exists?
We just wanted to understand the Diffie Hellman Key Exchange Algorithm, what better way to do it than writing it, we acknowledge the network we implemented is nothing close to a real one. Thanks to Jorik Schllekens for the help.
