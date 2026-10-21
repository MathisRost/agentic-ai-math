"""Reproducible importance sampling of the accepted v04 local factorial laws.

This is NOT a collection of iid whole-process realisations. Sphere observations
are sampled Poisson factorial tuples; correction observations are rejected
cluster marks. See ../notes/estimator_derivation.md for the measure identities.
No target reciprocal density is evaluated when generating process samples.
"""
from __future__ import annotations
import argparse, hashlib, json, math, os, platform, time
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
M = 1.0
LAM = 6e-6
RMAX = 2.0
C0 = np.pi**1.5 / (3*np.sqrt(3))
KAPPA = 1/(36*np.e*np.pi)
LAMC = min(LAM, KAPPA/2)
LAMY = 2*LAM-LAMC
K = 1e8*LAMY**3/C0**3
C = np.sqrt(C0*K**3/LAMY)
F = K**4/C**3
A2 = np.pi*K*K/(4*C)
A3 = K*np.sqrt(np.pi)/8
L = max(1., 128*np.pi**2*A3/LAMC, np.sqrt(2*np.pi*A2/LAMC))
BL = 8*np.pi*A3/L
DELTA = 2*BL
EPS = 1/(2*L)
J = 2*EPS-EPS*EPS
T = 16*np.pi**2*A3*J
Q2 = 4*np.pi*(DELTA/2 + A2*(.5 + L*L*np.expm1(-1/(2*L*L))))
AN = {2:(A2+DELTA)/2, 3:A3/2, 4:C/96}
VB = 4*np.pi/3
BINS = {2:np.array([.1,.25,.4,.55,.7,.85,1.]),
        3:np.array([.01,.03,.06,.10,.16,.24,.34,np.sqrt(3)/4]),
        4:np.array([.002,.006,.012,.025,.045,.075])}
SEEDS = {'sphere2':2026102102,'sphere3':2026102103,'sphere4':2026102104,
         'pair':2026102112,'triple':2026102113,
         'reference2':2026102122,'reference3':2026102123,'reference4':2026102124,
         'checks':2026102199}

def direction(rng, n):
    a = rng.normal(size=(n,3))
    return a/np.linalg.norm(a,axis=1)[:,None]

def frame(axis):
    helper = np.zeros_like(axis)
    helper[:,0] = 1
    near = np.abs(axis[:,0])>.8
    helper[near] = [0,1,0]
    e = np.cross(axis,helper)
    e /= np.linalg.norm(e,axis=1)[:,None]
    return e,np.cross(axis,e)

def ball(rng,n):
    return direction(rng,n)*rng.random(n)[:,None]**(1/3)

def geom(points,order):
    """Points include the anchor at zero; return simplex size and admissibility."""
    m=len(points)
    valid=np.ones(m,dtype=bool)
    for i in range(order):
        for j in range(i):
            valid &= np.sum((points[:,i]-points[:,j])**2,axis=1)<1
    if order==2:
        delta=np.linalg.norm(points[:,1],axis=1)
    elif order==3:
        delta=np.linalg.norm(np.cross(points[:,1],points[:,2]),axis=1)/2
    else:
        delta=np.abs(np.linalg.det(points[:,1:]))/6
        # Circumcentre solves rows x_i dot z = |x_i|^2/2.
        # Positive-volume bins exclude all singular matrices before solving.
        eligible=valid & (delta>=BINS[4][0])
        centres=np.zeros((m,3))
        centres[eligible]=np.linalg.solve(points[eligible,1:],
            np.sum(points[eligible,1:]**2,axis=2)[...,None]/2)[...,0]
        valid &= eligible & (np.sum(centres**2,axis=1)<=RMAX*RMAX)
    return delta,valid

def bin_index(delta,valid,order):
    ix=np.searchsorted(BINS[order],delta,side='right')-1
    ix[~valid]=-1
    ix[(ix<0)|(ix>=len(BINS[order])-1)]=-1
    return ix

def contributions(index,weight,order):
    a=np.zeros((len(index),len(BINS[order])-1))
    ok=index>=0
    a[np.flatnonzero(ok),index[ok]]=np.broadcast_to(weight,(len(index),))[ok]
    return a

def sphere_sample(rng,n,order):
    if order==2:
        radii=L*np.sqrt(-np.log(rng.random(n))/2)
    elif order==3:
        radii=np.abs(rng.normal(size=n))*L/np.sqrt(2)
    else:
        norm=1/6+np.log(2*RMAX)
        low=rng.random(n)<(1/6)/norm
        radii=np.empty(n)
        radii[low]=.5*rng.random(low.sum())**(1/6)
        radii[~low]=.5*np.exp(np.log(2*RMAX)*rng.random((~low).sum()))
    axis=direction(rng,n)
    e,f=frame(axis)
    cap_d2=np.minimum(1.,4*radii*radii)
    points=np.zeros((n,order,3))
    for i in range(1,order):
        d2=cap_d2*rng.random(n)
        axial=d2/(2*radii)
        radial=np.sqrt(np.maximum(0,d2-axial*axial))
        phi=2*np.pi*rng.random(n)
        points[:,i]=axial[:,None]*axis+radial[:,None]*(np.cos(phi)[:,None]*e+np.sin(phi)[:,None]*f)
    area=np.pi*cap_d2
    if order==2: weight=2*A2*area
    elif order==3: weight=4*np.pi*A3*area*area
    else: weight=np.full(n,np.pi**4*C/2*(1/6+np.log(2*RMAX)))
    delta,valid=geom(points,order)
    ix=bin_index(delta,valid,order)
    return points,radii,weight,ix,contributions(ix,weight,order)

def cylindrical(rng,u):
    d=np.linalg.norm(u,axis=1)
    axis=u/d[:,None]
    e,f=frame(axis)
    n=len(u)
    low=rng.random(n)<EPS/J
    rr=np.empty(n)
    rr[low]=EPS*rng.random(low.sum())
    rr[~low]=1/(1/EPS-rng.random((~low).sum())*(1/EPS-1))
    tt=rng.uniform(-1,1,n)
    phi=rng.uniform(0,2*np.pi,n)
    z=tt[:,None]*axis+rr[:,None]*(np.cos(phi)[:,None]*e+np.sin(phi)[:,None]*f)
    z2=np.sum(z*z,axis=1)
    zu2=np.sum((z-u)**2,axis=1)
    allowed=(z2<1)&(zu2<1)
    deficit=-np.expm1(-z2*zu2/(4*rr*rr*L*L))
    envelope=np.minimum(1.,EPS*EPS/(rr*rr))
    ratio=deficit/envelope
    ratio[~allowed]=0
    if np.max(ratio)>1+1e-12: raise AssertionError('triple rejection bound')
    return z,rr,ratio

def q2_pairs(rng,n):
    ds=[]
    remaining=n
    upper=DELTA+A2*(-np.expm1(-1/(2*L*L)))
    proposed=0
    while remaining:
        m=max(1024,math.ceil(remaining*1.5))
        d=np.sqrt(rng.random(m));proposed+=m
        good=rng.random(m)<(DELTA+A2*(-np.expm1(-d*d/(2*L*L))))/upper
        accepted=d[good][:remaining]
        ds.append(accepted);remaining-=len(accepted)
    d=np.concatenate(ds)
    return direction(rng,n)*d[:,None],proposed

def pair_sample(rng,n):
    u,proposed=q2_pairs(rng,n)
    aux,rr,ratio=cylindrical(rng,u)
    d=np.linalg.norm(u,axis=1)
    coeff=DELTA+A2*(-np.expm1(-d*d/(2*L*L)))
    rejection=8*np.pi*A3*J*ratio/coeff
    if rejection.max()>.5+1e-12: raise AssertionError('pair rejection bound')
    accepted=rng.random(n)>=rejection
    pts=np.stack((np.zeros_like(u),u),axis=1)
    ix=bin_index(d,accepted,2)
    return pts,aux,accepted,ix,contributions(ix,Q2,2),proposed

def triple_sample(rng,n):
    u=direction(rng,n)*np.sqrt(rng.random(n))[:,None]
    v,rr,ratio=cylindrical(rng,u)
    accepted=rng.random(n)<ratio
    pts=np.stack((np.zeros_like(u),u,v),axis=1)
    delta,valid=geom(pts,3)
    ix=bin_index(delta,valid&accepted,3)
    c3=contributions(ix,T,3)
    c2=np.zeros((n,len(BINS[2])-1))
    for edge in (u,v,v-u):
        c2+=contributions(bin_index(np.linalg.norm(edge,axis=1),accepted,2),T/3,2)
    return pts,accepted,ix,c2,c3

def meanvar(a):
    return {'mean':a.mean(axis=0).tolist(),'variance_of_mean':(a.var(axis=0,ddof=1)/len(a)).tolist(),
            'n':len(a),'nonzero_per_bin':np.count_nonzero(a,axis=0).tolist()}

def save_npz(name,**kwargs):
    np.savez_compressed(ROOT/'data'/name,**kwargs)

def process_samples(n):
    out={}
    for order in (2,3,4):
        rng=np.random.Generator(np.random.PCG64(SEEDS[f'sphere{order}']))
        points,radii,weight,ix,c=sphere_sample(rng,n,order)
        save_npz(f'sphere{order}.npz',points=points,radius=radii,weight=weight,bin_index=ix,contribution=c)
        out[f'sphere{order}']=meanvar(c)
        print(f'sphere{order}: {n} tuples, {np.count_nonzero(ix>=0)} in measured bins',flush=True)
    rng=np.random.Generator(np.random.PCG64(SEEDS['pair']))
    points,aux,accept,ix,c,proposed=pair_sample(rng,n)
    save_npz('correction_pairs.npz',points=points,auxiliary=aux,accepted=accept,bin_index=ix,contribution=c)
    out['pair']=meanvar(c);out['pair']['accepted_marks']=int(accept.sum());out['pair']['radial_proposals']=proposed
    print(f'correction pairs: {accept.sum()} accepted / {n}',flush=True)
    rng=np.random.Generator(np.random.PCG64(SEEDS['triple']))
    points,accept,ix,c2,c3=triple_sample(rng,n)
    save_npz('correction_triples.npz',points=points,accepted=accept,bin_index=ix,pair_contribution=c2,triple_contribution=c3)
    out['triple2']=meanvar(c2);out['triple3']=meanvar(c3)
    out['triple3']['accepted_marks']=int(accept.sum())
    out['triple3']['Q3_estimate']=float(T*accept.mean())
    out['triple3']['Q3_standard_error']=float(T*np.sqrt(accept.var(ddof=1)/n))
    print(f'correction triples: {accept.sum()} accepted / {n}',flush=True)
    return out

def reference_samples(n,chunk=65536):
    out={}
    for order in (2,3,4):
        rng=np.random.Generator(np.random.PCG64(SEEDS[f'reference{order}']))
        s=np.zeros((len(BINS[order])-1,5));batch=[];counts=np.zeros(len(s),dtype=np.int64)
        for first in range(0,n,chunk):
            m=min(n-first,chunk)
            pts=np.zeros((m,order,3))
            for j in range(1,order):pts[:,j]=ball(rng,m)
            delta,valid=geom(pts,order)
            ix=bin_index(delta,valid,order)
            a=contributions(ix,VB**(order-1),order)
            b=contributions(ix,VB**(order-1)/np.maximum(delta,1e-300),order)
            s[:,0]+=a.sum(axis=0);s[:,1]+=(a*a).sum(axis=0)
            s[:,2]+=b.sum(axis=0);s[:,3]+=(b*b).sum(axis=0);s[:,4]+=(a*b).sum(axis=0)
            counts+=np.count_nonzero(a,axis=0)
            batch.append(np.stack((a.sum(axis=0),b.sum(axis=0)),axis=1))
        am=s[:,0]/n;bm=s[:,2]/n
        av=(s[:,1]/n-am*am)/(n-1);bv=(s[:,3]/n-bm*bm)/(n-1)
        cov=(s[:,4]/n-am*bm)/(n-1)
        out[str(order)]={'n':n,'bin_volume':am.tolist(),'bin_volume_variance':av.tolist(),
            'inverse_simplex_integral':bm.tolist(),'inverse_simplex_variance':bv.tolist(),
            'covariance':cov.tolist(),'hits':counts.tolist()}
        save_npz(f'reference{order}_sufficient_statistics.npz',raw_sums=s,chunk_sums=np.array(batch),counts=counts,n=np.array(n))
        print(f'reference {order}: {n} independent Lebesgue proposal points',flush=True)
    return out

def assemble(proc,ref):
    rows=[]
    for order in (2,3,4):
        ym=np.array(proc[f'sphere{order}']['mean']);yv=np.array(proc[f'sphere{order}']['variance_of_mean'])
        if order==2:
            cm=np.array(proc['pair']['mean'])+np.array(proc['triple2']['mean'])
            cv=np.array(proc['pair']['variance_of_mean'])+np.array(proc['triple2']['variance_of_mean'])
        elif order==3:
            cm=np.array(proc['triple3']['mean']);cv=np.array(proc['triple3']['variance_of_mean'])
        else:cm=np.zeros_like(ym);cv=np.zeros_like(yv)
        num=(ym+cm)/2;nv=(yv+cv)/4
        r=ref[str(order)]
        vol=np.array(r['bin_volume']);vv=np.array(r['bin_volume_variance'])
        inv=np.array(r['inverse_simplex_integral']);iv=np.array(r['inverse_simplex_variance'])
        cov=np.array(r['covariance'])
        gh=num/(LAM**order*vol)
        ghv=gh*gh*(nv/num**2+vv/vol**2)
        gt=AN[order]/LAM**order*inv/vol
        gtv=(AN[order]/LAM**order)**2*(iv/vol**2+inv**2*vv/vol**4-2*inv*cov/vol**3)
        rat=num/(AN[order]*inv)
        ratv=rat**2*(nv/num**2+iv/inv**2)
        for k in range(len(vol)):
            rows.append({'order':order,'lower':float(BINS[order][k]),'upper':float(BINS[order][k+1]),
                'g_estimate':float(gh[k]),'g_standard_error':float(np.sqrt(ghv[k])),
                'g_theory_bin_average':float(gt[k]),'theory_quadrature_standard_error':float(np.sqrt(max(0,gtv[k]))),
                'ratio':float(rat[k]),'ratio_standard_error':float(np.sqrt(ratv[k])),
                'sphere_integral_estimate':float(ym[k]),'correction_integral_estimate':float(cm[k]),
                'factorial_integral_estimate':float(num[k]),'factorial_integral_standard_error':float(np.sqrt(nv[k])),
                'bin_volume':float(vol[k]),'inverse_simplex_integral':float(inv[k]),
                'correction_fraction':float(cm[k]/(ym[k]+cm[k]))})
    return rows

def checks():
    rng=np.random.Generator(np.random.PCG64(SEEDS['checks']))
    report={}
    for order in (2,3,4):
        pts,r,_,_,_=sphere_sample(rng,10000,order)
        # Recover centres from sampled directions for n=4; a generated sphere
        # has a unique circumsphere except on a probability-zero determinant set.
        if order==4:
            z=np.linalg.solve(pts[:,1:],np.sum(pts[:,1:]**2,axis=2)[...,None]/2)[...,0]
            rel=np.abs(np.linalg.norm(z,axis=1)-r)/r
            assert np.max(rel)<1e-7
            report['maximum_relative_circumradius_error']=float(np.max(rel))
        assert np.max(np.linalg.norm(pts[:,1:],axis=2))<=1+1e-12
    assert L==1 and F<=1.0000001e-4 and Q2<=LAMC/2
    assert T <= BL*2*np.pi
    assert (LAMC-Q2/2+2*T/3)<=KAPPA
    # Dyadic probability budget computed directly. The remaining tail, k>=7,
    # has exp(-4 R^2) with R>=64 and is below representable precision.
    p=[]
    for k in range(7):
        b=2.**k;lo=0 if k==0 else b/2
        rstar=np.clip(L/np.sqrt(8),lo,b)
        gam=2*F*rstar/L**4*np.exp(-4*rstar*rstar/L**2)
        p.append(2*(4*b+2)**3*gam)
    assert sum(p)<1
    report.update({'parameter_checks':'passed','sphere_probability_first_seven_bands':p,
        'sphere_probability_sum_first_seven_bands':sum(p),'probability_budget_tail_bound':1e-300,
        'Q2':Q2,'Q2_bound':LAMC/2,'envelope_mass_T':T,
        'supplementary_mark_probability_sum':(LAMC-Q2/2+2*T/3)/KAPPA})
    return report

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=524288)
    ap.add_argument('--reference-n',type=int,default=2097152)
    args=ap.parse_args();start=time.time()
    for sub in ('data','figures','notes'):(ROOT/sub).mkdir(exist_ok=True)
    validation=checks()
    proc=process_samples(args.n)
    ref=reference_samples(args.reference_n)
    rows=assemble(proc,ref)
    result={'description':'Importance sampled factorial tuples and correction marks, not iid whole-law windows',
        'parameters':{'M':M,'lambda':LAM,'lambda_C':LAMC,'lambda_Y':LAMY,'C0':C0,'K':K,'c':C,'F':F,'L':L,'A2':A2,'A3':A3,'B_L':BL,'delta':DELTA,'Q2':Q2,'T':T,'epsilon':EPS,'J':J,'kappa':KAPPA,'a2':AN[2],'a3':AN[3],'a4':AN[4],'Rmax_estimator_guard':RMAX},
        'seeds':SEEDS,'generator':'numpy.random.Generator(PCG64)',
        'environment':{'python':platform.python_version(),'numpy':np.__version__,'platform':platform.platform()},
        'sample_sizes':{'each_sphere_order':args.n,'pair_candidates':args.n,'triple_candidates':args.n,'each_reference_order':args.reference_n},
        'checks':validation,'process_statistics':proc,'reference_statistics':ref,'results':rows,
        'elapsed_seconds':time.time()-start,
        'uncertainty':'Delta-method Monte Carlo standard errors; independent random streams; no finite-sample coverage assertion. Pair contributions within one triple kept together.'}
    (ROOT/'data/results.json').write_text(json.dumps(result,indent=2))
    import csv
    with (ROOT/'data/results.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(json.dumps({'elapsed_seconds':result['elapsed_seconds'],'max_absolute_ratio_z_score':max(abs(x['ratio']-1)/x['ratio_standard_error'] for x in rows),'results':rows},indent=2))

if __name__=='__main__':main()
