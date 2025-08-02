import bcrypt

class hashCrypt:
    def __init__(self):
        pass

    def encript(self,pas):
        
        passbytes = pas.encode('utf-8')

        # generating the salt
        salt = bcrypt.gensalt()

        # Hashing the password
        hash = bcrypt.hashpw(passbytes, salt)
        return hash

    def comparar(self,passCompara,pas):
        bpass=pas.encode('utf-8')
        passByt = passCompara.encode('utf-8')

        result = bcrypt.checkpw(password= passByt, hashed_password= bpass)
        return result