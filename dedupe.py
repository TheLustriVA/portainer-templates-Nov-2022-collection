import json

def load_json_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def save_json_file(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def main():
    file_path = "mlva-templates-2.0-deduped.json"
    output_path = "mlva-templates-2.1-deduped.json"
    
    data = load_json_file(file_path)
    version = data["version"]
    portainer_templates = data["templates"]

    cleaned_templates = {}
    for template in portainer_templates:
        title = template["title"]

        if title not in cleaned_templates:
            cleaned_templates[title] = template
        else:
            existing_template = cleaned_templates[title]
            new_template = template

            existing_keys = set(existing_template.keys())
            new_keys = set(new_template.keys())
            
            if ("description" in existing_keys and "note" in existing_keys) or \
                ("description" in new_keys and "note" in new_keys):

                if len(existing_keys) < len(new_keys):
                    cleaned_templates[title] = new_template

            elif len(existing_keys) < len(new_keys):
                cleaned_templates[title] = new_template

    cleaned_data = {
        "version": "2.1",
        "portainer_templates": list(cleaned_templates.values())
    }

    save_json_file(output_path, cleaned_data)

if __name__ == "__main__":
    main()

