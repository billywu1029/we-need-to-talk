import pandas
import geopandas
import json
import unidecode

df = geopandas.read_file("tur_polbnda_adm1.shp")
with open("../provinces_data.json", "r") as f:
    province_data = json.load(f)
df["adm1_tr"] = df["adm1_tr"].str.capitalize()
df["adm1_en"] = df["adm1_en"].str.capitalize()

# unidecode replaces Turkish characters with Latin alphabet equivalents to match
# the shapefile province names
pps = {unidecode.unidecode(province): province_data[province]["Period Poverty Score"] for province in
        province_data}

df["pps"] = df["adm1_en"].map(pps)
df.to_file("modified_adm1_tr.shp")
print("Shapefile modified, table is:")
print(df)

