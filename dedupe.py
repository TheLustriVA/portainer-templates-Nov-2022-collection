import json
from collections import OrderedDict

def load_json_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def save_json_file(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def main(dry_run: bool=False):
    file_path = "mlva-templates-2.0-deduped.json"
    output_path = "mlva-templates-2.2.rc2-deduped.json"
    
    data = load_json_file(file_path)
    version = data["version"]
    portainer_templates = data["templates"]

    cleaned_templates = OrderedDict()
    for template in portainer_templates:
        title = template["title"]

        if title not in cleaned_templates:
            cleaned_templates[title] = OrderedDict(template)
        else:
            break

    cleaned_data = {
        "version": "2.1",
        "portainer_templates": list(cleaned_templates.values())
    }

    if dry_run:
        print(json.dumps(cleaned_data, indent=2))
        return
    save_json_file(output_path, cleaned_data)

if __name__ == "__main__":
    main()

