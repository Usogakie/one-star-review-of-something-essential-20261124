import os

REVIEW = "Gravity has never caught a single thing I have dropped, yet it has never once missed the floor."

# The gate allows 1 to 160 characters; fail loudly instead of shipping an invalid entry.
assert 1 <= len(REVIEW) <= 160, "review outside the 1-160 character gate"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)

if __name__ == "__main__":
    main()
