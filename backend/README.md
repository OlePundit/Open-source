

## Getting Started 

### 1 Install Python 


- Debian/Ubuntu
     Install using [apt-get](https://linux.die.net/man/8/apt-get).
     Install using [apt-get](https://linux.die.net/man/8/apt-get).
    
    Install using [apt-get](https://linux.die.net/man/8/apt-get).
    
        $ sudo apt-get update
        $ sudo apt-get install python3       
        


+   - macOS
    1. Install [Brew](https://brew.sh). 
    2. Install Python using Brew:
        ```sh
        $ brew install python3
        ```
    3. Make your the Brew executables `bin` directory is in your `PATH` variable.
- Windows
    1. Download Python from the [Windows Download](https://www.python.org/downloads/windows/) page.
    2. Run the installer.
        - Be sure to _check_ the box on to have Python added to your `PATH` if the installer offers such an option (it's normally off by default).

For more details, see this gist - [Set up a Python 3 virtual environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).

### 2 Clone this repo in your local machine

```bash
    https://github.com/yourusername/Open-source.git
```

### 3 Set up virtual environment

#### Navigate to the project directory and follow the steps below

- Debian/Ubuntu
 1. Install virtual environment

    ```bash
    pip install virtualenv
    ```
2. name your virtual environent 
    ```bash
   python -m venv environment_name
    ```
3. Activate

    ```bash
    source environmentname/bin/activate
    ```
### Install Django
On your project root dir type the following command

```bash
pip install django
```
