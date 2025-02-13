FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "init_page.py", "--server.port=8501", "--server.address=0.0.0.0"]
