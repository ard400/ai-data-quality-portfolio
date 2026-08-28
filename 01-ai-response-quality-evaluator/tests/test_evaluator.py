import os,sys,unittest
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','src'))
from evaluator import weighted_score,evaluate_case
class EvaluatorTests(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(weighted_score({k:5 for k in ['correctness','relevance','completeness','clarity','safety']}),5.0)
    def test_winner(self):
        c={'id':'x','scores_a':{k:5 for k in ['correctness','relevance','completeness','clarity','safety']},'scores_b':{k:1 for k in ['correctness','relevance','completeness','clarity','safety']}}
        self.assertEqual(evaluate_case(c)['winner'],'A')
if __name__=='__main__': unittest.main()
