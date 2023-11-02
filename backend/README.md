

## Getting Started for Development

### 1. Install Python(3.11)

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

###  2. Fork this repo.
Read more... [How to fork a github repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

### 3. Clone the fork to your local machine
Read more... [How to clone a github repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

```bash
$ git clone https://github.com/yourusername/Open-source.git
```

### 4. Set up virtual environment and install dependencies with pipenv
Read more... [Prefered installation of pipenv](https://pipenv.pypa.io/en/latest/installation/#preferred-installation-of-pipenv)

#### Navigate to the project backend folder and follow the steps below

- Install pipenv
    1. using pip
    ```bash
    $ pip install pipenv
    ```
    2. using homebrew
    ```bash
    $ brew install pipenv
    ```
- Install Dependencies
    ```bash
    $ pipenv install # pipenv will create a new virtual environment and then install all dependencies in the Pipfile
    ```
- Activate the New env and Start Coding
    ```bash
    $ pipenv shell
    ```
    if using vscode

    ```bash
    $ code .
    ```

    to uninstall the environment created, within the same directory run
    ```bash
    $ pipenv --rm
    ```
