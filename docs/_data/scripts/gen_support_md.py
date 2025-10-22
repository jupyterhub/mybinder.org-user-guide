"""Generate snippets of markdown for various types of supporters.
These are meant to be inserted into our docs.
"""
from pathlib import Path
from yaml import safe_load
from textwrap import dedent

# Read from our YAML data file 
path_root = Path(__file__).parent.parent
path_data = path_root / "support" / "supporters.yml"
supporters_yaml = safe_load(path_data.read_text())
for kind, supporters in supporters_yaml.items():
  # This is where we write the txt snippet to be imported
  path_snippet = path_root.joinpath("snippets", f"supporters_{kind}_md.txt")
  path_snippet.parent.mkdir(parents=True, exist_ok=True)

  # If no supporters are listed juts write a short message saying there are none.
  if not supporters:
    path_snippet.write_text("**There are currently no supporters of this category.**")
    continue

  # Generate markdown entries for each member
  output = ""
  for supporter in supporters:
      output += dedent(f"""
      ```{{grid-item-card}}
      :text-align: center
      :class-card: bg-light
      :class-body: sd-p-4 d-flex sd-m-auto
      :link: {supporter["url"]}
      :text-align: center

      **{supporter["name"]}**
      ^^^

      <img src="{supporter['logo']}" class="dark-light" style="max-height:5em;min-height:2em;" />
      
      ```

      """)

  # Wrap the entries in a `grid` directive
  directive = dedent("""
  ````{{grid}} 1 1 2 2
  :class-container: support-{kind}
  :gutter: 4

  {output}
  ````
  """)
  directive = directive.format(output=output, kind=kind)

  # Write a txt file that we can insert into docs
  path_snippet.write_text(directive)
