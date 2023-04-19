# Python script to be able to automatly create the first wiki page in Github.

# The script will:
* Navigate to github.com
* Log in to your account with:
    -username
    -github password
* Go into settings and uncheck botton "Restrict editing to collaborators only"
* Navigate to wiki-tab in main github window
* Find "create the first page"-tab and click it
* Find "save"-tab and click it.


Done!! Your wiki is now ready to go!

## Set up
# Create a virtual environment
Creating a Virtual Environment with WSL2 and Linux on Windows 11
1. Installing WSL2. Using the command line
* Open a command prompt as an Administrator and run the following line of code:
>wsl --install
2. Download Ubuntu
>wsl --list --online
* Choose the Ubunto version you want to install. Here we install Ubuntu-22.04
>wsl --install -d Ubuntu-22.04
* If you want to check which distros are installed in the WSL and what version of WSL they are running on you can check by typing:
>wsl -l -v
* install the latest updates by typing in the terminal:
>sudo apt update
>sudo apt full-upgrade
* To create the new python environment type this code in the Ubuntu terminal:
>python3 -m venv saras_venv (choose your venv name. Here its saras_venv)
* Activate your venv.
>source <venv>/bin/activate

# Install requirements
> pip3 install -r requirements.txt

# Run script
> python3 wiki_selenium_script.py

# After work is done
* Deactivate your venv
> deactivate
