from model.group import Group

def test_del_group(app):
  old_groups = app.group.get_group_list()
  if app.group.count() == 0:
    app.group.create_groups(Group(groupname="sdfsdываываывf", groupheader="sdfsdf",  groupfooter="sdf"))
  app.group.del_groups()
  new_groups = app.group.get_group_list()
  assert len(old_groups) - 1 == len(new_groups)
  

