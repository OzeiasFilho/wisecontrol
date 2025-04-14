FROM python:3.11

ENV PIPENV_VENV_IN_PROJECT=1

WORKDIR /app 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Verificar a instalação do Django
RUN python -m django --version

COPY . .

RUN useradd -ms /bin/bash appuser
USER appuser

# CMD ["gunicorn", "-b", "0.0.0.0:8000", "meu_projeto.wsgi:application"]
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]