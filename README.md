# 2508_DS5111_epx8hh
Repo for DS5111 Automation and Data Pipeline with Automation

#### *Preconditions**

1. This is based on Amazon AWS EC2 with a created instance. Please ensure this is already present (this will serve as our virtual ubuntu linux machine).

2. Please have a github key already established inside the Virtual Machine. If not see Appendix A. 


## Repo

Create a new repo (make sure you are in the pwd you want to be in) by cloning this repo with `git clone git@github.com:Lcocks/2508_DS5111_epx8hh.git` command scripts.

   If you want to remove the remote origin control (make your clone independent) then:
   1. `cd repo-name` 
   2. `git remote remove origin`
   3. Create a new repo in your GitHub account
   4. `git remote add origin git@github.com:yourusername/new-repo-name.git`
   5. Finally push the change with `git push -u origin main`

Run the init.sh file with `bash init.sh`. Your packages should be up to date with some others installed.


## Setting up generic bootstrap sequence (from your VM)

This repo will have the "scripts" directory, "makefile", and "requirements.txt" that are required to start.

Navigate to the "init_git_creds.sh" file and `nano init_git_creds.sh` and update the NAME and USER to your own account for github. 

Navigate to "scripts", make "init.sh" and "init_git_creds.sh" executable by running `chmod +x init.sh` & `chmod +x init_git_creds.sh`.

Then run the script with `bash init.sh` then run `bash init_git_creds.sh` from which you should see your email and user name echoed.

If all went well, you should be able to execute `tree` and instead of an error see the name of the init.sh script.

Navigate out of scripts and test makefile is working so type `make` which should refelct the contents of the file. `make update` will run the update section of the makefile and the requirements.txt file.

Finally check the python environment is working use `. env/bin/activate`, this activates the new virtual environment, you should see an (env) on the left of the prompt.

   Now type `pip list` and you should see pandas and numpy listed to the console as installed packages.

Feel free to git add, commit, and push to ensure everything is updated accordingly and in sync.

STEP 2:

We want to work from a new branch so at this point we will make a new branch from the root with `git checkout -b m02_normalizer`. We will be working from this branch for the next steps.

	Now use `git push` to activate the branch. You can always check your branch on the github web UI.

Within your repository you will have a scripts folder, in which 'install_chrome_headless.sh' will reside. Feel free to review the file with cat, vim, or nano.
	
	Run the script with `bash install_chrome_headless.sh` 
	
	If all went well, you should see some text near the bottom that says <h1>Example Domain</h1>. This means it was able to download the html from example.com

Now navigate to the root of your repo and enter the '.gitignore' file. In here you will go to the very end of the file, add a few lines and instert `**/*.deb` to instruct git to ignore the deb file type.

Finally give your repo a check with `git status`, add, commit (with sufficient info), and push.

STEP 3: 

From your repo root `cat requirements.txt` in order to verify you have all the neccessary packages like beautifulsoup4, lxml and html5lib. 

Also check your 'makefile' and verify it includes the ygainers.html and wsjgainers.html jobs. If you so you then `make update` to ensure your make if up to date, `. env/bin/activate` to start your virtual environment kernel, and run `make wsjgainers.csv` and `make ygainers.csv` respectively.

	You will know the jobs correctly ran when there is a .csv file of each name in your directory and it will display something like this:

	,Unnamed: 0,Volume,Last,Chg,% Chg
	0,QMMM Holdings Ltd. Cl A (QMMM),14.8M,207.0,195.73,1736.73
	1,Epsium Enterprise Ltd. (EPSM),665.3K,138.0,111.02,411.49
	2,CaliberCos Inc. (CWD),133.4M,9.11,6.96,323.72
	3,Kindly MD Inc. (NAKA),15.9M,8.08,3.52,77.19
	4,Pitanium Ltd. (PTNM),26.8M,4.53,1.79,65.33

Now following the same logic as before, edit the '.gitignore' file to disregard the .csv and .html files types. 

After this is complete you can add, commit, and push to the new branch(which should display with `git branch`).

Step 4:

Navigate to the root directory of the repo, `cd` into the `bin/` directory and review the `my_normalizer.py` file with `cat my_normalizer.py`.

	This should contain 2 function for each of the csv files from Yahoo and WSJ. Feel free to run the script by exiting the file and (with your environment active) run `python3 my_normalizer.py`. 2 files should be created and within those normalized stock data should display.

There should be no need to update git as nothing has changed (since we ran the python script, the created files are .csv and therefore ignored by git since our `.git/ignore` updates).

Step 5: Setting Up Testing

Requirements.txt will have `pylint` and `pytest`, to test run pylint use `pylint bin/my_normalizer.py` and a score should display to indicate a working command.

The `tests` directory will have several tests including `test_testsmoke.py`, to test this package you can run the file directly in your env. All tests should PASS.

`pylintrc` will be present in the root directory as well which gives the conditions for how pylint conducts its testing (standards). The makefile should have `lint` job and `test` jobs which will run consecutively with `make test`.

`testing.py` is a python file to test simple functions, feel free to use as necessary to test before making final adjustments to a full `test_...` file.

After confirming all the working packages, files, and commands you should be good. Unless a change was made no reason to commit to git.

Step 6: Getting validations.yml and basic.yml setup

The `.github/workflows` folder was created as a hidden directory, this also serves as the base of the github actions (workflows). 

In this you will find 2 file names including `validations.yml` & `basic.yml` of which have several jobs. When pushing you will see under the github actions tab in github,
	a either successfully run or failed actions (this should in include the 2 file names mentioned above for a push).

The success of a passing action can be captued as a 'badge' and displayed (commonly in your README): please see Appendix A - Badge for Successful Testing.


## Appendix A

### Setting up Github Keys

*A new VM should have `sudo apt update` run manually, do this right in the VM, later the init.sh file will be run to apply this among other package updates.*

Git credentials should be setup via the settings and by following the [GitHub SSH key instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

### A few things you will need to do:

1. Navigate to GitHub settings and SSH & GPG keys page. Now navigate back to your command line.

2. Follow the [generating a new SSH key instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key). This should be done from your root directory in your linux command.
   
   - Enter `ssh-keygen -t ed25519 -C "your_email_id@example.com"` with your email from your GitHub account.
   
   - If you do not want a password just press enter without typing anything in (this password is required for every git action).

3. In order to access GitHub from anywhere in your directories, enter your .ssh root directory, create a config file with `nano config` and provide this inside the file:
   
   ```
   Host github.com
       HostName github.com
       User git
       IdentityFile ~/.ssh/id_ed25519
       IdentitiesOnly Yes
   ```

4. Run `cat id_ed25519.pub` to see the provided SSH key, copy this key, navigate back to GitHub, create new SSH key, provide a terse title, and paste the key into the 'key' box. Finally add the key.

5. Back in the command line, test connection with `ssh -T git@github.com` and type `yes` to add git@github.com to be added to the permanent list of known hosts. **Your GitHub handle should appear**

At this point your GitHub account and your directory should be linked and authenticated.

### Badge for Successful Testing

1. [![Feature Validation](https://github.com/Lcocks/2508_DS5111_epx8hh/actions/workflows/validations.yml/badge.svg)](https://github.com/Lcocks/2508_DS5111_epx8hh/actions/workflows/validations.yml)
2. [![CI](https://github.com/Lcocks/2508_DS5111_epx8hh/actions/workflows/basic.yml/badge.svg?branch=patch-1)](https://github.com/Lcocks/2508_DS5111_epx8hh/actions/workflows/basic.yml)


   

### Additional Resources

- [Resource 1](url): Brief description

### Troubleshooting

**Common Issue 1**
- Solution or notes

### Notes

- You can do a `git log` to verify the commit is done, also `git status` should let you know everything is up to date.
