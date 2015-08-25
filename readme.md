### Python3 Virtual Env

  * `mkdir ~/Envs/sds_vrfy`
  * `pyvenv ~/Envs/sds_vrfy`
  * and once you're in the directory where this project is, activate the virtual environment with: `source ~/Envs/sds_vrfy/bin/activate`

### Start the Database / Create a Table
* `pg_ctl start -D /usr/local/var/postgres`
* `psql -l`  //lists databases
* `createuser <username>`
* `createdb -O <username> <dbname>`

**Use these names in the settings file**



### (meeting with adam 6.4.15)
output from the test.py
likely include a tools or utils.py file for test.py to use
some message to the student
data.csv or json object that gives tango info like number of attempts and date submitted
data dump to the host server 

return something like results.txt with fields like score, feedback
to do: give adam and jim and eric a detailed desription of what needs to be in data.csv and results.txt 



------


### Running locally:
  * (if you don't have python3 installed, `brew install python3`. if you don't have homwebrew installed, do that.)
  * start postgres database should be something like `pg_ctl start -D /usr/local/var/postgres`, where `/usr/local/var/postgres` is the location of the database. 
  * In another tab/window `cd <vrfy-dir>` and start the virtual environment
  * `pip install -r requirements.txt` this command installs the python libs for this project 
  * `npm install` this command installs the node modules required for this project (if you don't have node installed `brew install node`)
  * `bower install` this command installs the bower components required for this project (if you don't have bower installed `npm install -g bower`)
  * `python3 manage.py collectstatic` this collects static files from the static folders and the bower_components directories (as per vrfy/settings.py).
  * if you're running this for the first time or have changed the models at all, make migrations (see below)
  * `grunt` this command creates the files & folder necessary (e.g course/static/course)
  * `python3 manage.py customdashboard vrfy/dashboard.py` creates a dashboard for grappelli.dashboard to use
  * `python3 manage.py gruntserver`  this is a *custom* command that integrates the task runner grunt with the traditional runserver command provided by django (see [https://lincolnloop.com/blog/simplifying-your-django-frontend-tasks-grunt/] if you're curious). Grunt compiles all .scss files into .css, concatenates all .js files and puts them into the /static/ subdirectory of the course app. Whenever a change is made to a .js file in course/js (and respectively, a .scss file in course/sass) grunt recompiles everything and the changes are reflected in the browser (at localhost:8000).  Of course, you can always use `python3 manage.py runserver`, which runs the server using localhost at port 8000. 

  * (Add `/admin` to see the admin interface (which is all there really is to see right now, since the authentication is hardcoded in for this development environment) if you add some problems & problem sets and go back to the home page you'll be able to see the problem sets and problems on the main page)

### Special Ubuntu instructions
  * When installing postgres, install PostgreSQL 9.4 using the [GUI installer](http://www.enterprisedb.com/products/pgdownload.do)
  * then create/modify the .bashrc (either for postgres user `/opt/PostgreSQL/9.4/.bashrc`, by default, or for all users `/etc/bash.bashrc`)
    * you can get the home folder for the postgres user by logging in to it (`sudo su - postgres`) and typing `pwd`
  * edit the PATH variable and add the bin folder in you postgres installation (default add `export PATH=/opt/PostgreSQL/9.4/bin:$PATH` to the .bashrc)
  * to start, log in to your postgres user (`sudo su - postgres`) and run `pg_ctl start -D /opt/PostgreSQL/9.4/data` (unless you specified a different data folder in the installer)
    * If it has any problems starting up, try running ``sudo kill -9 `ps -el | grep postgres | awk '{print $4}'` ``
  * Before installing `psycopg2`, (ie. before installing requirements.txt), install `libpq-dev` and `python-dev` using `sudo apt-get install`
  * Before you run grunt you need to run `sudo apt-get install nodejs-legacy`
  


### If there are migrations to make:
  * `python3 manage.py makemigrations <app_name>`
  * `python3 manage.py migrate`


### Testing via the admin interface
  * log in (create a superuser if you didn'd do that already)
  * any problems (and associated solution files) that are created will be added to the problem_assets folder (for more on the directory structure surrounding that, see solution_file_upload_path() and student_file_upload_path() in course/models.py)


### Create a user for the admin interface:
  * `python3 manage.py createsuperuser`

###Getting Tango to work
  * clone Tango to your machine (the dist_docker branch, commit `eb18878d49c0ca718fc994919ed08b92aa00a77b`, see [how to clone old commit](http://stackoverflow.com/questions/1655361/how-to-clone-an-old-git-commit-and-some-more-questions-about-git))
  * Follow [their instructions](https://github.com/autolab/Tango/wiki/Tango-with-Docker) for getting Tango running with docker
  * In `vrfy/settings.py` change `TANGO_ADDRESS` to the Tango server's address, `TANGO_KEY` to one of the keys for the server and `TANGO_COURSELAB_DIR` to the directory where Tango will store its courselabs
  * When you start the server you may want to use sudo, ie: `sudo python restful-tango/server.py` to make sure it has permission to edit the courselabs

### To get tango to work (if you don't have a linux machine):
  * (get help with docker)[https://docs.docker.com/installation/mac/#from-your-command-line]
  * `brew install boot2docker`
  * `boot2docker init`
  * `boot2docker start`
  * `eval "$(boot2docker shellinit)"`

Docker examples
Starts an niginx webserver, keeps the process running, publishes the ports, uses the files at the given path, and calls it mysite
`docker run -d -P -v $HOME/site:/usr/share/nginx/html --name mysite nginx`
`docker ps` //lists processes
`boot2docker ip` //boot2docker's ip
`docker pull ubuntu` //grab a linux distro

###Goals
make sure there's markdown support for the problem statements
