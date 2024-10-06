import requests
import json

with open('config.json') as file:
    data = json.load(file)
    api_key = data['nasa_api_key']

base_url = "https://api.nasa.gov/mars-photos/api/v1/"

curiosity_manifest_url = f"https://api.nasa.gov/mars-photos/api/v1/manifests/curiosity?api_key={api_key}"
opportunity_manifest_url = f"https://api.nasa.gov/mars-photos/api/v1/manifests/opportunity?api_key={api_key}"
spirit_manifest_url = f"https://api.nasa.gov/mars-photos/api/v1/manifests/spirit?api_key={api_key}"

manifest_dict = {'curiosity': curiosity_manifest_url,
                 'opportunity': opportunity_manifest_url,
                 'spirit': spirit_manifest_url}

for rover_name, manifest in manifest_dict.items():

    response = requests.get(manifest)
    data = response.json()

    filename = f"{rover_name}_manifest.json"
    with open(filename, 'w') as rover_json:
        json.dump(data, rover_json, indent=4)
