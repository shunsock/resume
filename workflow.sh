echo "[workflow] Activating virtual environment..."
source env/bin/activate
echo "[workflow] ✅ virtual environment activated"

echo "[workflow] Formatting..."
black update_data.py build.py src tests
echo "[workflow] ✅ formatted"
isort update_data.py build.py src tests
echo "[workflow] ✅ sorted imports"

echo "[workflow] Running static analyser..."
mypy update_data.py build.py
echo "[workflow] ✅ static analysis passed"

echo "[workflow] Running tests..."
pytest
echo "[workflow] ✅ tests passed"

echo "[workflow] Building..."
python update_data.py
python build.py
echo "[workflow] ✅ built"

echo "[workflow] Deactivating virtual environment..."
deactivate
echo "[workflow] ✅ virtual environment deactivated"

echo "[workflow] 🎉 Done! All Processes Completed Successfully! 🎉"
