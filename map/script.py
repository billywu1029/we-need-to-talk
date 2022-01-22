import pandas
import geopandas
import json

df = geopandas.read_file("tur_polbnda_adm1.shp")
with open("../provinces_data.json", "r") as f:
    province_data = json.load(f)
df["adm1_tr"] = df["adm1_tr"].str.capitalize()
df["adm1_en"] = df["adm1_en"].str.capitalize()

pps = {province: province_data[province]["Period Poverty Score"] for province in
        province_data}

df["pps"] = df["adm1_tr"].map(pps)

df.to_file("modified_adm1_tr.shp")
