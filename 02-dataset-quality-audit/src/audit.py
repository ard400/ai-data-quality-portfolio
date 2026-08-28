import csv,sys,statistics
def read_csv(path):
    with open(path,newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def missing_counts(rows):
    return {} if not rows else {k:sum(1 for r in rows if str(r.get(k,'')).strip()=='') for k in rows[0]}
def duplicate_count(rows):
    seen=set(); dup=0
    for r in rows:
        key=tuple(sorted(r.items())); dup += key in seen; seen.add(key)
    return dup
def numeric_failures(rows,column):
    failures=0; values=[]
    for r in rows:
        raw=str(r.get(column,'')).strip()
        if not raw: continue
        try: values.append(float(raw))
        except ValueError: failures += 1
    return failures,values
def iqr_outliers(values):
    if len(values)<4: return []
    vals=sorted(values); mid=len(vals)//2; q1=statistics.median(vals[:mid]); q3=statistics.median(vals[(len(vals)+1)//2:]); iqr=q3-q1; lo=q1-1.5*iqr; hi=q3+1.5*iqr
    return [v for v in vals if v<lo or v>hi]
def audit(path):
    rows=read_csv(path); result={'rows':len(rows),'missing':missing_counts(rows),'duplicates':duplicate_count(rows),'numeric_checks':{}}
    for col in ['revenue_usd','employees']:
        failures,values=numeric_failures(rows,col); result['numeric_checks'][col]={'conversion_failures':failures,'outliers':iqr_outliers(values)}
    return result
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python audit.py <file.csv>')
    print(audit(sys.argv[1]))
