# DONT CHANGE THESE CODES⚠️⚠️
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Jeolpaul/MUSICBYPASS /MUSICBYPASS
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MUSICBYPASS
fi
cd /MUSICBYPASS
pip3 install -U -r requirements.txt
echo "BOT IS STARTING"
python3 -m 
