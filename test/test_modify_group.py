from model.group import Group

def test_modify_first_group_name(app):
  app.session.login(user="admin", password="secret")
  app.group.modify_first_group(Group(groupname="Modify Group name"))
  app.group.view_groups()
  app.session.logout()

def test_modify_first_group_header(app):
  app.session.login(user="admin", password="secret")
  app.group.modify_first_group(Group(groupheader="Modify Group header"))
  app.group.view_groups()
  app.session.logout()

def test_modify_first_group_footer(app):
  app.session.login(user="admin", password="secret")
  app.group.modify_first_group(Group(groupfooter="Modify Group footer"))
  app.group.view_groups()
  app.session.logout()

