echo 'deb [arch=all] https://xz.ax/cowponder-apt-repo stable main' >> /etc/apt/sources.list/cowponder.list
apt-get update --allow-insecure-repositories
echo 'successfuly configured apt to install cowponder from https://xz.ax/cowponder-apt-repo'
echo 'now run apt-get install cowponder to complete installation.'
