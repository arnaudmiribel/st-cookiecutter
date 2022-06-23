import os
import shutil

REMOVE_PATHS = [
    "{% if not cookiecutter.app_uses_secrets|int %} .streamlit/secrets.toml {% endif %}",
    "{% if not cookiecutter.app_is_multi_page|int %} pages {% endif %}",
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        else:
            os.unlink(path)

# Add Streamlit secrets to .gitignore
with open(".gitignore", "a") as gitignore:
    gitignore.write("\n")
    gitignore.write("\n")
    gitignore.write("# Add Streamlit secrets to .gitignore")
    gitignore.write("\n")
    gitignore.write(".streamlit/secrets.toml")
