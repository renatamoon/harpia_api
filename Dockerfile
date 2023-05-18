# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Set environment variables
ENV HOST_POSTGRES=''
ENV PORT_POSTGRES=''
ENV DATABASE_POSTGRES=''
ENV USER_POSTGRES=''
ENV PASSWORD_POSTGRES=''


WORKDIR /harpia_api

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["flask", "--app", "main.py", "run", "--host", "0.0.0.0", "-p", "8000"]