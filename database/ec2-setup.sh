before_reboot(){
    sudo amazon-linux-extras install docker -y
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    sudo chkconfig docker on
    sudo yum install -y git
    sudo reboot
}

after_reboot(){
    sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose version
    git clone https://github.com/augustoaccorsi/microservices.git
    cd microservices
    docker-compose -f docker-compose-db.yml up --build --detach
}

if [ -f /var/run/rebooting-for-updates ]; then
    after_reboot
    rm /var/run/rebooting-for-updates
    update-rc.d myupdate remove
else
    before_reboot
    touch /var/run/rebooting-for-updates
    update-rc.d myupdate defaults
    sudo reboot
fi