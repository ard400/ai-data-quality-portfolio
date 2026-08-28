import csv,sys,statistics,math
def load(path):
    with open(path,newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
    for r in rows:
        r['year']=int(r['year'])
        for c in ['gdp_growth_pct','inflation_pct','policy_rate_pct']: r[c]=float(r[c])
    return rows
def corr(xs,ys):
    mx,my=statistics.mean(xs),statistics.mean(ys); num=sum((x-mx)*(y-my) for x,y in zip(xs,ys)); den=math.sqrt(sum((x-mx)**2 for x in xs)*sum((y-my)**2 for y in ys)); return num/den if den else float('nan')
def analyze(rows):
    g=[r['gdp_growth_pct'] for r in rows]; i=[r['inflation_pct'] for r in rows]; p=[r['policy_rate_pct'] for r in rows]; avg=statistics.mean(g); dev=sorted(rows,key=lambda r:abs(r['gdp_growth_pct']-avg),reverse=True)[:2]
    return {'avg_growth':round(avg,2),'avg_inflation':round(statistics.mean(i),2),'inflation_rate_corr':round(corr(i,p),3),'largest_growth_deviations':[(r['year'],r['gdp_growth_pct']) for r in dev]}
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python analyze.py <file.csv>')
    print(analyze(load(sys.argv[1])))
