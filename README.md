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


## Setting up generic bootstrap sequence

This repo will have the "scripts" directory, "makefile", and "requirements.txt" that are required to start.

Navigate to the "init_git_creds.sh" file and `nano init_git_creds.sh` and update the NAME and USER to your own account for github. 

Navigate to "scripts", make "init.sh" and "init_git_creds.sh" executable by running `chmod +x init.sh` & `chmod +x init_git_creds.sh`.

Then run the script with `bash init.sh` then run `bash init_git_creds.sh` from which you should see your email and user name echoed.

If all went well, you should be able to execute `tree` and instead of an error see the name of the init.sh script.

Navigate out of scripts and test makefile is working so type `make` which should refelct the contents of the file. `make update` will run the update section of the makefile and the requirements.txt file.

Finally check the python environment is working use `. env/bin/activate`, this activates the new virtual environment, you should see an (env) on the left of the prompt.

   Now type `pip list` and you should see pandas and numpy listed to the console as installed packages.

Feel free to git add, commit, and push to ensure everything is updated accordingly and in sync.


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

### Additional Resources

- [Resource 1](url): Brief description

### Troubleshooting

**Common Issue 1**
- Solution or notes

### Notes

- You can do a `git log` to verify the commit is done, also `git status` should let you know everything is up to date.
