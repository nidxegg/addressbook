from model.group import Group

def test_del_group(app):
  if app.group.count() == 0:
    app.group.create_groups(Group(groupname="sdfsdываываывf", groupheader="sdfsdf",  groupfooter="sdf"))
  app.group.del_groups()
  

