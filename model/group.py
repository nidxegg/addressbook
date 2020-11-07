from sys import maxsize
class Group:
    def __init__(self, groupname=None, groupheader=None, groupfooter=None, id = None):
        self.groupname = groupname
        self.groupheader = groupheader
        self.groupfooter = groupfooter
        self.id = id

    def __repr__(self):
        return "%s:%s" %(self.id, self.groupname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.groupname == other.groupname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
