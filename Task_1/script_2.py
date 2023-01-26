class NoAccess(Exception):
    pass


def admin_l3_perm(func):
    def wrap(user, action, level):
        if user == "Admin":
            if level >= 3:
                return func(user, action)
        raise NoAccess(Exception)
    return wrap


def admin_perm(func):
    def wrap(user, action):
        if user == "Admin":
            return func(user, action)
        raise NoAccess(Exception)
    return wrap


def moderator_perm(func):
    def wrap(user, action):
        if user == "Moderator" or user == "Admin":
            return func(user, action)
        raise NoAccess(Exception)
    return wrap


@admin_l3_perm  # для роботи цього декоратора потрібно передавати третій параметр - рівень андміністратора
def delete_group(user, group_id):
    print("Group has been deleted")
    return True


@admin_perm
def delete_article(user, article_id):
    print("Article has been deleted")
    return True


@moderator_perm
def create_article(user, post_data):
    print("Article has been created")
    return True


@moderator_perm
def update_article(user, update_data):
    print("Article has been updated")
    return True


def share_article(user, article_id):
    print("Article has been shared")
    return True


def set_like_to_article(user, post_data):
    print("Like has been set")
    return True
