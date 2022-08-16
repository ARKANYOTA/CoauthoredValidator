# CoauthoredValidator
Permet de automatiquement débloquer le Coauthored Achievement

## requirement
- python

## Comment Faire

- [Fork this repo with Main user Account](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)  (*Not the octocat/Spoon-Knife repo*)
- [Get USERNAME and EMAIL of Coauthored](https://www.sourcecon.com/how-to-find-almost-any-github-users-email-address)
- [Setup ssh or github token](https://blog.corsego.com/aws-cloud9-github-sshoken)
- Execte this with terminal
```
git clone https://github.com/<YOUR USERNAME>/CoauthoredValidator
cd CoauthoredValidator
cp .env.structure .env
```


- Modify Varibale of .env file (He is hidden by default)
	- OWNER(optional): Userame of Main User Account
	- REPO(optional): Name of the forked repository, Normally "GalaxyBrainValidator"
	- TIER: 1 (NoLevel x1: 1, Bronze x2:10, Argent x3: 24, Gold x4: 48)
	- CO_AUTOR: The user has also Coauthored
	- CO_AUTOR_EMAIL: The email of user

- execute program in same folder
```py
python main.py
```


