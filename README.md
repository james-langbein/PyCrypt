## PyCrypt

A side-project experimenting with encryption.  

It uses a shared private key, hence a secure back-channel is required for communication of the key, but that is currently outside the scope of this project.

As far as I can see, this algorithm is reasonably secure, provided the key is long enough.

Also, this algorithm is blazingly fast, completing encryption and decryption in a few micro-seconds.

### Encryption
 1. Split the string into random length parts, delimited by sets of 5 spaces.
 2. Variation on ROT, changing 'space' characters as well.
 3. One-time pseudo-random pad which is cryptographically secure, and not reliant on a human-given seed. A delimiter of pseudo-random characters is placed in between the string and the pad, using a given seed.
 4. Variation on ROT.
 5. Shuffle the string.
 6. A pseudo-random number of rounds, repeating steps 4 and 5. Also not reliant on a human-given seed.

### Decryption
Reverse of the above.  
The number of rounds in encryption does not need to be known.


**Read through the code for more details.**
