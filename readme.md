# Cowponder

A simple terminal command that displays randomly selected philosophical thoughts from a cow

```
 ______________________________________
( squeezing an ounce of meaning out of )
( this world                           )
 --------------------------------------
        o   ^__^
         o  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## Installation

### OSX

If you already have homebrew installed, just run
```bash
brew install maxcai314/cowponder/cowponder
```
See the homebrew repo here: [homebrew-cowponder](https://github.com/maxcai314/homebrew-cowponder)

### Debian

Install the .deb package by running
`curl -s https://xz.ax/cowponder_debian_installer.sh | sudo bash`

Alternatively, download the [deb package file](https://xz.ax/cowponder_0.0.1-1_all.deb) and install it manually using `dpkg -i cowponder_<version>.deb`

### Windows

To install for powershell, run
```powershell
Install-Module cowponder
```
If, upon running `cowponder`, you get an error saying `running scripts is disabled on this system`, run one of these:
```powershell
# if you are running (or can run) powershell as administrator
Set-ExecutionPolicy RemoteSigned

# if you don't have administrator privileges
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
This allows scripts like cowponder to run if they are signed. [learn more here](https://go.microsoft.com/fwlink/?LinkID=135170).

## Usage

```
ponder     # displays a thought
cowponder  # displays a thought from a cow
```

### Dependencies

Debian systems:
* cowsay (auto installs if missing)
* python3 (auto installs if missing)
* dpkg
* apt

Windows systems:
* powershell which has been updated in the past two decades
