

def test_del_group(app):
  app.session.login(user="admin", password="secret")
  app.group.del_groups()
  app.group.view_groups()
  app.session.logout()

