# Makefile compatible Windows et Linux

# Variables
PYTHON = python
PIP = pip
VENV = venv

# Détecter le système d'exploitation
ifeq ($(OS),Windows_NT)
    # Windows
    SOURCE_VENV = .\$(VENV)\Scripts\activate
    RM = rmdir /s /q
    DEL = del /s /q
    MKDIR = mkdir
    CHECK_DIR = if exist
    PYTHON_EXE = python.exe
else
    # Linux/MacOS
    SOURCE_VENV = . $(VENV)/bin/activate
    RM = rm -rf
    DEL = find . -type f -name "*.pyc" -delete
    MKDIR = mkdir -p
    CHECK_DIR = test -d
    PYTHON_EXE = python
endif

# Directories
SRC_PYTHON = src/main/python
TEST_PYTHON = src/test/python

# Commands
BEHAVE = behave
ALLURE = allure
UNITTEST = $(PYTHON) -m unittest
FLAKE8 = flake8
BLACK = black
ISORT = isort
COVERAGE = coverage

# Default target
all: install test

# Set up virtual environment and install dependencies
install:
	@echo "Setting up virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Installing dependencies..."
	$(SOURCE_VENV) && $(PYTHON_EXE) -m pip install --upgrade pip
	$(SOURCE_VENV) && $(PIP) install -r requirements.txt

# Run all tests (unit and behavior) and serve the report
test: unit-test behave-test serve-behave-test test-coverage

# Run all tests (unit and behavior)
test-action: unit-test behave-test test-coverage

# Run unit tests
unit-test:
	@echo "Running unit tests..."
	$(SOURCE_VENV) && $(UNITTEST) discover -s $(TEST_PYTHON) -v

# Run behavior tests (behave)
behave-test:
	@echo "Running behavior tests..."
	$(SOURCE_VENV) && $(RM) allure-results 2> /dev/null || echo "No allure-results directory to delete, skipping..."
	$(SOURCE_VENV) && $(BEHAVE)

# Run behavior tests (behave)
serve-behave-test:
	$(SOURCE_VENV) && $(ALLURE) serve

test-coverage:
	@echo "Running unit tests with coverage..."
	$(SOURCE_VENV) && $(COVERAGE) run --source=$(SRC_PYTHON) -m unittest discover -s $(TEST_PYTHON) -v
	$(SOURCE_VENV) && $(COVERAGE) report
	$(SOURCE_VENV) && $(COVERAGE) xml

# Lint the code
lint:
	@echo "Linting code..."
	$(SOURCE_VENV) && $(FLAKE8) $(SRC_PYTHON) $(TEST_PYTHON)

# Format the code
format:
	@echo "Formatting code..."
	$(SOURCE_VENV) && $(BLACK) $(SRC_PYTHON) $(TEST_PYTHON)
	$(SOURCE_VENV) && $(ISORT) $(SRC_PYTHON) $(TEST_PYTHON)

# Build the project (create a distributable package)
build:
	@echo "Building the project..."
	$(SOURCE_VENV) && $(PYTHON) setup.py sdist bdist_wheel

# Clean up temporary files
clean:
	@echo "Cleaning up..."
ifeq ($(OS),Windows_NT)
	@if exist $(VENV) ( $(RM) $(VENV) ) else ( echo "venv not found, skipping..." )
	@if exist dist ( $(RM) dist ) else ( echo "dist not found, skipping..." )
	@if exist build ( $(RM) build ) else ( echo "build not found, skipping..." )
	@if exist *.pyc ( $(DEL) *.pyc ) else ( echo "No .pyc files to delete, skipping..." )
	@if exist __pycache__ ( $(RM) __pycache__ ) else ( echo "__pycache__ not found, skipping..." )
else
	@$(CHECK_DIR) $(VENV) && $(RM) $(VENV) || echo "venv not found, skipping..."
	@$(CHECK_DIR) dist && $(RM) dist || echo "dist not found, skipping..."
	@$(CHECK_DIR) build && $(RM) build || echo "build not found, skipping..."
	@$(DEL) || echo "No .pyc files to delete, skipping..."
	@$(CHECK_DIR) __pycache__ && $(RM) __pycache__ || echo "__pycache__ not found, skipping..."
endif

# Run the application
run:
	@echo "Running the application..."
	$(SOURCE_VENV) && set PYTHONPATH=. && $(PYTHON) src/main/python/calculator/main.py

# Phony targets
.PHONY: all install test unit-test behave-test lint format build clean run
