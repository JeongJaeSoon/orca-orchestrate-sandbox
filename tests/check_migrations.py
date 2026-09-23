"""Fail when migration numbers are not contiguous from 0001."""
import pathlib, re, sys

nums = sorted(int(m.group(1)) for p in pathlib.Path("migrations").glob("*.sql") if (m := re.match(r"(\d{4})_", p.name)))
if nums != list(range(1, len(nums) + 1)):
    sys.exit(f"migration numbers not contiguous: {nums}")
print(f"{len(nums)} migrations ok")
