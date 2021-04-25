

<div align="center" style="margin-bottom: 10px;">
    <img alt="Redis" src="https://img.shields.io/badge/storage-redis-red.svg?style=for-the-badge">
    <img alt="Python" src="https://img.shields.io/badge/python-3.7-informational.svg?style=for-the-badge">
    <img alt="Celery" src="https://img.shields.io/badge/multiprocessing-celery-green.svg?style=for-the-badge">
    <img alt="Flask" src="https://img.shields.io/badge/interface-flask-yellowgreen.svg?style=for-the-badge">
    <img alt="Node" src="https://img.shields.io/badge/node-12.x-brightgreen.svg?style=for-the-badge">
    <img alt="Angular" src="https://img.shields.io/badge/web%20framwork-angular%207-red.svg?style=for-the-badge">
</div>

<!--
<div align="center" style="margin-bottom: 10px;">
    <img alt="Boostrap" src="https://img.shields.io/badge/toolkit-boostrap-blueviolet.svg?style=for-the-badge">
    <img alt="UI Kit" src="https://img.shields.io/badge/UI%20Kit-Nebular-9cf.svg?style=for-the-badge">
</div>
-->



---

<div align="center">
    <img alt="Logo" src="https://i.pinimg.com/originals/69/25/dd/6925ddab4707f7867690983b3a562740.png">
</div>

---

<div align="center">   

[Description](#description)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Installation](#installation)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Website][website]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Modules](#modules)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Issues][issues]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Supporting](#sponsor)

</div>

---

<!--
Website References
-->
[website]:https://cyberkillerhere.blogspot.com/
[issues]:https://github.com/Rajkumar-kumawat/Swami-G/issues
[readmees]: README.es.md
[readmeen]: README.md

<h1 align="center">Swami-G </h1>

<h1 id="description">Description</h1>
Project Swami-G is a tool that collects information from an email and shows results in a nice visual interface.
just ask ...... !!!!!!


<div align="center">
    <a href="https://vimeo.com/434501702"><img src="https://kennbroorg.gitlab.io/ikyweb/assets/img/Giba.gif"></a>
</div>

[Video Demo](https://vimeo.com/434501702 "Video Demo - Click to Watch!")

<h2 id="modules">Modules</h2>

<div align="center" style="margin-bottom: 10px;">
    <img alt="fullcontact" src="https://img.shields.io/badge/module-fullcontact-blue.svg?style=flat-square">
    <img alt="twitter" src="https://img.shields.io/badge/module-twitter-blue.svg?style=flat-square">
    <img alt="linkedin" src="https://img.shields.io/badge/module-linkedin-blue.svg?style=flat-square">
    <img alt="github" src="https://img.shields.io/badge/module-github-blue.svg?style=flat-square">
    <img alt="keybase" src="https://img.shields.io/badge/module-keybase-blue.svg?style=flat-square">
    <img alt="ghostproject" src="https://img.shields.io/badge/module-ghostproject-red.svg?style=flat-square">
    <img alt="haveibeenpwned" src="https://img.shields.io/badge/module-haveibeenpwned-blue.svg?style=flat-square">
    <img alt="emailrep.io" src="https://img.shields.io/badge/amodule-emailrep.io-blue.svg?style=flat-square">
    <img alt="socialscan" src="https://img.shields.io/badge/module-socialscan-blue.svg?style=flat-square">
    <img alt="instagram" src="https://img.shields.io/badge/module-instagram-blue.svg?style=flat-square">
    <img alt="tiktok" src="https://img.shields.io/badge/module-tiktok-blue.svg?style=flat-square">
    <img alt="sherlock" src="https://img.shields.io/badge/module-sherlock-blue.svg?style=flat-square">
    <img alt="skype" src="https://img.shields.io/badge/module-skype-blue.svg?style=flat-square">
    <img alt="tinder" src="https://img.shields.io/badge/module-tinder-blue.svg?style=flat-square">
    <img alt="venmo" src="https://img.shields.io/badge/module-venmo-blue.svg?style=flat-square">
    <img alt="darkpass" src="https://img.shields.io/badge/module-darkpass-blue.svg?style=flat-square">
    <img alt="tweetiment" src="https://img.shields.io/badge/module-tweetiment-blue.svg?style=flat-square">
    <img alt="peopledatalabs" src="https://img.shields.io/badge/module-peopledatalabs-blue.svg?style=flat-square">
    <img alt="reddit" src="https://img.shields.io/badge/module-reddit-blue.svg?style=flat-square">
    <img alt="leaklookup" src="https://img.shields.io/badge/module-leaklookup-blue.svg?style=flat-square">
    <img alt="twint" src="https://img.shields.io/badge/module-twint-blue.svg?style=flat-square">
    <img alt="holehe" src="https://img.shields.io/badge/module-holehe-blue.svg?style=flat-square">
    <img alt="spotify" src="https://img.shields.io/badge/module-spotify-blue.svg?style=flat-square">
    <img alt="twitch" src="https://img.shields.io/badge/module-twitch-blue.svg?style=flat-square">
</div>

<h1 id="installation">Installation</h1>

<div align="left" style="margin-bottom: 10px;">
    <h2><img alt="important" height="30" src="https://kennbroorg.gitlab.io/ikyweb/assets/img/important.png"> Installation </h2>
</div>

## Full installation 

### Install Backend

#### Redis

You must install Redis

```shell
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
make test
sudo make install

```

### open another terminal and Clone repository !!

```shell
https://github.com/Rajkumar-kumawat/Swami-G.git
```

#### Python stuff and Celery

You must install the libraries inside requirements.txt

```shell
cd Swami-G
python3 -m pip install -r requirements.txt
```

### Install Frontend

#### Node
```
sudo apt install nodejs
OR
sudo apt install nodejs npm
```
 OR First of all, install [nodejs](https://nodejs.org/en/).

#### Dependencies

Inside the directory **frontend** install the dependencies

```shell
cd frontend
npm install

```

## Wake up  Swami-G Tool

### Turn on Backend

#### Redis

Turn on the server in a terminal

```shell
redis-server
```

#### Python stuff and Celery

Turn on Celery in another terminal, within the directory **backend**

```shell
./celery.sh
```

Again, in another terminal turn on backend app from directory **backend** 

```shell
python3 app.py
```

### Turn on Frontend

Finally, to run frontend server, execute the following command from directory **frontend**

```shell
npm start
```

<!--
### Screen after turn on Swami-G


-->

<h3 id="browser">Browse</h3>

Open the browser in this [url](http://127.0.0.1:4200) 

### Config API Keys

Once the application is loaded in the browser, you should go to the Api Keys option and load the values of the APIs that are needed.

- Fullcontact: Generate the APIs from [here](https://support.fullcontact.com/hc/en-us/articles/115003415888-Getting-Started-FullContact-v2-APIs)
- PeopleDataLabs : Generate the APIs from [aquí](https://www.peopledatalabs.com/signup)
- Linkedin: Only the user and password of your account must be loaded
- Instagram: Only the user and password of your account must be loaded
- HaveIBeenPwned : Generate the APIs from [here](https://haveibeenpwned.com/API/Key) (Paid)
- Emailrep.io : Generate the APIs from [here](https://emailrep.io/key)
- Leaklookup : Generate the APIs from [here](https://leak-lookup.com/api)
- Twitter: Generate the APIs from [here](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)
- Spotify: Generate the APIs from [here](https://developer.spotify.com/dashboard/applications)
- Twitch: Generate the APIs from [here](https://dev.twitch.tv/docs/api/)




## Demo Video

<div align="center">
    <a href="https://vimeo.com/434501702"><img alt="Kali 2019" src="https://kennbroorg.gitlab.io/ikyweb/assets/img/iKy-01.png"></a>
    <p>Vimeo</p>
</div>



# Disclaimer
Anyone who contributes or contributed to the project, Most Welcome in Swami-G world.

Keep in mind that this software was Combine of lots of Tool , I Did not code much inside , In this Tool ,I have combine a lot of OSINT Research tools which are available on internet too. then for educational purposes , and now the goal is to collaborate with the me and  making quality free software, and while the quality is not excellent (sometimes it's not even good) we strive to pursue excellence.

Consider that all the information collected is free and available online, the tool only tries to discover, collect and display it. Many times the tool cannot even achieve its goal of discovery and collection. Please load the necessary APIs


Do not use the tool if you cannot read the instructions and / or this disclaimer clearly.


Rajkumar-Kumawat
