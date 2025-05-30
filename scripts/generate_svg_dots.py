import os
from pathlib import Path

# Define the language colors (keys = language, values = GitHub hex color)
language_colors = {
    "python": "#3572A5",
    "cpp": "#f34b7d",
    "c": "#555555",
    "assembly": "#6E4C13",
    "shell": "#89e051",
    "docker": "#0db7ed",
    "postgresql": "#336791",
    "pytorch": "#EE4C2C",
    "sql": "#DA5B0B",
    "dart": "#0175C2",
    "deepblue": "#0D47A1",
    "ceruleanblue": "#1976D2",
    "fluttersky": "#007ACC",
    "trueazure": "#0088CC",
    "brightcyanblue": "#0095DD",
    "fluorescentblue": "#00A3E0",
    "firestore": "#FFCA28",
    "r": "#198CE7",
    "mpi": "#0072C6",
    "openmp": "#E4B400",
    "slurm": "#1E7145",
    "cuda": "#76B900"
}

# Directory to store the SVG files
output_dir = Path(__file__).parent.parent / "assets" / "svg"
output_dir.mkdir(parents=True, exist_ok=True)

# SVG template for a small circle
svg_template = """<svg width="10" height="10" xmlns="http://www.w3.org/2000/svg">
  <circle cx="4" cy="4" r="4" fill="{color}" />
</svg>"""

# Generate SVG files
for language, color in language_colors.items():
    out_path = output_dir / f"{language}-dot.svg"
    # filename = f"{output_dir}/{language.lower().replace(' ', '-')}-dot.svg"
    with out_path.open(mode="w") as file:
    # with open(filename, "w") as file:
        file.write(svg_template.format(color=color))
    print(f"Generated: {str(out_path)}")

print("\n✅ SVG files have been generated successfully!")