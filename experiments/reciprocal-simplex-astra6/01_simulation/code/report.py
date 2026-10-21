"""Regenerate figures, manuscript tables and checks from saved simulation data."""
import os,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'notes/matplotlib_cache'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from experiment import A2,AN,L,LAM,Q2,T,BINS

plt.rcParams.update({'font.family':'serif','font.size':9,'axes.labelsize':10,
    'axes.titlesize':10,'legend.fontsize':8,'pdf.fonttype':42,'ps.fonttype':42,
    'axes.spines.top':False,'axes.spines.right':False})
result=json.loads((ROOT/'data/results.json').read_text())
ordinary=json.loads((ROOT/'data/ordinary_windows.json').read_text())
rows=result['results']
fig,axs=plt.subplots(2,3,figsize=(8.1,5.1),gridspec_kw={'height_ratios':[2.2,1]},sharex='col')
labels={2:r'Distance $D$',3:r'Triangle area $A$',4:r'Tetrahedral volume $V$'}
for j,order in enumerate((2,3,4)):
    rr=[r for r in rows if r['order']==order]
    x=np.array([(r['lower']+r['upper'])/2 for r in rr])
    y=np.array([r['g_estimate'] for r in rr]);se=np.array([r['g_standard_error'] for r in rr])
    theory=np.array([r['g_theory_bin_average'] for r in rr])
    axs[0,j].errorbar(x,y,yerr=1.96*se,fmt='o',color='#167c80',ms=4,capsize=2,label='Sample estimate')
    axs[0,j].plot(x,theory,'_',color='#bf641c',ms=13,mew=1.7,label='Theory bin average')
    axs[0,j].set_yscale('log');axs[0,j].set_title(fr'Order {order}'+(r' ($R_{\rm circ}\leq2$)' if order==4 else ''))
    axs[0,j].set_ylabel(fr'$\overline{{g}}_{order}$');axs[0,j].grid(alpha=.15)
    ratio=np.array([r['ratio'] for r in rr]);rs=np.array([r['ratio_standard_error'] for r in rr])
    axs[1,j].axhline(1,color='#bf641c',lw=1)
    axs[1,j].errorbar(x,ratio,yerr=1.96*rs,fmt='o',color='#167c80',ms=3,capsize=2)
    axs[1,j].set_ylim(.92,1.055);axs[1,j].set_xlabel(labels[order]);axs[1,j].grid(alpha=.15)
    axs[1,j].set_ylabel('Estimate / theory')
axs[0,0].legend(frameon=False)
fig.tight_layout()
for ext in ('pdf','png'):fig.savefig(ROOT/f'figures/correlations.{ext}',dpi=220,bbox_inches='tight')
plt.close(fig)

fig=plt.figure(figsize=(9,3.2))
actual=np.load(ROOT/'data/ordinary_windows.npz')
cap=np.load(ROOT/'data/conditional_sphere_illustration.npz')
tr=np.load(ROOT/'data/correction_triples.npz')
tri=tr['points'][np.flatnonzero(tr['accepted'])[10]]
datasets=[actual['point_coordinates'],cap['points'],tri]
titles=['Ordinary windows (overlaid)','Conditional sphere cap','Accepted triple-cluster mark']
for i,(p,title) in enumerate(zip(datasets,titles)):
    ax=fig.add_subplot(1,3,i+1,projection='3d')
    if i==1:
        xx=np.linspace(-.43,.43,50);xx,yy=np.meshgrid(xx,xx)
        zz=2-np.sqrt(4-xx*xx-yy*yy)
        zz[xx*xx+yy*yy+zz*zz>.45**2]=np.nan
        ax.plot_surface(xx,yy,zz,color='#167c80',alpha=.18,linewidth=0)
    if i==2:
        loop=np.vstack((p,p[0]));ax.plot(*loop.T,color='#bf641c',lw=1)
    ax.scatter(*p.T,color='#167c80',s=24,depthshade=False)
    if i<2:
        ax.set(xlim=(-.45,.45),ylim=(-.45,.45),zlim=(-.45,.45))
    ax.set_title(title,pad=8);ax.set_xlabel('$x$',labelpad=-2);ax.set_ylabel('$y$',labelpad=-2);ax.set_zlabel('$z$',labelpad=-2)
    ax.tick_params(labelsize=7,pad=0);ax.set_box_aspect((1,1,1))
fig.subplots_adjust(left=.02,right=.94,bottom=.04,top=.85,wspace=.08)
for ext in ('pdf','png'):fig.savefig(ROOT/f'figures/sampled_configurations.{ext}',dpi=220)
plt.close(fig)

checks={}
rr=result['reference_statistics']['2']
lo=BINS[2][:-1];hi=BINS[2][1:]
exactvol=4*np.pi/3*(hi**3-lo**3);exactinv=2*np.pi*(hi**2-lo**2)
checks['pair_reference_volume_z'] = ((np.array(rr['bin_volume'])-exactvol)/np.sqrt(rr['bin_volume_variance'])).tolist()
checks['pair_reference_inverse_integral_z']=((np.array(rr['inverse_simplex_integral'])-exactinv)/np.sqrt(rr['inverse_simplex_variance'])).tolist()
ym=np.array(result['process_statistics']['sphere2']['mean']);yv=np.array(result['process_statistics']['sphere2']['variance_of_mean'])
expected=4*np.pi*A2*L*L*(np.exp(-lo*lo/(2*L*L))-np.exp(-hi*hi/(2*L*L)))
checks['pair_sphere_against_exact_integral_z']=((ym-expected)/np.sqrt(yv)).tolist()
pair=np.load(ROOT/'data/correction_pairs.npz')
ap=pair['accepted'].astype(float);at=tr['accepted'].astype(float)
gap=Q2*ap.mean()+T*at.mean()-Q2
se=np.sqrt(Q2*Q2*ap.var(ddof=1)/len(ap)+T*T*at.var(ddof=1)/len(at))
checks['F2_plus_Q3_equals_Q2_z']=float(gap/se)
checks['max_comparison_ratio_z']=max(abs(r['ratio']-1)/r['ratio_standard_error'] for r in rows)
checks['all_reported_process_and_reference_standard_errors_finite']=all(math.isfinite(r['g_standard_error']) and math.isfinite(r['theory_quadrature_standard_error']) for r in rows)
assert all(abs(x)<5 for key,val in checks.items() if key.endswith('_z') for x in (val if isinstance(val,list) else [val]))
(ROOT/'data/additional_checks.json').write_text(json.dumps(checks,indent=2))

def sci(v):
    e=int(np.floor(np.log10(abs(v)))) if v else 0
    return f'{v/10**e:.3f}\\times10^{{{e}}}'
lines=[r'\begin{table}[htbp]',r'\centering\small',r'\caption{Bin-averaged normalised correlations. The ratio column gives one Monte Carlo standard error in parentheses; the full-precision CSV also reports the separate error of the reference integration. Every bin has diameter below 1. At order four we additionally require $R_{\rm circ}\leq2$.}',r'\label{tab:simulation-results}',r'\begin{tabular}{ccrrr}',r'\toprule',r'Order & Simplex bin & Estimate & Theory bin average & Ratio (SE)\\',r'\midrule']
for order in (2,3,4):
    selected=[r for r in rows if r['order']==order]
    # Three representative rows per order keep the paper table compact; all
    # bins and separate errors appear in the machine-readable supplement.
    for k in [0,len(selected)//2,len(selected)-1]:
        r=selected[k]
        interval=f"[{r['lower']:.3g}, {r['upper']:.3g})"
        lines.append(f"{order} & ${interval}$ & ${sci(r['g_estimate'])}$ & ${sci(r['g_theory_bin_average'])}$ & ${r['ratio']:.4f}\\;({r['ratio_standard_error']:.4f})$\\\\")
lines += [r'\bottomrule',r'\end{tabular}',r'\end{table}']
(ROOT/'results_table.tex').write_text('\n'.join(lines)+'\n')
print(json.dumps({'figures':['correlations.pdf','correlations.png','sampled_configurations.pdf','sampled_configurations.png'],'checks':checks},indent=2))
