import os
import urllib.request
import zipfile

dir = "../../data/nvd/year"
os.system(f"rm -rf {dir}")

if not os.path.exists(dir):
    os.makedirs(dir)
    print(f"Creating {dir}...")

for i in range(2002, 2023):
    url = f"https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-{i}.json.zip"
    file_name = f"{dir}/nvdcve-1.1-{i}.json.zip"
    destination = f"{dir}/nvdcve-1.1-{i}.zip"

    urllib.request.urlretrieve(url, file_name)
    os.rename(file_name, destination)

    with zipfile.ZipFile(destination, "r") as zip_ref:
        zip_ref.extractall(dir)

    os.remove(destination)
