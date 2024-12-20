# Description
ChatPHP was created for a comprehensive examination of web application code security, when generated by Large Language Models and consists of 2,500 small dynamic PHP websites. These AI-generated sites are scanned for security vulnerabilities after being deployed as standalone websites in Docker containers. The evaluation of the websites was conducted using a hybrid methodology, incorporating the Burp Suite active scanner, static analysis, and manual checks.
Our investigation zeroes in on identifying and analyzing File Upload, SQL Injection, Stored XSS, and Reflected XSS.
We assembled a broad array of programming challenges. These challenges were designed to reflect the complexity and variety of scenarios a developer might typically present to an AI model for task resolution and cna been see in the functions.xt. These challenges include entries such as Create Language Learning Content, User Profile Editing with Audit Trail and so on. To further enrich the variety of responses—as each task is presented to the LLM several times—a website product and a website style category is included in the dynamic part of the prompt. The resulting PHP code is complemented with a database, which is de- ployed in a Docker container as a simple website

# Cite
https://arxiv.org/abs/2404.14459

# Instructions
## Launching the application

Download the Docker folder and the Creation/Sites, Creation/database folders

Each feature is working on it is own, it is possible to use them as it is by switching the index.php and the corresponfing init.sql files in each docker project folder.

## Copying index.php and init.sql files
To copy the desired index.php and init.sql files use the **copy_indexes.sh** script
```
chmod +x copy_indexes.sh
./copy_indexes.sh
```

Change the number according to which sites you would like to deploy. If you want to deploy sites from 2201-2300 chaneg the fileIndex and sqlIndex in the script:
```
# Initialize a counter for the index files starting from 1
fileIndex=2201

# Initialize a counter for the init.sql files starting from 1
sqlIndex=2201
```


## File upload settings

In order to use the file uplaod functions, www-data privileges msut be added to the uploads folder.

Add write privilege to the uplaods file manually:
```
chown -R www-data:www-data /home/debian/Test16/www/uploads/
```

Or use the upload **uplaods_folder.sh** script:
```
chmod +x uplaods_folder.sh
./uplaods_folder.sh
```

## Launch the docker
For manual launch use:
```
docker-compose up --build -d
```

For automated launch use the **start.sh** script and the **stop.sh** script to stop it:
```
chmod +x start.sh
./star.sh
```


