import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()

# A note from a second pass: the excuse itself lives in entry.txt,
# and this file only carries it across. Keeping the copier plain is
# deliberate — any rendering or rewriting here could change the exact
# words the judge is meant to read, and the words are the whole entry.
