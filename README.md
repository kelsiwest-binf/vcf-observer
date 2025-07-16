# VCF Observer

VCF Observer is a web tool that performs [VCF](https://en.wikipedia.org/wiki/Variant_Call_Format) file analysis, comparison, and visualization.

![Screenshot of the VCF Observer user interface displaying a Venn diagram.](screenshot.png)

## Installation
This version uses a dockerfile to control dependencies across different systems. 

1. Build vcfobserver docker image by running the following code inside the vcf-observer directory:

    `docker build -t vcfobserver --file Dockerfile .`

    This command builds a Docker image from a Dockerfile.

*Breakdown:*  
`docker build`	Command to build a Docker image.  
`-t vcfobserver`	Tags the image with the name vcfobserver. This makes it easier to refer to later when running containers.  
`--file Dockerfile`	Specifies the name of the Dockerfile to use. The default is Dockerfile, but here it's explicitly named Dockerfile.  
`.`	The build context, meaning Docker will use the current directory (.) and its contents during the build.  

You're creating an image called vcfobserver based on instructions in the DockerFile, using the files in the current directory as input.

2. Run the docker container and launch vcfobserver page by running the following code:

    `docker run -it --rm -p 8050:8050 -v .:/vcf-observer -w /vcf-observer/app vcfobserver python app.py`

    Click the hyperlink in `App running at: http://127.0.0.1:8050` and that will launch the vcfobserver page.

*Breakdown:*
`docker run`	Starts a new container.  
`-it`	Interactive terminal mode: -i keeps STDIN open, -t allocates a pseudo-TTY (lets you use a shell interactively).  
`--rm`	Automatically removes the container when you exit. Helps keep your system clean.  
`-p 8050:8050`	Maps port 8050 on your host to port 8050 in the container. Useful if the app runs a server (like a web app) on that port.  
`-v .:/vcf-observer`	Mounts the current directory (host) into the container at /vcfobserver. This allows the container to access your source code or data.  
`-w /vcf-observer/app`	Sets the working directory inside the container. When the container starts, you'll be placed in this directory.  
`vcfobserver`	Specifies the image to use (the one built earlier).  
`python app.py`	 Command to execute within the docker container to launch the vcfobserver app.  


### For Additional Development Needs

3. After running the docker build step (#1 above), run vcf-observer inside the docker container by running the following code:

    `docker run -it --rm   -p 8050:8050   -v .:/vcf-observer   -w /vcf-observer/app   vcfobserver   /bin/bash`
     
    This runs the container based on the vcfobserver image and gives you an interactive terminal inside it.

*Breakdown:*  
`docker run`	Starts a new container.  
`-it`	Interactive terminal mode: -i keeps STDIN open, -t allocates a pseudo-TTY (lets you use a shell interactively).  
`--rm`	Automatically removes the container when you exit. Helps keep your system clean.  
`-p 8050:8050`	Maps port 8050 on your host to port 8050 in the container. Useful if the app runs a server (like a web app) on that port.  
`-v .:/vcf-observer`	Mounts the current directory (host) into the container at /vcfobserver. This allows the container to access your source code or data.  
`-w /vcf-observer/app`	Sets the working directory inside the container. When the container starts, you'll be placed in this directory.  
`vcfobserver`	Specifies the image to use (the one built earlier).  
`/bin/bash`	Runs the Bash shell in the container so you can interact manually.  

