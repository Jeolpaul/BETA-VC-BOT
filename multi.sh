if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Jeolpaul/YukkiMusicBot /YukkiMusicBot     
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /YukkiMusicBot
fi
cd /YukkiMusicBot
pip3 install -U -r requirements.txt
echo "BOT IS STARTING⚡️⚡️⚡️"
python3 -m YukkiMusic
