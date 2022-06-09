Directory=".env"
if [ -d "$Directory" ];
then
	source .env/bin/activate
fi
streamlit run app.py
