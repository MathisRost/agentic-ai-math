"""Layout-only revision of the saved-configuration figure; original stays frozen."""
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'notes/matplotlib_cache'))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.size':9,'axes.labelsize':10,
                    'axes.titlesize':10,'pdf.fonttype':42,'ps.fonttype':42})
fig=plt.figure(figsize=(9,3.5))
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
    if i<2:ax.set(xlim=(-.45,.45),ylim=(-.45,.45),zlim=(-.45,.45))
    ax.set_title(title,pad=8)
    ax.set_xlabel('$x$',labelpad=-2);ax.set_ylabel('$y$',labelpad=-2);ax.set_zlabel('$z$',labelpad=-2)
    ax.tick_params(labelsize=7,pad=0);ax.set_box_aspect((1,1,1))
fig.subplots_adjust(left=.02,right=.94,bottom=.15,top=.86,wspace=.08)
for ext in ('pdf','png'):fig.savefig(ROOT/f'figures/sampled_configurations_v02.{ext}',dpi=220)
