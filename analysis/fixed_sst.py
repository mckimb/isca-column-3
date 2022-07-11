import numpy as np
import xarray as xr

# plotting modules
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import LogFormatter 
from faceted import faceted as fc
from scipy.integrate import trapz,simps,cumtrapz
import trop_funcs as tf
import trop_constants as tc
import pretty_plotting_funcs as ppf
import warnings
warnings.filterwarnings('ignore')

mpl.rcParams['xtick.color'] = 'k'
mpl.rcParams['ytick.color'] = 'k'
mpl.rcParams['text.usetex'] = True
mpl.rc('font',**{'family':'serif','serif':['Palatino']})
mpl.rcParams['figure.dpi']= 300

location = '/scratch/bam218/isca_data/'

# h2o LW only, fixed sst
sst170 = xr.open_dataset(location+'col_exp_LW_h2o_co2_170.0K_PIx0_take1/run0050/atmos_monthly.nc')
sst190 = xr.open_dataset(location+'col_exp_LW_h2o_co2_190.0K_PIx0_take1/run0050/atmos_monthly.nc')
sst210 = xr.open_dataset(location+'col_exp_LW_h2o_co2_210.0K_PIx0_take1/run0050/atmos_monthly.nc')
sst230 = xr.open_dataset(location+'col_exp_LW_h2o_co2_230.0K_PIx0_take1/run0050/atmos_monthly.nc')
sst250 = xr.open_dataset(location+'col_exp_LW_h2o_co2_250.0K_PIx0_take1/run0050/atmos_monthly.nc')
sst270 = xr.open_dataset(location+'col_exp_LW_h2o_co2_270.0K_PIx0_take1/run0050/atmos_monthly.nc')
sst290 = xr.open_dataset(location+'col_exp_LW_h2o_co2_290.0K_PIx0_take1/run0050/atmos_monthly.nc')
sst310 = xr.open_dataset(location+'col_exp_LW_h2o_co2_310.0K_PIx0_take1/run0050/atmos_monthly.nc')
sst330 = xr.open_dataset(location+'col_exp_LW_h2o_co2_330.0K_PIx0_take1/run0050/atmos_monthly.nc')
data_adj = [sst170, sst190, sst210, sst230, sst250, sst270, sst290, sst310, sst330]

# h2o LW only, fixed sst, no stratospheric adjustment
sst170 = xr.open_dataset(location+'col_exp_LW_h2o_co2_170.0K_PIx0_take2/run0050/atmos_monthly.nc')
sst190 = xr.open_dataset(location+'col_exp_LW_h2o_co2_190.0K_PIx0_take2/run0050/atmos_monthly.nc')
sst210 = xr.open_dataset(location+'col_exp_LW_h2o_co2_210.0K_PIx0_take2/run0050/atmos_monthly.nc')
sst230 = xr.open_dataset(location+'col_exp_LW_h2o_co2_230.0K_PIx0_take2/run0050/atmos_monthly.nc')
sst250 = xr.open_dataset(location+'col_exp_LW_h2o_co2_250.0K_PIx0_take2/run0050/atmos_monthly.nc')
sst270 = xr.open_dataset(location+'col_exp_LW_h2o_co2_270.0K_PIx0_take2/run0050/atmos_monthly.nc')
sst290 = xr.open_dataset(location+'col_exp_LW_h2o_co2_290.0K_PIx0_take2/run0050/atmos_monthly.nc')
sst310 = xr.open_dataset(location+'col_exp_LW_h2o_co2_310.0K_PIx0_take2/run0050/atmos_monthly.nc')
sst330 = xr.open_dataset(location+'col_exp_LW_h2o_co2_330.0K_PIx0_take2/run0050/atmos_monthly.nc')
data = [sst170, sst190, sst210, sst230, sst250, sst270, sst290, sst310, sst330]

# h2o+co2 LW+sw fixed sst, no stratospheric adjustment
sst170 = xr.open_dataset(location+'col_exp_LW_h2o_co2_170.0K_PIx1_take1/run0010/atmos_monthly.nc')
sst190 = xr.open_dataset(location+'col_exp_LW_h2o_co2_190.0K_PIx1_take1/run0010/atmos_monthly.nc')
sst210 = xr.open_dataset(location+'col_exp_LW_h2o_co2_210.0K_PIx1_take1/run0010/atmos_monthly.nc')
sst230 = xr.open_dataset(location+'col_exp_LW_h2o_co2_230.0K_PIx1_take1/run0010/atmos_monthly.nc')
sst250 = xr.open_dataset(location+'col_exp_LW_h2o_co2_250.0K_PIx1_take1/run0010/atmos_monthly.nc')
sst270 = xr.open_dataset(location+'col_exp_LW_h2o_co2_270.0K_PIx1_take1/run0010/atmos_monthly.nc')
sst290 = xr.open_dataset(location+'col_exp_LW_h2o_co2_290.0K_PIx1_take1/run0010/atmos_monthly.nc')
sst310 = xr.open_dataset(location+'col_exp_LW_h2o_co2_310.0K_PIx1_take1/run0010/atmos_monthly.nc')
sst330 = xr.open_dataset(location+'col_exp_LW_h2o_co2_330.0K_PIx1_take1/run0010/atmos_monthly.nc')
data_adj = [sst170, sst190, sst210, sst230, sst250, sst270, sst290, sst310, sst330]

# h2o+co2 LW+sw fixed sst, no stratospheric adjustment
sst170 = xr.open_dataset(location+'col_exp_LW_h2o_co2_170.0K_PIx1_take2/run0010/atmos_monthly.nc')
sst190 = xr.open_dataset(location+'col_exp_LW_h2o_co2_190.0K_PIx1_take2/run0010/atmos_monthly.nc')
sst210 = xr.open_dataset(location+'col_exp_LW_h2o_co2_210.0K_PIx1_take2/run0010/atmos_monthly.nc')
sst230 = xr.open_dataset(location+'col_exp_LW_h2o_co2_230.0K_PIx1_take2/run0010/atmos_monthly.nc')
sst250 = xr.open_dataset(location+'col_exp_LW_h2o_co2_250.0K_PIx1_take2/run0010/atmos_monthly.nc')
sst270 = xr.open_dataset(location+'col_exp_LW_h2o_co2_270.0K_PIx1_take2/run0010/atmos_monthly.nc')
sst290 = xr.open_dataset(location+'col_exp_LW_h2o_co2_290.0K_PIx1_take2/run0010/atmos_monthly.nc')
sst310 = xr.open_dataset(location+'col_exp_LW_h2o_co2_310.0K_PIx1_take2/run0010/atmos_monthly.nc')
sst330 = xr.open_dataset(location+'col_exp_LW_h2o_co2_330.0K_PIx1_take2/run0010/atmos_monthly.nc')
data = [sst170, sst190, sst210, sst230, sst250, sst270, sst290, sst310, sst330]

aspect=1

str_sst = str(170.)
take_num = 1
length = 10
co2 = 1
times = np.linspace(1,length,length)
tsurf, ttp = (np.zeros_like(times), np.zeros_like(times))

count=0
for time in times:
        str_time = str(int(time)).zfill(2)
        input_data = xr.open_dataset(location+'col_exp_LW_h2o_co2_'+str_sst+'K_PIx'+str(co2)+'_take'+str(take_num)+'/run00'+str_time+'/atmos_monthly.nc')
        tsurf[count] = tf.Ts(input_data)
        ttp[count] = tf.Ttp_conv(input_data, threshold=0)
        count+=1

#####################################################################
################## SURFACE TEMPERATURE TIMESCALE ####################
#####################################################################
fig, axes = fc(1, 1, width=2, aspect=aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=0, xmax=50, ymin=150, ymax=350, xlabel=r'Time (years)', ylabel=r'$T_s$ (K)')
ax.set_xticks([0,10,20,30,40,50])
ax.set_xticklabels(['0','10','20', '30', '40', '50'])
fig.text(0.5, 0.75, r'$T_s$ = '+str_sst+' K', color='k', fontsize='small')
ax.scatter(times,tsurf, s=1, color='k')

#####################################################################
################## TROPOPAUSE TEMPERATURE TIMESCALE #################
#####################################################################
fig, axes = fc(1, 1, width=2, aspect=aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=0, xmax=50, ymin=120, ymax=220, xlabel=r'Time (years)', ylabel=r'$T_{tp}$ (K)')
ax.set_xticks([0,10,20,30,40,50])
ax.set_xticklabels(['0','10','20', '30', '40', '50'])
fig.text(0.5, 0.75, r'$T_s$ = '+str_sst+' K', color='k', fontsize='small')
ax.scatter(times,ttp, s=1, color='k')
# ax.axhline(y=140, color='silver', linestyle='dashed', linewidth=0.5)


rad_threshold=0.0
conv_threshold=0.0
aspect=1
width=2
# color=cm.Greys(count/(len(data)+1)) # monochrome

#####################################################################
################## VERTICAL SPECIFIC HUMIDITY #######################
#####################################################################
fig, axes = fc(1, 1, width=width, aspect=aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=1e-11, xmax=1e-1, ymin=1000, ymax=1, xscalelog=True, yscalelog=True, 
                 xlabel=r'$q_v$', ylabel=r'$p$ (hPa)')
ax.set_xticks([1e-11, 1e-9,1e-7,1e-5,1e-3,1e-1])

count = 0
for exp in data:
    count+=1
    ax.plot(exp.sphum.mean(('lat','lon','time')), exp.pfull,color=cm.coolwarm(0.5-(count/(len(data)+1))/2), linewidth=1)
    ax.plot(exp.sphum.mean(('lat','lon','time'))/exp.rh.mean(('lat','lon','time'))*100, exp.pfull, 
            color=cm.coolwarm(0.5-(count/(len(data)+1))/2), linestyle='dashed',linewidth=0.5)
    ax.scatter(exp.sphum.mean(('lat','lon','time')).sel(pfull=tf.Ptp_conv(exp, threshold=conv_threshold),method='nearest').values, 
               tf.Ptp_conv(exp,threshold=conv_threshold), color=cm.coolwarm(0.5-(count/(len(data)+1))/2), s=4, zorder=10)
       
#####################################################################
################## VERTICAL RELATIVE HUMIDITY #######################
#####################################################################
fig, axes = fc(1, 1, width=width, aspect=aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=0, xmax=101, ymin=1000, ymax=1, yscalelog=True, xlabel=r'RH', ylabel=r'$p$ (hPa)')
ax.set_xticks([0, 20, 40, 60, 80, 100])
ax.axvline(x=70, color='silver', linewidth=0.5, linestyle='dashed')
ax.axvline(x=100, color='silver', linewidth=0.5, linestyle='dashed')    

count=0
for exp in data:
    count+=1
    ax.plot(exp.rh.mean(('lat','lon','time')), exp.pfull, linewidth=1, color=cm.coolwarm(0.5-(count/(len(data)+1))/2))
    ax.scatter(exp.rh.mean(('lat','lon','time')).sel(pfull=tf.Ptp_conv(exp, threshold=conv_threshold),method='nearest').values, 
               tf.Ptp_conv(exp, threshold=conv_threshold), color=cm.coolwarm(0.5-(count/(len(data)+1))/2), s=4, zorder=10)
    
#####################################################################
##################### VERTICAL TEMPERATURE ##########################
#####################################################################
fig, axes = fc(1, 1, width=width, aspect=aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=100, xmax=350, ymin=1000, ymax=1, yscalelog=True, xlabel=r'T (K)', ylabel=r'$p$ (hPa)')
ax.set_xticks([100,120,140, 160, 180, 200, 220, 240, 260, 280, 300, 320,340])
ax.set_xticklabels(['100','','140', '', '180', '', '220', '', '260', '', '300', '', '340'])

count = 0
for exp in data:
    count+=1
    ax.plot(exp.temp.mean(('lat','lon','time')), exp.pfull,color=cm.coolwarm(0.5-(count/(len(data)+1))/2), linewidth=1)
    ax.scatter(tf.Ttp_conv(exp, threshold=conv_threshold), tf.Ptp_conv(exp, threshold=conv_threshold), 
               color=cm.coolwarm(0.5-(count/(len(data)+1))/2), s=4, zorder=10)
    ax.scatter(tf.Ts(exp), exp.pfull.values[-1], color=cm.coolwarm(0.5-(count/(len(data)+1))/2), s=4)
    
#####################################################################
##################### VERTICAL LAPSE RATE ###########################
#####################################################################
fig, axes = fc(1, 1, width=width, aspect=aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=-1, xmax=11, ymin=1000, ymax=1, yscalelog=True, xlabel=r'$\Gamma$ (K/km)', ylabel=r'$p$ (hPa)')
ax.axvline(x=0, color='silver', linewidth=0.5, linestyle='dashed')

count = 0
for exp in data:
    count+=1
    gamma = (exp.temp.differentiate('pfull')*exp.pfull/exp.temp).mean(('lat','lon','time'))*tc.g/tc.Rd*1000
    ax.plot(gamma, exp.pfull,color=cm.coolwarm(0.5-(count/(len(data)+1))/2), linewidth=1)
    ax.scatter(gamma.sel(pfull=tf.Ptp_conv(exp, threshold=conv_threshold),method='nearest').values, 
               tf.Ptp_conv(exp, threshold=conv_threshold), color=cm.coolwarm(0.5-(count/(len(data)+1))/2), s=4, zorder=10)
    
#####################################################################    
########## TROPOPAUSE TEMPERATURE ###################################    
#####################################################################
fig, axes = fc(1, 1, width=width, aspect=1/aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=160, xmax=350, ymin=200, ymax=140,xlabel=r'$T_s$ (K)',ylabel=r'$T_{tp}$ (K)')
ax.set_xticks([160,180,200,220, 240, 260, 280, 300, 320, 340])
ax.set_xticklabels(['','180','','220', '', '260', '', '300', '','340'])
ax.set_yticks([60,80,100,120, 140, 160, 180, 200, 220, 240])
ax.set_yticklabels(['','80','','120', '', '160', '', '200', '','240'])
fig.text(0.6,0.8, '0.0 K/day', color='k', fontsize='small')
kaptp = 5000000
# fig.text(0.37,0.73, r'$\kappa$ = ' + str(kaptp) + r' m$^2$/kg', fontsize='small', color='silver')

count = 0
ssm_tp = []
ts = []
for exp in data:
    count+=1
    ssm_tp.append(tf.ssm_tp(0.7, 5000000, exp))
    ts.append(tf.Ts(exp))
#     print(str(tf.Ttp_conv(exp, threshold=0)))
#     print(str(tf.ssm_tp(0.7, 5000000, exp)))
#     print()
    ax.scatter(tf.Ts(exp), tf.Ttp_conv(exp, threshold=0), color=cm.coolwarm(0.5-(count/(len(data)+1))/2), s=4)
# ax.plot(ts, ssm_tp, color='silver', linewidth=0.5, zorder=-1)

#####################################################################    
########## TROPOPAUSE TEMPERATURE COMPARISON ########################   
#####################################################################
fig, axes = fc(1, 1, width=2, aspect=aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=160, xmax=350, ymin=195, ymax=160,xlabel=r'$T_s$ (K)',ylabel=r'$T_{tp}$ (K)')
ax.set_xticks([160,180,200,220, 240, 260, 280, 300, 320, 340])
ax.set_xticklabels(['','180','','220', '', '260', '', '300', '','340'])
# ax.set_yticks([120, 140, 160, 180, 200, 220, 240])
# ax.set_yticklabels(['','80','','120', '', '160', '', '200', '','240'])
fig.text(0.15,0.8, '0.0 K/day', color='k', fontsize='small')
fig.text(0.15,0.73, 'no adjustment', color='navy')
fig.text(0.15,0.66, r'$\partial _z q$ $\leq$ 0 enforced', color='darkred')

count=0
for exp in data:
    count+=1
#     ax.scatter(tf.Ts(exp), tf.ssm_tp(0.7, 30000, exp), color='cornflowerblue', s=4)
    ax.scatter(tf.Ts(exp), tf.Ttp_conv(exp, threshold=0), color=cm.coolwarm(0.5+(count/(len(data)+1))/2), s=6)
#     print(str(tf.Ttp_conv(exp, threshold=0)))

ssm_tp = []
ts = []
count=0
for exp in data_adj:
    count+=1
    ax.scatter(tf.Ts(exp), tf.Ttp_conv(exp, threshold=0), color=cm.coolwarm(0.5-(count/(len(data)+1))/2), s=3, marker='*')
    ssm_tp.append(tf.ssm_tp(0.7, 5000000, exp))
    ts.append(tf.Ts(exp))
# ax.plot(ts, ssm_tp, color='indianred', linewidth=0.5)
#     print(str(tf.Ttp_conv(exp, threshold=0)))

#####################################################################    
#################### BOUNDARY LAYER HEIGHT ##########################   
#####################################################################
fig, axes = fc(1, 1, width=width, aspect=1/aspect, internal_pad=0)
ax = axes[0]
ppf.make_pretty_plot(ax, xmin=160, xmax=350, ymin=0, ymax=1500,xlabel=r'$T_s$ (K)',ylabel=r'BL Height (m)')
ax.set_xticks([160,180,200,220, 240, 260, 280, 300, 320, 340])
ax.set_xticklabels(['','180','','220', '', '260', '', '300', '','340'])

count = 0
for exp in data:
    count+=1
    ax.scatter(tf.Ts(exp), exp.pbl_height.mean(('lon','lat','time')), color=cm.coolwarm(0.5-(count/(len(data)+1))/2), s=4)
    
