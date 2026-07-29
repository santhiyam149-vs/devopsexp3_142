from pathlib import Path
import sys

# Required files
required_files = ["index.html", "style.css", "script.js"]

all_ok = True

print("Checking project files...\\n")

for filename in required_files:
    file_path = Path(filename)

    # Check if file exists
    if not file_path.exists():
        print(f"❌ {filename} is MISSING")
        all_ok = False
        continue

    print(f"✅ {filename} exists")

    # Check if file is empty
    content = file_path.read_text(encoding="utf-8").strip()

    if len(content) == 0:
        print(f"❌ {filename} is EMPTY")
        all_ok = False
    else:
        print(f"✅ {filename} is NOT empty ({len(content)} characters)")

    # Additional validation
    if filename == "index.html" and "<html" not in content.lower():
        print("⚠️ index.html does not contain an <html> tag")

    if filename == "style.css" and "{" not in content:
        print("⚠️ style.css may not contain CSS rules")

    if filename == "script.js" and len(content) < 5:
        print("⚠️ script.js content is very small")

    print()

# Final result
if not all_ok:
    print("❌ Verification FAILED")
    sys.exit(1)
else:
    print("🎉 All required files are present and non-empty")