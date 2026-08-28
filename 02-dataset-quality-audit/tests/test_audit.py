import os,sys,unittest
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','src'))
from audit import duplicate_count,missing_counts
class AuditTests(unittest.TestCase):
    def test_duplicate_count(self): self.assertEqual(duplicate_count([{'a':'1'},{'a':'1'},{'a':'2'}]),1)
    def test_missing(self): self.assertEqual(missing_counts([{'a':''},{'a':'x'}])['a'],1)
if __name__=='__main__': unittest.main()
