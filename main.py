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
    os.system("git checkout -b newbranch")
    for it in range(TIER):
        TextData = f'Iteration n°{it} of {TIER} \n\nCo-authored-by: {CO_AUTHOR} <{CO_AUTHOR_EMAIL}>'
        os.system(f'git commit --allow-empty -m "{TextData}"')	
    os.system('git push --set-upstream origin newbranch')
    os.system("git switch main")
    os.system("git branch --delete newbranch")


if __name__ == "__main__":
    main()
