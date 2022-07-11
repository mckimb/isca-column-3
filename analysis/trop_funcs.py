import numpy as np
import xarray as xr
import scipy.special.lambertw as lambertw
import trop_constants as tc

###############################################################
###### GET THE SURFACE TEMPERATURE FROM ISCA COLUMN MODEL #####
###############################################################
def Ts(data):
    ts = data.t_surf.mean(('lon','lat','time')).values
    return ts

###############################################################
########### GET CONVECTIVE TOP FROM ISCA COLUMN MODEL #########
###############################################################
def Ttp_conv(data, threshold):
    convheat = data.dt_tg_convection.mean(('lon','lat','time'))*86400
    temp = data.temp.mean(('lon','lat','time'))
    mask = convheat.where(convheat>threshold)
    if np.sum(~np.isnan(mask.values)) == 0 or np.sum(~np.isnan(mask.values))==len(mask):
        p_tp = data.pfull.values[-1]
        t_tp = float(Ts(data))
    else:
        convective_top_value = next(x for x in mask if not np.isnan(x))
        p_tp = convheat.where(convheat==convective_top_value, drop=True).pfull.values[0]
        t_tp = temp.sel(pfull=p_tp).values
    return t_tp

def Ptp_conv(data, threshold):
    convheat = data.dt_tg_convection.mean(('lon','lat','time'))*86400
    temp = data.temp.mean(('lon','lat','time'))
    mask = convheat.where(convheat>threshold)
    if np.sum(~np.isnan(mask.values)) == 0 or np.sum(~np.isnan(mask.values)) == len(mask):
        p_tp = data.pfull.values[-1]
        t_tp = float(Ts(data))
    else:
        convective_top_value = next(x for x in mask if not np.isnan(x))
        p_tp = convheat.where(convheat==convective_top_value, drop=True).pfull.values[0]
        t_tp = temp.sel(pfull=p_tp).values
    return p_tp

###############################################################
########### GET RADIATIVE TOP FROM ISCA COLUMN MODEL ##########
###############################################################
def Ttp_H(data, threshold):
#     convheat = data.tdt_rad.mean(('lon','lat','time'))*86400
    convheat = data.soc_tdt_rad.mean(('lon','lat','time'))*86400
    temp = data.temp.mean(('lon','lat','time'))
    mask = convheat.where(convheat<threshold)
    convective_top_value = next(x for x in mask if not np.isnan(x))
    p_tp = convheat.where(convheat==convective_top_value, drop=True).pfull.values[0]
    t_tp = temp.sel(pfull=p_tp).values
    return t_tp

def Ptp_H(data, threshold):
#     convheat = data.tdt_rad.mean(('lon','lat','time'))*86400
    convheat = data.soc_tdt_rad.mean(('lon','lat','time'))*86400
    temp = data.temp.mean(('lon','lat','time'))
    mask = convheat.where(convheat<threshold)
    convective_top_value = next(x for x in mask if not np.isnan(x))
    p_tp = convheat.where(convheat==convective_top_value, drop=True).pfull.values[0]
    t_tp = temp.sel(pfull=p_tp).values
    return p_tp

###############################################################
######## GET RADIATIVE TOP FROM SIMPLE SPECTRAL MODEL #########
###############################################################
def ssm_tp(RH,kaptp,data):
    tsurf = Ts(data) 
    temp = data.temp.mean(('lon','lat','time'))
    Tref = float(temp.sel(pfull=tc.pref, method='nearest').values)
    Tav = (tsurf + tc.Tstrat)/2
    WVP0 = Tav * RH * tc.Pvinf / (tc.Gamma * tc.L)
    Tstar = tc.L * tc.Rd * tc.Gamma / (tc.g * tc.Rv)

    return float(Tstar / lambertw( Tstar/Tref * (tc.D*WVP0*kaptp)**(tc.Rd*tc.Gamma/tc.g) ))

###############################################################
######################## OLD FUNCTIONS ########################
###############################################################
# # get the radiative tropopause temperature from isca column model
# def Ttp_H(data, threshold=-0.2):
#     if Ts(data)>=320:
#         pthresh=50
#     if Ts(data)<=300:
#         pthresh = 850
#         if Ts(data)<=240:
#             pthresh=1025
#     else:
#         pthresh = 400
#     radheat = data.tdt_rad.mean(('lon','lat','time'))*86400
#     temp = data.temp.mean(('lon','lat','time'))
#     radheat = radheat.reindex(pfull=radheat.pfull[::-1])
#     temp = temp.reindex(pfull=temp.pfull[::-1])  
#     radheat_upper = radheat.where(radheat.pfull<pthresh)
#     radheat_threshold = radheat_upper.where(radheat_upper>threshold)
#     threshold_value = next(x for x in radheat_threshold if not np.isnan(x))
#     p_tp = radheat_threshold.where(radheat_threshold==threshold_value.values, drop=True).pfull.values
#     t_tp = temp.sel(pfull=p_tp).values[0]
#     return t_tp

# # get the radiative tropopause pressure from isca column model
# def Ptp_H(data, threshold=-0.2):
#     if Ts(data)>=320:
#         pthresh=50
#     if Ts(data)<=300:
#         pthresh = 850
#         if Ts(data)<=240:
#             pthresh=1025
#     else:
#         pthresh = 400
#     radheat = data.tdt_rad.mean(('lon','lat','time'))*86400
#     temp = data.temp.mean(('lon','lat','time'))     
#     radheat = radheat.reindex(pfull=radheat.pfull[::-1])
#     temp = temp.reindex(pfull=temp.pfull[::-1]) 
#     radheat_upper = radheat.where(radheat.pfull<pthresh)
#     radheat_threshold = radheat_upper.where(radheat_upper>threshold)
#     threshold_value = next(x for x in radheat_threshold if not np.isnan(x))
#     p_tp = radheat_threshold.where(radheat_threshold==threshold_value.values, drop=True).pfull.values
#     return p_tp


#     convheat = data.dt_tg_convection.mean(('lon','lat','time'))*86400
#     temp = data.temp.mean(('lon','lat','time'))
#     mask = convheat.where(convheat>threshold)
#     convective_top_value = next(x for x in mask if not np.isnan(x))
#     p_tp = convheat.where(convheat==convective_top_value, drop=True).pfull.values[0]
#     t_tp = temp.sel(pfull=p_tp).values
#     return t_tp