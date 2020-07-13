from arcgis.gis import GIS
anon_gis = GIS()
features = anon_gis.content.get('dd4580c810204019a7b8eb3e0b329dd6').tables[0].query()
features.save(save_location='.', out_name="data.csv")

import requests
url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Projekte_RKI/Nowcasting_Zahlen.xlsx?__blob=publicationFile'
with open('nowcasting.xlsx', 'wb') as file:
    file.write(requests.get(url).content)
