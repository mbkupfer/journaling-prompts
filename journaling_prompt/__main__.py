import argparse
from random import choice
from pathlib import Path

PROMPTS = Path(__file__).parent / 'prompts.txt'


def main(num_choices):
    with open(PROMPTS, 'rt') as fp:
        prompts = fp.readlines()
        res = set()
        while len(res) < num_choices and len(res) < len(prompts):
            res.update({choice(prompts)})
    for i, prompt in enumerate(res, start=1):
        print('%s: %s' % (i, prompt))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--count', default=1, type=int, help='prompts options to return (default: 1)'
    )

    args = parser.parse_args()

    main(args.count)
