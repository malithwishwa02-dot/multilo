# CLAUDE.md

## Project: Quantum Profile Warmup CLI

### Commands
- Run CLI: `python3 main.py --help`
- Run Interactive: `python3 main.py --interactive`
- Run Integrated Framework: `python3 integrated_fraud_framework.py`
- Run Multilogin Generator: `python3 quantum_multilogin_generator_v2.py`
- Run Warmup Standalone: `python3 quantum_warmup_profile_v2.py`

### Dependencies
- `pip install -r requirements.txt`
- Requires Chrome/Chromium for Selenium (undetected-chromedriver manages this)

### Structure
- `main.py`: CLI entry point
- `quantum_multilogin_generator_v2.py`: Core logic for profile generation
- `quantum_warmup_profile_v2.py`: Core logic for warmup
- `profile_generator.py`: Wrapper for main.py integration
- `warmup.py`: Wrapper for main.py integration
- `injector.py`: Artifact injection stub
