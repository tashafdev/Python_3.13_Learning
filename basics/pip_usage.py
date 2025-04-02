"""
pip_usage.py

🔰 Purpose:
This file explains how to use pip (Python's package installer).

👩‍💻 Created for personal Python 3.13 learning

📘 What is pip?
PIP stands for "Pip Installs Packages".
It is used to install and manage external Python libraries and dependencies.

📘 Common pip Commands:
------------------------------------------------
✅ Install a package:
pip install package_name

✅ Install a specific version:
pip install package_name==1.2.3

✅ Upgrade a package:
pip install --upgrade package_name

✅ Uninstall a package:
pip uninstall package_name

✅ List installed packages:
pip list

✅ Show package details:
pip show package_name

✅ Freeze installed packages (for requirements.txt):
pip freeze > requirements.txt

✅ Install from requirements.txt:
pip install -r requirements.txt

📘 Bonus Tip:
If you're using virtual environments (recommended):
- Create: python -m venv env
- Activate:
    Windows → env\\Scripts\\activate
    Mac/Linux → source env/bin/activate
"""

# ⚠️ pip is a terminal/command-line tool, not run inside Python code.

# ✅ However, you can check installed packages using code:
import pkg_resources

print("🔍 Installed Packages (Top 5):")
for pkg in list(pkg_resources.working_set)[:5]:
    print(f"{pkg.project_name} - {pkg.version}")

# ✅ You can also use subprocess to install (⚠️ use with care)
# import subprocess
# subprocess.check_call(["pip", "install", "requests"])
# print("✅ 'requests' library installed via script")
