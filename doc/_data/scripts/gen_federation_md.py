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
:link: {LINK}

**{TITLE}**

^^^

<img src="{LOGO}" class="dark-light" style="max-height: 5em; min-height: 2em;" />
```

"""

# Read from our YAML data file
path_root = Path(__file__).parent.parent
path_data = path_root / "support" / "federation.yml"
binderhubs = safe_load(path_data.read_text())


def make_entry(binderhub: dict) -> str:
    active = binderhub.get("active", True)
    if active:
        link = binderhub["url_binderhub"]
    else:
        link = binderhub["funded_by_link"]
    return template_binderhub.format(
        LINK=link,
        TITLE=binderhub["url_binderhub"].split("//")[-1],
        LOGO=binderhub["logo"],
        RUN_BY=binderhub.get("run_by", binderhub["funded_by"]),
        RUN_BY_LINK=binderhub.get("run_by_link", binderhub["funded_by_link"]),
        FUNDED_BY=binderhub["funded_by"],
        FUNDED_BY_LINK=binderhub["funded_by_link"],
    )


# Generate markdown entries for each federation member
active_entries = []
past_entries = []
for binderhub in binderhubs:
    entry = make_entry(binderhub)
    if binderhub.get("active", True):
        active_entries.append(entry)
    else:
        past_entries.append(entry)

# Wrap the entries in a `grid` directive
directive_template = """
````{{grid}} 1 1 2 2
:class-container: federation-members
:gutter: 4

{ENTRIES}
````
"""

snippet_dir = path_root / "snippets"
snippet_dir.mkdir(parents=True, exist_ok=True)
for snippet_name, entries in [
    ("federation_md.txt", active_entries),
    ("federation_past_md.txt", past_entries),
]:
    # Write a txt file that we can insert into docs
    directive = directive_template.format(ENTRIES="\n".join(entries))
    path_md = snippet_dir / snippet_name
    path_md.write_text(directive)
    print(f"Wrote {len(entries)} entries to {path_md}")
