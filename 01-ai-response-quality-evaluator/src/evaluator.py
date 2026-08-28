import json, sys
WEIGHTS={"correctness":0.35,"relevance":0.20,"completeness":0.15,"clarity":0.10,"safety":0.20}
def weighted_score(scores):
    missing=set(WEIGHTS)-set(scores)
    if missing: raise ValueError(f"Missing rubric fields: {sorted(missing)}")
    for k in WEIGHTS:
        if not 0<=scores[k]<=5: raise ValueError(f"{k} must be between 0 and 5")
    return round(sum(scores[k]*WEIGHTS[k] for k in WEIGHTS),2)
def evaluate_case(case):
    a,b=weighted_score(case['scores_a']),weighted_score(case['scores_b'])
    return {'id':case['id'],'score_a':a,'score_b':b,'winner':'A' if a>b else 'B' if b>a else 'TIE'}
def main(path):
    cases=json.load(open(path,encoding='utf-8'))
    for c in cases:
        r=evaluate_case(c); print(f"{r['id']}: A={r['score_a']} B={r['score_b']} Winner={r['winner']}")
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python evaluator.py <cases.json>')
    main(sys.argv[1])
