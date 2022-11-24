"""Generate snippets of markdown for various types of supporters.
These are meant to be inserted into our docs.
"""
from pathlib import Path
from yaml import safe_load

# Code to generate the HTML grid
template_binderhub = """
```{{grid-item-card}}
:text-align: center
:class-header: sd-text-dark
:class-body: sd-p-4 sd-m-auto
:class-card: bg-light
:text-align: center
:link: {URL_BINDERHUB}

**{BINDERHUB_SUBDOMAIN}**

^^^

<img src="{LOGO}" class="dark-light" style="max-height: 5em; min-height: 2em;" />
```

"""

# Read from our YAML data file 
path_root = Path(__file__).parent.parent
path_data = path_root / "support" / "federation.yml"
binderhubs = safe_load(path_data.read_text())

# Generate markdown entries for each federation member
entries = []
for binderhub in binderhubs:
    entries.append(template_binderhub.format(URL_BINDERHUB=binderhub["url_binderhub"],
        BINDERHUB_SUBDOMAIN=binderhub["url_binderhub"].split("//")[-1],
        LOGO=binderhub["logo"],
        RUN_BY=binderhub["run_by"],
        RUN_BY_LINK=binderhub["run_by_link"],
        FUNDED_BY=binderhub["funded_by"],
        FUNDED_BY_LINK=binderhub["funded_by_link"],))
entries = "\n".join(entries)

# Wrap the entries in a `grid` directive
directive = f"""
````{{grid}} 1 1 2 2
:class-container: federation-members
:gutter: 4

{entries}
````
"""

# Write a txt file that we can insert into docs
path_md = path_root.joinpath("snippets", "federation_md.txt")
path_md.parent.mkdir(parents=True, exist_ok=True)
path_md.write_text(directive)
