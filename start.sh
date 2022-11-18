
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/PRIYA-OS/TELETHON.git /TELETHON
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /TELETHON
fi
cd /TELETHON
pip3 install -U -r requirements.txt
echo "Starting THANOS...."
python3 bot.py
