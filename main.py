#!/usr/bin/env python
import os
from dotenv import load_dotenv

load_dotenv()

OWNER          = os.getenv('OWNER')
REPO           = os.getenv('REPO')
TIER           = os.getenv('TIER')
CO_AUTOR       = os.getenv('CO_AUTOR')
CO_AUTOR_EMAIL = os.getenv('CO_AUTOR_EMAIL')

def main():
    for it in range(TIER):
        TextData = f'Iteration n°{it} of {TIER} \n\nCo-authored-by: {CO_AUTHOR} <{CO_AUTHOR_EMAIL}>'
        os.system(f'git commit --allow-empty -m "{TextData}"')	
    os.system('git push')


if __name__ == "__main__":
    main()
