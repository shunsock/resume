# check if virtual env exists
function check_status {
    if [ $? -eq 0 ]; then
        echo "[workflow] ✅ success! => $1"
    else
        echo "[workflow] 🚨 failed! =>  $1"
        exit 1
    fi
}

# --------------------------------
# Activate Virtual Env 
# --------------------------------
source env/bin/activate
check_status "virtual environment activated"


# --------------------------------
# Run Formatting
# --------------------------------
black update_data.py build.py src tests
check_status "formatting code by black"

isort update_data.py build.py src tests
check_status "formatting code by isort"

# --------------------------------
# Run Static Analysis
# --------------------------------
mypy update_data.py build.py
check_status "static analysis"


# --------------------------------
# Run Tests
# --------------------------------
pytest
check_status "tests"


# --------------------------------
# Build
# --------------------------------
echo "[workflow] Building..."
python update_data.py
python build.py
check_status "build"


# --------------------------------
# Deactivate Virtual Env
# --------------------------------
deactivate
check_status "virtual environment deactivated"

echo "[workflow] 🎉 Done! All Processes Completed Successfully! 🎉"
