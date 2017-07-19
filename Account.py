class Account:
    site = '';
    site_link = '';
    login = '';
    password = '';
    comments = '';

    def __init__(self,in_site, in_site_link, in_login, in_password, in_comments):
        self.site = in_site;
        self.site_link = in_site_link;
        self.login = in_login;
        self.password = in_password;
        self.comments = in_comments;

    def show_account(self):
        print (self.site);
