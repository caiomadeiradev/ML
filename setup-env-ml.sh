REQUIRED_PACKAGES="numpy pandas matplotlib seaborn jupyter python-dotenv"
ML_PACKAGES="scikit-learn"

echo "[1] Checking python version..."
python_v=$(python3 --version)

if [[ "${python_v:7:1}" == 3 && "${python_v:9:1}" == 1 && "${python_v:10:1}" == 0 ]]; then
    echo "  [+] Python is in correctly version."
    echo "  [+] Actual version: $(python3 --version)"
else
    echo "  [x] wrong python version"
    sudo apt update
    sudo apt install software-properties-common -y
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.10 python3.10-venv python3.10-dev
    python3 --version
fi

echo "======================================================="
echo "[2] Checking virtual enviroment..."

if pip show virtualenv > /dev/null 2>&1; then
    echo "  [+] python virtualenv package is already installed."
else
    echo "  [x] python virtualenv package is NOT installed. Installing"
    pip install virtualenv
fi

file_str=$(ls -a)
if [[ $file_str =~ "venv" || $file_str =~ "env" ]]; then
    echo "  [+] Virtual env is already created."
    source venv/bin/activate
else
    echo "  [x] Virtual env NOT exists."
    python3 -m venv venv
    source venv/bin/activate
fi

echo "======================================================="
echo "[3] Installing dependencies..."
req_file=$(ls -a)

if [[ $req_file =~ "requirements.txt" ]]; then
    echo "  [+] requirements.txt exists. Preparing to install it..."
    pip install -r requirements.txt
else
    echo "  [!] requirements.txt not found. Installing packages manually..."
    pip install $REQUIRED_PACKAGES
    pip install $ML_PACKAGES

    echo "  [+] Generating requirements.txt"
    pip freeze > requirements.txt
fi