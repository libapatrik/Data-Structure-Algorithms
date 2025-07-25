class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for q in group.get_groups():
        if is_user_in_group(user, q):
            return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent_user = "parent_user"
parent.add_user(parent_user)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child) # child has sub_child
parent.add_group(child) # parent has child

# Test cases:
# Test of parent
# Expected True & pass;
print(is_user_in_group(sub_child_user, parent))
print('pass' if is_user_in_group(sub_child_user, parent) == True else "fail")

# Test of child
# Expected True & pass;
print(is_user_in_group(sub_child_user, child))
print('pass' if is_user_in_group(sub_child_user, child) == True else "fail")

# Test of extreme
# Expected False & fail;
print(is_user_in_group("macho_user", parent))
print('pass' if is_user_in_group("macho_user", parent) == True else "fail")
