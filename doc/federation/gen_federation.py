"""Generate HTML binderhubs tables for team pages
"""
import pandas as pd
import os
import os.path as op
from ruamel import yaml

# Variables
N_PER_ROW = 4

# Code to generate the HTML grid
template_binderhub = """
```{{grid-item-card}}
:text-align: center
:class-header: bg-light
:class-body: p-4 d-flex align-items-center
:class-footer: bg-light

[{BINDERHUB_SUBDOMAIN}]({URL_BINDERHUB})
^^^
![{RUN_BY}]({LOGO})
+++
Run by [{RUN_BY}]({RUN_BY_LINK})

Funded by [{FUNDED_BY}]({FUNDED_BY_LINK})
```

"""

# Run the function
path_data = op.join(
    op.dirname(op.abspath(__file__)), "..", "federation", "data-federation.yml"
)
yaml = yaml.YAML()

with open(path_data, "r") as ff:
    data = yaml.load(ff)

binderhubs = pd.DataFrame(data)

entries = []
for ix, binderhub in binderhubs.iterrows():
    entries.append(template_binderhub.format(URL_BINDERHUB=binderhub["url_binderhub"],
        BINDERHUB_SUBDOMAIN=binderhub["url_binderhub"].split("//")[-1],
        LOGO=binderhub["logo"],
        RUN_BY=binderhub["run_by"],
        RUN_BY_LINK=binderhub["run_by_link"],
        FUNDED_BY=binderhub["funded_by"],
        FUNDED_BY_LINK=binderhub["funded_by_link"],))
entries = "\n".join(entries)

directive = f"""
````{{grid}} 1 1 2 2
:class-container: federation-members
:gutter: 4

{entries}
````
"""

new_name = os.path.splitext(path_data)[0]
with open(new_name + ".txt", "w") as ff:
    ff.write(directive)
