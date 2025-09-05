# 2508_DS5111_epx8hh
Repo for DS5111 Automation and Data Pipeline with Automation

### Setting up generic bootstrap sequence
*A new VM should have >sudo apt update< run manually, do this right in the VM, later the init.sh file will be run to apply this among other package updates.*
Git credentials should be setup via the settings and by following the https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent instructions.
  A few things you will need to do:
    Navigate to github settings and SSH & GPG keys page. Now navigate back to your command line.
    Follow the https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key instructions. This should be done from your root directory in your linux command.
      Enter >ssh-keygen -t ed25519 -C "your_email_id@example.com"< with your email from your github account.
      If you do not want a password just press enter without typing anything in (this password is required for every git action).
        In order to access github from anywhere in your directories, enter your .ssh root directory, create a config file with >nano config< and provide this inside the file 
          #
          Host github.com
              HostName github.com
              User git
              IdentityFile ~/.ssh/id_ed25519
              IdentitiesOnly Yes
          #
  Run >cat id_ed25519.pub< to see the provided ssh key, copy this key, navigate back to github, create new ssh key, provide a terse title, and paste the key into the 'key' box. Finally add the key.
  Back in the command line, test connection with >ssh -T git@gtihub.com< and /type >yes< to add git@github.com to be added to the permanent list of known hosts. **Your github handle should appear**
At this point your github account and your directory should be linked and authenticated.

### Repo
Create a new repo (make sure you are in the pwd you want to be in) by cloning this repo with >git clone git@github.com:Lcocks/2508_DS5111_epx8hh.git< command scripts.
  If you want to remove the remote origin control (make your clone independent) then >cd repo-name< then >git remote remove origin<, create a new repo in your github account, then >git remote add origin git@github.com:yourusername/new-repo-name.git<. Finally push the change with >git push -u origin main<.
Run the init.sh file with >bash init.sh<. Your packages should be up to date with some others installed.
