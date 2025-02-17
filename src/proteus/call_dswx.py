# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:57:50 2023

@author: LUV14
"""
from dswx_hls import generate_dswx_layers

generate_dswx_layers('D:/Luisa/start_insitu_data_wrongdata/downloaded/HLS.S30.T18TWK.2021250T154809.v2.0.B03.subset.tif',
                         output_file = 'D:/Luisa/start_insitu_data_wrongdata/proteus_tentative/HLS.S30.T18TWK.2021250T154809.v2.0.B03.subset.tif',
                         hls_thresholds = None,
                         dem_file=None,
                         dem_file_description=None,
                         output_interpreted_band=None,
                         output_rgb_file=None,
                         output_infrared_rgb_file=None,
                         output_binary_water=None,
                         output_confidence_layer=None,
                         output_diagnostic_layer=None,
                         output_non_masked_dswx=None,
                         output_shadow_masked_dswx=None,
                         output_landcover=None,
                         output_shadow_layer=None,
                         output_cloud_layer=None,
                         output_dem_layer=None,
                         output_browse_image=None,
                         browse_image_height=None,
                         browse_image_width=None,
                         exclude_psw_aggressive_in_browse=None,
                         not_water_in_browse=None,
                         cloud_in_browse=None,
                         snow_in_browse=None,
                         landcover_file=None,
                         landcover_file_description=None,
                         worldcover_file=None,
                         worldcover_file_description=None,
                         shoreline_shapefile=None,
                         shoreline_shapefile_description=None,
                         flag_offset_and_scale_inputs=False,
                         scratch_dir='.',
                         product_id=None,
                         product_version=None,
                         check_ancillary_inputs_coverage=None,
                         apply_ocean_masking=None,
                         apply_aerosol_class_remapping=None,
                         aerosol_not_water_to_high_conf_water_fmask_values=None,
                         aerosol_water_moderate_conf_to_high_conf_water_fmask_values=None,
                         aerosol_partial_surface_water_conservative_to_high_conf_water_fmask_values=None,
                         aerosol_partial_surface_aggressive_to_high_conf_water_fmask_values=None,
                         shadow_masking_algorithm=None,
                         min_slope_angle=None,
                         max_sun_local_inc_angle=None,
                         mask_adjacent_to_cloud_mode=None,
                         forest_mask_landcover_classes=None,
                         ocean_masking_shoreline_distance_km=None,
                         flag_debug=False)