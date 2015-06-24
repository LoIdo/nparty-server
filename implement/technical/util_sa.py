"""
utils for SQLAlchemy
"""

import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import sqlalchemy.sql

""" dictionary to store table declarative_base """
_base_table = {}


def declarative_base(name):
    try:
        ''' return existing declarative_base '''
        return _base_table[name]
    except KeyError:
        ''' create new if not found '''
        t = sqlalchemy.ext.declarative.declarative_base()
        _base_table[name] = t
        return t


class SearchList(object):
    """
    define custom search list
    """
    class Iter(object):

        def __init__(self, origin, session):
            self.origin = origin
            self.session = session

        def __next__(self):
            s = next(self.origin)
            if self.session:
                s.session = self.session
            return s

        def next(self):
            s = next(self.origin)
            if self.session:
                s.session = self.session
            return s

    def __init__(self, query_list, query_num, session=None):
        self.items = query_list
        self.count = query_num
        self.session = session

    def __iter__(self):
        if not isinstance(self.items, list):
            self.items = self.items.all()
        return SearchList.Iter(
            iter(self.items), self.session)

    def __len__(self):
        if not isinstance(self.items, list):
            self.items = self.items.all()
        return len(self.items)

    def count_total(self):
        if not isinstance(self.count, int):
            self.count = self.count.scalar()
        return self.count