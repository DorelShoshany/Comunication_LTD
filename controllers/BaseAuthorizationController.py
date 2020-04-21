import time
from abc import ABC, abstractmethod

from services import UserTokenEncryptinoService


class BaseAuthorizationController():
    def __init__(self, value):
        self.value = value
        super().__init__()
'''

    @abstractmethod
    def extract_valid_token_user_id(self, token):
        try:
             tokenData = UserTokenEncryptinoService.Decrypt(token)
            if time.time() - tokenData.date > TOKEN_VALIDATIONT_TIMESPAN_CONST :
                return Unauthorizsd() # AKA 401
            else:
                return tokenData.userId

        except IOError:
            return Unauthorizsd()

'''

