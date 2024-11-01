import math
import random

## UTILS ##

def integer_to_list(x: int) -> list[int]:
    return [int(i) for i in str(x)]

def list_to_integer(L: list[int]) -> int:
    result = ""
    for num in L:
        result += str(num);
    return (int(result))


# get a random list of length, with each element within bounds, inclusive.
def random_list(lower_bound: int, upper_bound: int, length: int) -> list[int]:
    result : list[int] = []

    for i in range(length):
        result += [random.randint(lower_bound, upper_bound)]
    return result

## UTILS ##

def secret_server_decryption():
    ### INTERNAL SERVER BEHAVIOR START #### (the attacker does not see what happens here)

    # ASSUME encryption and decryption has already occured.
    secret_message = 1234;
    # let M be the decrypted secret within the server.
    M = list_to_integer(pad(integer_to_list(secret_message), 8));

    #### INTERNAL SERVER BEHAVIOR END ####

    ## Now, server responds with some feedback which we assume gives the oracle. 
    # In reality, this might be a timing attack.

    return True;

def pad(message: list[int], total_length: int) -> int:
    padding_size: int = total_length - 4 - 2 - len(message) # take away constant 0002 and 00 markers (length 4 + 2)
    if (padding_size <= 0):
        print(f"Padding size {padding_size} too small!")
        return
    # 0002 + random + 00 + secret_unencrypted_message
    return [0,0,0,2] + random_list(1,9, padding_size) + [0,0] + message

# In setup, try random s until the oracle returns 1. Then, can start the search.
def oracle(c: int, s: int, e: int) -> bool:
    # c_prime = c(s_0^e) mod n
    c_prime = (c * math.pow(s,e)) % n

def setup():



    oracle()

    # modulus n
    n = 91 # n = pq
    # exponent e
    e = random.randint(128,256)





def main():
    pass

rand_list = random_list(1, 9, 10)
# rand_list = integer_to_list(1234)

# print(rand_list)

# print(list_to_integer(rand_list))

print(pad(integer_to_list(1234), 48))


