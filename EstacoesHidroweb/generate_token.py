import time
import secrets
import jwt

variables = {
    'client_secret': "ymr99wp7u4n7nmb92jm_",
    'client_id': "r21d4zpik9zc9_3",
    'URL_SNIRH': "https://www.snirh.gov.br",
    'URL_API': "https://www.snirh.gov.br/hidroweb/rest/api/",
    'URL_INTELGEO': "https://ows.snirh.gov.br/ords/prd11/servicos/snirh_ig/intelgeo",
    'URL_SSO_LOGIN': "https://www.snirh.gov.br/sso/login.jsf?response_type=code&client_id=r21d4zpik9zc9_3&scope=PROFILE%20PERMISSOES%20RESTRICOES&state=&redirect_uri=" + i,
    'APIKEY_TINY_MCE': "dh57ixjuqgi3ik563bo0kne156g0h8oi22fzw4wp1ylgmdkk",
    'TOKENSECRETKEY': "7f-j&CKk=coNzZc0y7_4obMP?#TfcYq%fcD0mDpenW2nc!lfGoZ|d?f&RNbDHUX6HIDROWEBBACK"
}


def gera_token():
    payload = {
        "sub": str(secrets.randbelow(1_000_000)),
        "iss": "HidroWeb-Front",
        "permissions": ["read", "write"],
        "exp": int(time.time()) + 60,
    }
    return jwt.encode(
        payload,
        variables["TOKENSECRETKEY"],
        algorithm="HS256"
    )

def get_headers():
    token = f"Bearer {gera_token()}"
    return {
        "HidroWeb-Front": token,
        "Authorization": token,
        "Content-Type": "application/x-www-form-urlencoded",
    }