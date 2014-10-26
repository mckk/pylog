class Rule:
    def __init__(self, head, body):
        self.head = head
        self.body = list(body)
    def __repr__(self):
        rep = "%r :- %r" % (self.head, self.body)
        return "%s(%s)" % (self.__class__, rep)


class Predicate:
    def __init__(self, name, args):
        self.name = name
        self.args = list(args)
    def arity(self):
        return len(self.args)

