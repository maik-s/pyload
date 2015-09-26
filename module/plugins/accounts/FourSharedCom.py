# -*- coding: utf-8 -*-

from module.plugins.internal.Account import Account
from module.plugins.internal.Plugin import set_cookie


class FourSharedCom(Account):
    __name__    = "FourSharedCom"
    __type__    = "account"
    __version__ = "0.08"
    __status__  = "testing"

    __description__ = """FourShared.com account plugin"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz"),
                       ("stickell", "l.stickell@yahoo.it")]


    def grab_info(self, user, password, data, req):
        #: Free mode only for now
        return {'premium': False}


    def login(self, user, password, data, req):
        set_cookie(req.cj, "4shared.com", "4langcookie", "en")

        res = self.load("https://www.4shared.com/web/login",
                        post={'login'    : user,
                              'password' : password,
                              'remember' : "on",
                              '_remember': "on",
                              'returnTo' : "http://www.4shared.com/account/home.jsp"})

        if 'Please log in to access your 4shared account' in res:
            self.fail_login()
