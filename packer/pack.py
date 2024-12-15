import argparse
import json
import os


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='python3 -m pack -h',
        description='Pack directory (git repo) '
                    'into one single JSON Package.',
    )
    parser.add_argument(
        '-p', '--path', type=str,
        help='Path to directory (repo).',
        required=True,
    )
    parser.add_argument(
        '-o', '--output', type=str,
        help='Output file path.',
        default='./repo.json',
    )
    return parser.parse_args()


def pack(path: str, output: str, exclude: list | None = None):

    if not exclude:
        exclude = []

    exclude += ['.git', '__pycache__', 'venv', '.idea']

    data = {}
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, encoding='utf-8') as f:
                    relative_path = os.path.relpath(file_path, path)
                    data[relative_path] = f.read()
            except (UnicodeDecodeError, OSError):
                continue

    with open(output, 'w', encoding='utf-8') as fd:
        json.dump(data, fd, indent=2)


if __name__ == '__main__':
    args = get_args()
    pack(
        path=args.path,
        output=args.output,
    )
