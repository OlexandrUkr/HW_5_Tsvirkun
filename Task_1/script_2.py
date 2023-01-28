from Task_1.script_1 import Admin as Admin, Moderator as Moderator


class NoAccess(Exception):
    pass


"""була ще така ідея
def admin_perm(func):
    def wrap(user, action, level=1, dija="delete_article"):
        if (isinstance(user, Admin) and level >= 3) or (isinstance(user, Admin) and dija == "delete_article"):
            return func(user, action)
        else:
            raise NoAccess(Exception)

    return wrap"""


def admin_perm(func):
    def wrap(user, action, level=0):
        if isinstance(user, Admin) and (level == 0 or level >= 3):
            return func(user, action)
        else:
            raise NoAccess(Exception)

    return wrap


def moderator_perm(func):
    def wrap(user, action):
        if isinstance(user, Moderator) or isinstance(user, Admin):
            return func(user, action)
        raise NoAccess(Exception)

    return wrap


@admin_perm  # для роботи цього декоратора потрібно передавати (user, action, level, dija="delete_group")
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
