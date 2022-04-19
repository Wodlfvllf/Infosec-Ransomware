from hashlib import sha256
MAX_NONCE = 100000000000

class Cryptom:
    def __init__(self) -> None:
        pass
    def SHA256(self,text):
        return sha256(text.encode("ascii")).hexdigest()

    def mine(self,block_number, transactions, previous_hash, prefix_zeros):
        prefix_str = '0'*prefix_zeros
        for nonce in range(MAX_NONCE):
            text = str(block_number) + transactions + previous_hash + str(nonce)
            new_hash = self.SHA256(text)
            if new_hash.startswith(prefix_str):
                print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
                return new_hash

        raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

class Crt():
    def __init__(self) -> None:
        c=Cryptom()
        transactions='''
        Dhaval->Bhavin->20,
        Mando->Cara->45
        '''
        difficulty=6 
        import time
        start = time.time()
        print("start mining")
        new_hash = c.mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
        total_time = str((time.time() - start))
        print(f"end mining. Mining took: {total_time} seconds")
        print(new_hash)