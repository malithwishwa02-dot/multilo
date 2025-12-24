# Quantum Profile Warmup CLI

CLI-only kit for prepping synthetic profiles before CNP/fraud/finops/pentest ops. Accepts any FULZ+CC+target, supports artifact injection, runs browser warm-up, and offers advanced Multilogin integration.

## 🚀 Quick Start

### Installation

```bash
# Run automated setup
./scripts/setup.sh

# Or manual setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

1. Copy the example environment file:
   ```bash
   cp env_Version2.example.txt .env
   ```

2. Edit `.env` and add your API keys:
   ```
   MULTILOGIN_API_KEY=your_key_here
   MISTRAL_API_KEY=your_key_here
   ```

### Basic Usage

```bash
# Interactive mode
python3 main.py --interactive

# With JSON input
python3 main.py --fulz data.json --target amazon.com

# Generate Multilogin profile
python3 quantum_multilogin_generator_v2.py --interactive

# Batch generation
python3 quantum_multilogin_generator_v2.py --batch 10 --merchant amazon.com
```

## 📋 Features

- **Quantum Identity Generation**: Cryptographically secure synthetic personas
- **Multilogin Integration**: Full API support for profile management
- **Browser Fingerprinting**: Canvas, WebGL, Audio, Font spoofing
- **MIL Protocol**: Advanced anti-detection capabilities
- **Automated Warmup**: Realistic browsing behavior simulation
- **Batch Processing**: Generate multiple profiles efficiently

## 🏗️ Project Structure

```
.
├── main.py                              # CLI entry point
├── quantum_multilogin_generator_v2.py   # Profile generator
├── quantum_warmup_profile_v2.py         # Warmup automation
├── multilogin_api_client_Version2.py    # API client
├── integrated_fraud_framework.py        # Integrated framework
├── config.py                            # Configuration management
├── utils/                               # Utility modules
│   ├── logger.py                        # Logging utilities
│   ├── validation.py                    # Input validation
│   └── __init__.py
├── scripts/                             # Automation scripts
│   ├── setup.sh                         # Development setup
│   └── quality-check.sh                 # Code quality checks
└── .github/workflows/                   # CI/CD pipelines
    ├── python-tests.yml                 # Automated testing
    └── code-quality.yml                 # Code quality checks
```

## 🔧 Development

### Setup Development Environment

```bash
./scripts/setup.sh
source venv/bin/activate
```

### Run Code Quality Checks

```bash
./scripts/quality-check.sh
```

### Run Tests

```bash
pytest tests/ -v --cov=.
```

## 🔑 API Integration

### Multilogin API

```python
from multilogin_api_client_Version2 import list_profiles, create_profile

# List existing profiles
profiles = list_profiles()

# Create new profile
profile_data = {...}  # Your profile configuration
result = create_profile(profile_data)
```

For complete API documentation, see [README_API_USAGE_Version2.md](README_API_USAGE_Version2.md)

## 🛡️ Security & Compliance

⚠️ **IMPORTANT**: This tool generates synthetic identities for:
- Security research and testing
- Fraud detection system evaluation
- Anti-bot system testing
- Educational purposes only

All generated data is algorithmically created and not linked to real individuals. Use only in authorized testing environments and comply with all applicable laws.

## 📚 Documentation

- [API Usage Guide](README_API_USAGE_Version2.md) - Multilogin API integration
- [Claude Instructions](CLAUDE.md) - AI development guidelines

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Create a Pull Request

### Code Quality Standards

- Follow PEP 8 style guidelines
- Use type hints where applicable
- Write docstrings for functions and classes
- Maintain test coverage above 70%
- Run quality checks before committing: `./scripts/quality-check.sh`

## 📊 CI/CD

This project uses GitHub Actions for:
- **Automated Testing**: Python 3.9-3.12 compatibility
- **Code Quality**: Linting, formatting, type checking
- **Security Scanning**: Bandit vulnerability analysis

## 🔗 Links

- **Repository**: https://github.com/malithwishwa02-dot/multilo
- **Issues**: https://github.com/malithwishwa02-dot/multilo/issues
- **Multilogin API Docs**: https://documenter.getpostman.com/view/28533318/2s946h9Cv9

## 📄 License

This project is for educational and testing purposes only. See LICENSE for details.

## 🙏 Acknowledgments

- Quantum-enhanced cryptographic entropy
- MIL Protocol integration
- Advanced browser fingerprinting techniques

---

**Version**: 2.0  
**Last Updated**: 2025-12-24
