import os
import numpy as np
from isca import SocColumnCodeBase, DiagTable, Experiment, Namelist, GFDL_BASE

# column model only uses 1 core
NCORES = 1

# compile code
base_dir = os.path.dirname(os.path.realpath(__file__))
cb = SocColumnCodeBase.from_directory(GFDL_BASE)

cb.compile()

S0_add = 0. # S0 =  1360
co2_multiply = float(32) # PI = 280
co2_string = '32'
RH = 0.7
ml_depth = float(1e10)
sst = 290.
ml_temp = sst

exp = Experiment('col_exp_'+'LW_h2o_co2_'+str(sst)+'K'+'_PIx'+co2_string+'_take1', codebase=cb)
#Tell model how to write diagnostics
diag = DiagTable()
diag.add_file('atmos_monthly', 30, 'days', time_units='days')

#Tell model which diagnostics to write
diag.add_field('column', 'ps', time_avg=True)
diag.add_field('column', 'bk')
diag.add_field('column', 'pk')
diag.add_field('atmosphere', 'precipitation', time_avg=True)
diag.add_field('mixed_layer', 't_surf', time_avg=True)
diag.add_field('mixed_layer', 'flux_lhe', time_avg=True)
diag.add_field('mixed_layer', 'flux_t', time_avg=True)
diag.add_field('column', 'sphum', time_avg=True)
diag.add_field('column', 'ucomp', time_avg=True)
diag.add_field('column', 'vcomp', time_avg=True)
diag.add_field('column', 'temp', time_avg=True)
diag.add_field('column', 'height', time_avg=True)

# SOCRATES
diag.add_field('socrates', 'soc_tdt_lw', time_avg=True)
diag.add_field('socrates', 'soc_tdt_sw', time_avg=True)
diag.add_field('socrates', 'soc_tdt_rad', time_avg=True)
diag.add_field('socrates', 'soc_surf_flux_lw', time_avg=True)
diag.add_field('socrates', 'soc_surf_flux_sw', time_avg=True)
diag.add_field('socrates', 'soc_surf_flux_lw_down', time_avg=True)
diag.add_field('socrates', 'soc_surf_flux_sw_down', time_avg=True)
diag.add_field('socrates', 'soc_olr', time_avg=True)
diag.add_field('socrates', 'soc_toa_sw', time_avg=True)
diag.add_field('socrates', 'soc_toa_sw_down', time_avg=True)
diag.add_field('socrates', 'soc_co2', time_avg=True)
diag.add_field('socrates', 'soc_spectral_olr', time_avg=True)
diag.add_field('atmosphere', 'dt_ug_diffusion', time_avg=True)
diag.add_field('atmosphere', 'dt_vg_diffusion', time_avg=True)
diag.add_field('atmosphere', 'dt_tg_diffusion', time_avg=True)
diag.add_field('atmosphere', 'dt_qg_diffusion', time_avg=True)
diag.add_field('atmosphere', 'dt_qg_convection', time_avg=True)
diag.add_field('atmosphere', 'dt_tg_convection', time_avg=True)
diag.add_field('atmosphere', 'dt_tg_condensation', time_avg=True)
diag.add_field('atmosphere', 'dt_qg_condensation', time_avg=True)
diag.add_field('atmosphere', 'dt_qg_total', time_avg=True)
diag.add_field('atmosphere', 'pbl_height', time_avg=True)
diag.add_field('atmosphere', 'rh', time_avg=True)
diag.add_field('atmosphere', 'convection_rain', time_avg=True)
diag.add_field('atmosphere', 'cape', time_avg=True)
diag.add_field('atmosphere', 'cin', time_avg=True)
diag.add_field('atmosphere', 'pLCL', time_avg=True)
diag.add_field('atmosphere', 'pLZB', time_avg=True)
diag.add_field('atmosphere', 'kLZB', time_avg=True)
diag.add_field('atmosphere', 'pshallow', time_avg=True)
diag.add_field('atmosphere', 'convflag', time_avg=True)
diag.add_field('atmosphere', 'shallower_flag', time_avg=True)
diag.add_field('atmosphere', 'deep_gorman_flag', time_avg=True)
diag.add_field('atmosphere', 'deep_frierson_flag', time_avg=True)
diag.add_field('atmosphere', 'noconvflag', time_avg=True)
diag.add_field('atmosphere', 'precip_level_DNE_flag', time_avg=True)
diag.add_field('atmosphere', 'precip_level_DNE_ktop_flag', time_avg=True)
diag.add_field('atmosphere', 'precip_both_negative_flag', time_avg=True)
diag.add_field('atmosphere', 'z_pbl', time_avg=True)
diag.add_field('column', 'dt_a', time_avg=True)


exp.diag_table = diag

#Empty the run directory ready to run
exp.clear_rundir()

#Define values for the 'core' namelist
exp.namelist = namelist = Namelist({
    'main_nml':{
     'days'   : 360,
     'hours'  : 0,
     'minutes': 0,
     'seconds': 0,
     # 'dt_atmos':7200,  # default
     'dt_atmos':3600, # 600 for highres
     'current_date' : [1,1,1,0,0,0],
     'calendar' : 'thirty_day'
         },

    'atmosphere_nml': {
        'idealized_moist_model': True
    },

    'column_nml': {
        'lon_max': 1, # number of columns in longitude, default begins at lon=0.0
        'lat_max': 1, # number of columns in latitude, precise
                      # latitude can be set in column_grid_nml if only 1 lat used.
        'num_levels': 100,  # number of levels
        'initial_sphum': 1e-3, # default 1e-6
        'vert_coord_option': 'uneven_sigma',
        'surf_res':0.25,
        'scale_heights':7.0,
        'exponent':5.0,
        'robert_coeff':0.
    },

    'column_grid_nml': {
        # 'lat_value': 10 # deep tropics
        'lat_value': np.rad2deg(np.arcsin(1/np.sqrt(3))) # set latitude to that which causes insolation in frierson p2 radiation to be insolation / 4.
        # 'global_average': True # don't use this option at the moment
    },

    # set initial condition, NOTE: currently there is not an option to read in initial condition from a file.
    'column_init_cond_nml': {
        'initial_temperature': sst-1, # initial atmospheric temperature 264, the sst in isca is the initial_temperature +1.
        'surf_geopotential': 0.0, # applied to all columns
        'surface_wind': 5. # as described above
    },

    'idealized_moist_phys_nml': {
        'do_damping': False, # no damping in column model, surface wind prescribed
        'turb':True,        # DONT WANT TO USE THIS, BUT NOT DOING SO IS STOPPING MIXED LAYER FROM WORKING
        'mixed_layer_bc':True, # need surface, how is this trying to modify the wind field? ****
        'do_simple': True, # simple RH calculation
        'roughness_mom': 3.21e-05, # DONT WANT TO USE THIS, BUT NOT DOING SO IS STOPPING MIXED LAYER FROM WORKING
        'roughness_heat':3.21e-05,
        'roughness_moist':3.21e-05,
        'two_stream_gray': False,     #Use grey radiation
        'do_rrtm_radiation': False,
        'do_socrates_radiation': True,
        'convection_scheme': 'SIMPLE_BETTS_MILLER', #Use the simple Betts Miller convection scheme
        # 'convection_scheme': 'FULL_BETTS_MILLER', #Use the Full Betts Miller convection scheme
    },

    'socrates_rad_nml': {
        'stellar_constant':1370.+S0_add,
        'lw_spectral_filename':'/home/links/bam218/Isca/src/atmos_param/socrates/src/trunk/data/spectra/ga7/sp_lw_ga7',
        # 'lw_spectral_filename':'/home/links/bam218/spectral_files/sp_lw_17_dsa_arcc',
        'sw_spectral_filename':'/home/links/bam218/Isca/src/atmos_param/socrates/src/trunk/data/spectra/ga7/sp_sw_ga7',
        # 'do_read_ozone': False,
        'dt_rad':3600, # default 3600
        'store_intermediate_rad':True,
        'chunk_size': 1, # default 16
        'use_pressure_interp_for_half_levels':False,
        'tidally_locked':False,
        'inc_co2': False,
        'co2_ppmv':280.*co2_multiply,
        'inc_o3':False,
        'inc_o2':False,
        'account_for_effect_of_ozone':False
        # 'do_rad_time_avg':True, # from RRTM
        # 'dt_rad_avg':86400, # from RRTM
        #'solday': 90
    },

    'qe_moist_convection_nml': {
        'rhbm':RH, # rh criterion for convection
        'Tmin':100, # min temperature for convection scheme look up tables
        'Tmax':350.  # max temperature for convection scheme look up tables
    },

    'lscale_cond_nml': {
        'do_simple':True, # only rain
        'do_evap':False,  # no re-evaporation of falling precipitation
    },

    'surface_flux_nml': {
        'use_virtual_temp': True, # use virtual temperature for BL stability
        'do_simple': True,
        'old_dtaudv': True
    },

    'vert_turb_driver_nml': { # DONT WANT TO USE THIS, BUT NOT DOING SO IS STOPPING MIXED LAYER FROM WORKING
        'do_mellor_yamada': False,     # default: True
        'do_diffusivity': True,        # default: False
        'do_simple': True,             # default: False
        'constant_gust': 0.0,          # default: 1.0
        'use_tau': False
    },

    'diffusivity_nml': {
        'fixed_depth': True, # default: False
        # 'depth_0': BL_height, # default: 5000.0 (in meters)
    },

    #Use a large mixed-layer depth, and the Albedo of the CTRL case in Jucker & Gerber, 2017
    'mixed_layer_nml': {
        'tconst' : ml_temp, # default: 285
        'prescribe_initial_dist':False,
        'evaporation':True,
        'depth': ml_depth,                          #Depth of mixed layer used, 20 mostly
        'albedo_value': 0.20,                  #Albedo value used
    },

    'sat_vapor_pres_nml': {
        'do_simple':True,
    },

    # FMS Framework configuration
    'diag_manager_nml': {
        'mix_snapshot_average_fields': False  # time avg fields are labelled with time in middle of window
    },
    'fms_nml': {
        'domains_stack_size': 600000                        # default: 0
    },
    'fms_io_nml': {
        'threading_write': 'single',                         # default: multi
        'fileset_write': 'single',                           # default: multi
    },


    'astronomy_nml': {
            'ecc' : 0.0,
            'obliq' : 0.0,
            'per' : 0.0
            },

})

#Lets do a run!
if __name__=="__main__":

    exp.run(1, use_restart=False, num_cores=NCORES)
    # for i in range(2,11):
    for i in range(2,31):
        exp.run(i, num_cores=NCORES)
