
#!/bin/bash
echo "This script may possibly need restart the system"
echo "Please rerun this script after a potential restart to finish deployment"
FILE=./linux.zip
RUNTIME=$(grep -oP '(?<=RUNTIME=).*' .env)
if [ ! -f "$FILE" ]; then
  sudo apt install curl
  sudo apt install unzip
  curl -L https://github.com/amboltio/emily-cli/releases/download/Release-v0.1.3/linux.zip -O
  unzip linux.zip
  if [ "$RUNTIME" = "nvidia" ]; then
    ./linux/emily doctor fix -r docker docker-compose nvidia-docker nvidia-driver
  else
    ./linux/emily doctor fix -r docker docker-compose
  fi
fi
rm -f linux.zip
rm -rf linux

docker-compose --env-file .env -f docker-compose.prod.yml up -d
