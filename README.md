# ikusel (📷💻📊)

Simple web-based tool that lets users upload an image and convert it to an Excel spreadsheet (.xlsx) file!

## Getting Started

* Clone the repository
```bash
git clone git@github.com:Kawaeee/ikusel.git
cd ikusel/
```

* Install necessary dependencies
```bash
pip install -r requirements.txt
```

* Run the streamlit
```bash
streamlit run main.py
```
> Streamlit web application will be hosted on http://localhost:8501

* Serve Docker container
```bash
# Directly build and run
docker build -t ikusel-app-image .
docker run --rm --name=ikusel-app-container -p 0.0.0.0:8501:8501 ikusel-app-image

# Serve with docker compose
docker-compose build
docker-compose up
```