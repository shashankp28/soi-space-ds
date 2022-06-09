sudo apt-get update
sudo apt-get upgrade
while true; do
    read -p "Do you wish to setup up a vitual environment to install packages?" yn
    case $yn in
        [Yy]* ) python3 -m venv .env && source .env/bin/activate; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done
pip install -r requirements.txt
streamlit run app.py
