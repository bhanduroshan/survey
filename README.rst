survey
======

app to create survey

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create an AWS Ubuntu Machine using free tier account (Ubuntu 16.04 LTS) using key pair value


2. Create a New Security Group with inboud rules, that allows ssh from any ip and tcp request on port any port

3. Right click the ec2 instance and from networking, change security group and assign this security group

4. Connect to the machine using following command

    $ ssh -i <yourpemfile.pem> ubuntu@<ip_address>

5. Setup Up Docker on your machine using following commands

    $ sudo apt-get update

    $ sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

    $ sudo apt-get update

    $ sudo apt-get install docker-ce

    $ sudo apt-get install docker-compose

6. Go to your freenom account and edit the freenom dns record so as to point to your server ipaddress

7. Go to AWS account and create a publicly accessible s3 bucket and under acounts section create api keys

8. Go the repository and edit following files:
    a. envs > .production > .caddy ---> change the testptespt.tk domain to your domain name
    b. envs > .production > .django ---> change the DJANGO_ALLOWED_HOSTS testptespt.tk domain to your domain name


After the requirements are completed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Once you have completed docker installation, including docker and docker-compose, follow following instructions


Instructions
------------------------------------------

1. Clone the repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    $ git clone https://github.com/bhanduroshan/survey.git

2. Move to the survey directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    $ cd survey

3. Build the app
^^^^^^^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ sudo docker-compose -f production.yml  build


2. Make Migrations
^^^^^^^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ sudo docker-compose -f production.yml run django python manage.py makemigrations


3. Migrate the app
^^^^^^^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ sudo docker-compose -f production.yml run django python manage.py migrate


4. Set up Admin User
^^^^^^^^^^^^^^^^^^^^^^

* To create an **admin account**, use this command::

     $ sudo docker-compose -f production.yml run django python manage.py createsuperuser


5. Run the app
^^^^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ sudo nohup docker-compose -f production.yml  up --build


6. Access the app
^^^^^^^^^^^^^^^^

* Go to your browser and type: http://<ip_address>
* Enter into admin and then create:
    a. survey
    b. code


7. Accessing the survey
^^^^^^^^^^^^^^^^^^^^^

* Go to your browser and using the survey number and code you just created, type: http://<ip_address>/<survey_number>/<code>


8. Sample demo of the app
^^^^^^^^^^^^^^^^^^^^^

* Go to https://testptespt.tk/
