import json

def load_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

# Example usage
file_path = "/home/abhi/Desktop/PRECOGS/security-patches-dataset/data/nvd/year/nvdcve-1.1-2002.json"  # Replace with the actual path to your JSON file
json_data = load_json_file(file_path)

# Process the loaded JSON data (dictionary)
print(json_data)
