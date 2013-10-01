import unittest
from generic_mailpile import MailPileUnittest, setUp
from nose.tools import assert_equal, assert_less



def checkSearch(postinglist_kb, query):
  class TestSearch(object):
    def __init__(self):
      setUp(self)
      self.mp.set("postinglist_kb=%s" % postinglist_kb)
      self.mp.set("num_results=50")
      self.mp.set("default_order=rev-date")
      results = self.mp.search(*query)
      assert_less(float(results.as_dict()["elapsed"]), 0.2)
  return TestSearch


def test_generator():
  postinglist_kbs = [126, 62, 46, 30]
  search_queries = ['http', 'bjarni', 'ewelina', 'att:pdf', 'subject:bjarni', 'cowboy', 'unknown', 'zyxel']
  for postinglist_kb in postinglist_kbs:
    for search_query in search_queries:
      yield checkSearch(postinglist_kb, [search_query])

