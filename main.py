#!/usr/bin/env python
import os
from dotenv import load_dotenv


load_dotenv()

OWNER          = os.getenv('OWNER')
REPO           = os.getenv('REPO')
TIER           = int(os.getenv('TIER'))
CO_AUTHOR       = os.getenv('CO_AUTHOR')
CO_AUTHOR_EMAIL = os.getenv('CO_AUTHOR_EMAIL')

def main():
    for it in range(TIER):
        os.system(f"git checkout -b newbranch{it}of{TIER}")
        TextData = f'Iteration n°{it} of {TIER} \n\nCo-authored-by: {CO_AUTHOR} <{CO_AUTHOR_EMAIL}>'
        os.system(f'git commit --allow-empty -m "{TextData}"')	
        os.system('git push --set-upstream origin {it}of{TIER}')
        os.system("git switch main")


if __name__ == "__main__":
    main()
