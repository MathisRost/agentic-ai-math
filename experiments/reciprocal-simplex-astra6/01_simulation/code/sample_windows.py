"""Exact independent restrictions of X to B(0,.45), using separation.

Not a joint simulator of several windows of the same whole-space realisation.
No band tail is dropped. The restricted law is recovered from the first
measure of its at most one intersecting sphere or correction cluster.
"""
import argparse,json,math,time
import numpy as np
from experiment import (ROOT,L,F,C,K,LAMC,LAM,Q2,T,KAPPA,ball,direction,frame,
                        q2_pairs,cylindrical,A3,J,DELTA,A2)

RWIN=.45
SEED=2026102140

def cap_points(rng,centre,radius,at_least=None):
    d=np.linalg.norm(centre)
    if d+radius<=RWIN:
        mu=-1.;axis=np.array([0.,0.,1.])
    elif d>=radius+RWIN or d<=radius-RWIN:
        return np.empty((0,3)),0.
    else:
        mu=(radius*radius+d*d-RWIN*RWIN)/(2*radius*d)
        axis=-centre/d
    area=2*np.pi*radius*radius*(1-mu)
    mean=C*L/K*np.exp(radius*radius/L**2)/(2*radius)*area
    if at_least is None:
        n=rng.poisson(mean)
    else:
        # Conditional Poisson tail by a normalised recurrence, no rejection of
        # a potentially rare count event. This only serves the labelled image.
        probs=[1.];term=1.;j=at_least
        while term>1e-16*sum(probs):
            j+=1;term*=mean/j;probs.append(term)
        probs=np.array(probs);probs/=probs.sum()
        n=at_least+rng.choice(len(probs),p=probs)
    e,f=frame(axis[None,:]);e=e[0];f=f[0]
    cost=rng.uniform(mu,1,n);phi=rng.uniform(0,2*np.pi,n)
    pts=centre+radius*(cost[:,None]*axis+np.sqrt(1-cost*cost)[:,None]*(np.cos(phi)[:,None]*e+np.sin(phi)[:,None]*f))
    assert not len(pts) or np.max(np.linalg.norm(pts,axis=1))<=RWIN+1e-12
    return pts,float(mean)

def run(n):
    started=time.time();rng=np.random.Generator(np.random.PCG64(SEED))
    component=rng.random(n)<.5 # True=Y; one coin per independent realisation.
    counts=np.zeros(n,dtype=np.int64);saved_points=[];saved_ids=[]
    latent=[]
    def save(i,p):
        counts[i]=len(p)
        if len(p):saved_points.append(p);saved_ids.append(np.full(len(p),i,dtype=np.int64))
    # gamma(R) times the centre ball B(0,R+r) is a finite envelope for
    # gamma(R) times the sphere/window intersection centre domain.
    coeff=np.array([RWIN**3,3*RWIN**2,3*RWIN,1.])
    powers=np.arange(1,5)
    integrals=np.array([.5*(L*L/4)**((p+1)/2)*math.gamma((p+1)/2) for p in powers])
    masses=8*np.pi*F/(3*L**4)*coeff*integrals
    probability=masses.sum()
    assert probability<1
    ids=np.flatnonzero(component & (rng.random(n)<probability))
    mixture=rng.choice(4,size=len(ids),p=masses/probability)
    radii=np.sqrt(rng.gamma((powers[mixture]+1)/2,L*L/4))
    centres=ball(rng,len(ids))*(radii+RWIN)[:,None]
    intersect_count=0
    for i,r,z in zip(ids,radii,centres):
        intersects=np.linalg.norm(z)>=max(0,r-RWIN)
        if intersects:
            p,mean=cap_points(rng,z,r);save(i,p);intersect_count+=1
        else:mean=0.
        latent.append([int(i),float(r),*z.tolist(),bool(intersects),mean])
    # Marked retained-centre first intensity times a containing centre ball.
    # The at-most-one-intersecting-cluster fact makes this exact locally.
    expanded_volume=4*np.pi/3*(RWIN+1)**3
    cat_mass=expanded_volume*np.array([LAMC-Q2,Q2/2,T/6,T/2])
    assert cat_mass.sum()<1 and np.min(cat_mass)>0
    ids=np.flatnonzero((~component)&(rng.random(n)<cat_mass.sum()))
    cats=rng.choice(4,len(ids),p=cat_mass/cat_mass.sum())
    centres=ball(rng,len(ids))*(RWIN+1)
    mark_counts=np.zeros(4,dtype=int)
    for i,cat,z in zip(ids,cats,centres):
        if cat==0:p=z[None,:];mark=1
        elif cat==1:
            u,_=q2_pairs(rng,1)
            _,_,rat=cylindrical(rng,u)
            d2=np.sum(u*u)
            reject=8*np.pi*A3*J*rat[0]/(DELTA+A2*(-np.expm1(-d2/(2*L*L))))
            if rng.random()<reject:p=np.empty((0,3));mark=0
            else:p=z+np.vstack((np.zeros(3),u[0]));mark=2
        else:
            u=direction(rng,1)*np.sqrt(rng.random())
            v,_,rat=cylindrical(rng,u)
            if rng.random()>=rat[0]:p=np.empty((0,3));mark=0
            elif cat==2:p=z+np.vstack((np.zeros(3),u[0],v[0]));mark=3
            else:p=z[None,:];mark=1
        mark_counts[mark]+=1
        p=p[np.linalg.norm(p,axis=1)<RWIN]
        save(i,p)
    pts=np.concatenate(saved_points) if saved_points else np.empty((0,3))
    point_ids=np.concatenate(saved_ids) if saved_ids else np.empty(0,dtype=np.int64)
    np.savez_compressed(ROOT/'data/ordinary_windows.npz',component_Y=component,counts=counts,
                        point_coordinates=pts,point_realisation_id=point_ids,
                        sphere_candidate=np.array(latent,dtype=float))
    # A separate, disclosed regular conditional illustration. Parameters are
    # fixed; this is not counted among the ordinary iid windows above.
    illustration_rng=np.random.Generator(np.random.PCG64(SEED+1))
    conditional,mean=cap_points(illustration_rng,np.array([0.,0.,2.]),2.,at_least=4)
    np.savez_compressed(ROOT/'data/conditional_sphere_illustration.npz',points=conditional,
                        centre=np.array([0.,0.,2.]),radius=np.array(2.),window_radius=np.array(RWIN))
    report={'n_independent_whole_law_windows':n,'seed':SEED,'window':'B(0,0.45)',
        'window_volume':4*np.pi/3*RWIN**3,'expected_total_points':n*LAM*4*np.pi/3*RWIN**3,
        'Y_realisations':int(component.sum()),'C_realisations':int((~component).sum()),
        'observed_total_points':int(counts.sum()),'nonempty_realisations':int(np.count_nonzero(counts)),
        'maximum_count':int(counts.max()),'count_frequency':{str(k):int(v) for k,v in zip(*np.unique(counts,return_counts=True))},
        'Y_points':int(counts[component].sum()),'C_points':int(counts[~component].sum()),
        'sphere_envelope_event_probability':float(probability),'sphere_candidates':len(radii),
        'intersecting_spheres':intersect_count,'correction_candidates':len(ids),
        'correction_mark_counts_before_window_restriction':mark_counts.tolist(),
        'conditional_illustration':{'seed':SEED+1,'sphere_centre':[0,0,2],'sphere_radius':2,
            'condition':'Given this latent sphere, condition N(B(0,.45)) >= 4.',
            'unconditioned_cap_poisson_mean':mean,'drawn_count':len(conditional),
            'not_included_in_ordinary_windows':True,'count_tail_numerical_tolerance':1e-16},
        'elapsed_seconds':time.time()-started,
        'scope':'Independent exact restrictions to the stated small ball, up to floating-point sampling. No band truncation. Not a jointly consistent multi-window realisation sampler.'}
    (ROOT/'data/ordinary_windows.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=5000000)
    run(ap.parse_args().n)
