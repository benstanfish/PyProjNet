__doc__ = f"Module \"{__name__}\" stores user preferences for the \"tableStyler\" module."

import json
with open('PyTables/settings.json', 'r') as file_contents:
    settings = json.load(file_contents)