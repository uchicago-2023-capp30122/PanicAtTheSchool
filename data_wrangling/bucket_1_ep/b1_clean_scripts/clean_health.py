# Steps:
# 1. Obtain needed columns from health_atlas csv --Done
# 2. Clean extracted columns: look for inconsistencies --Done
# 3. Normalize columns- mean of zero and standard deviation of 1 --Done
# 4. Same process for demographic_data - Done
# 5. Merge the two files on ID Community areas - Done
# 6. New file has all the health and demographic data ready to be analysed - Done

import pandas as pd

# Check final location and name of file- will definitely lead to bugs in case of incorrect pathname
ha_df = pd.read_csv("health_indicators_atlas_v2.csv", skiprows=range(4))
ha_df = ha_df.loc[
    :,
    [
        "Name",
        "GEOID",
        "Population",
        "Longitude",
        "Latitude",
        "VRBWP_2013-2017",
        "UNS_2017-2021",
        "VRPNCP_2013-2017",
        "VAC_2017-2021",
        "HTA_2017-2021",
        "HCSCBP_2016-2018",
        "HCSCBP_2020-2021",
        "SNP_2017-2021",
        "SNQ_2017-2021",
        "RBU_2017-2021",
        "VRHOR_2015-2019",
        "VRDIDR_2015-2019",
    ],
]

ha_df = ha_df.rename(
    columns={
        "Name": "comm_area",
        "GEOID": "ca_id",
        "Population": "pop",
        "Longitude": "long",
        "Latitude": "lat",
        "VRBWP_2013-2017": "low_bw_rate",
        "UNS_2017-2021": "uninsured_rate",
        "VRPNCP_2013-2017": "adq_child_care",
        "VAC_2017-2021": "perc_vacant_units",
        "HTA_2017-2021": "perc_sing_par_hh",
        "HCSCBP_2016-2018": "comm_belong_16_18",
        "HCSCBP_2020-2021": "comm_belong_20_21",
        "SNP_2017-2021": "perc_hh_stamps",
        "SNQ_2017-2021": "perc_not_getting_stamps",
        "RBU_2017-2021": "rent_burdened_hh",
        "VRHOR_2015-2019": "homicide_rate",
        "VRDIDR_2015-2019": "drug_induced_dt_rate",
    }
)
#comm_belong_16_18 has 1 missing value; will impute average of remaining
col_impute_val = ha_df["comm_belong_16_18"].mean()
ha_df["comm_belong_16_18"].fillna(col_impute_val, inplace=True)
ha_df.to_csv('clean_health_atlas.csv', index = False)