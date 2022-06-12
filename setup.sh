sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-venv
while true; do
    read -p "Do you wish to setup up a vitual environment to install packages? (recommended) [Y/n] " yn
    case $yn in
        [Yy]* ) { 
                    python3 -m venv .env
                } || { 
                    python -m venv .env
                }; 
                source .env/bin/activate; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
pip install -r requirements.txt
cat > run.sh <<EOL
Directory=".env"
if [ -d "\$Directory" ];
then
	source .env/bin/activate
fi
streamlit run app.py
EOL
while true; do
    read -p "For better classification, download our Random Forest Model (3.2 GB) (recommended) [Y/n] " yn
    case $yn in
        [Yy]* ) wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1MTWGQinxfvbYmVzOYc4AGZO26kWE11xA' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1MTWGQinxfvbYmVzOYc4AGZO26kWE11xA" -O ML/rfc.pkl && rm -rf /tmp/cookies.txt;
                break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
chmod 755 run.sh