# signup_valid.py


def valid_username(user):
    if user:
        if len(user) >= 3 and len(user) <= 20:
            if " " in user:
                return False
            else:
                return True

        else:
            return False            

def valid_email(email):
    if email:
        if "@" in email:
            if " " not in email:
                if email[0: 1] != "@":
                    if len(email.split("@",1)[1]) > 2:
                        return True
                    else:
                        return False

                else:
                    return False
            else:
                return False        

        else:
            return False

def valid_password(password, verify):
    if password and verify and len(password) > 2:
        if password == verify:
            return True
        else:
            return False    
    else:
        return False

