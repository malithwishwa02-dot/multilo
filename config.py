"""
Configuration management for Quantum Profile Warmup CLI
Handles environment variables, API keys, and system settings
"""

import os
from typing import Optional, Dict, Any
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Central configuration management"""
    
    # API Keys
    MULTILOGIN_API_KEY: Optional[str] = os.getenv("MULTILOGIN_API_KEY")
    MISTRAL_API_KEY: Optional[str] = os.getenv("MISTRAL_API_KEY")
    
    # API Endpoints
    MULTILOGIN_API_BASE: str = os.getenv("MULTILOGIN_API_BASE", "https://api.multilogin.com/v2")
    
    # Application Settings
    DEFAULT_OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "out")
    DEFAULT_WARMUP_MINUTES: int = int(os.getenv("DEFAULT_WARMUP_MINUTES", "30"))
    DEFAULT_HEADLESS: bool = os.getenv("DEFAULT_HEADLESS", "false").lower() == "true"
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: Optional[str] = os.getenv("LOG_FILE")
    
    # Security
    ENABLE_MIL_PROTOCOL: bool = os.getenv("ENABLE_MIL_PROTOCOL", "true").lower() == "true"
    MIL_OVERRIDE_CODE: str = os.getenv("MIL_OVERRIDE_CODE", "6666")
    
    # Profile Generation
    DEFAULT_BIN_PREFIX: str = os.getenv("DEFAULT_BIN_PREFIX", "552742")
    DEFAULT_MERCHANT: str = os.getenv("DEFAULT_MERCHANT", "amazon.com")
    
    @classmethod
    def validate(cls) -> Dict[str, bool]:
        """Validate configuration settings"""
        validations = {
            "multilogin_api_configured": cls.MULTILOGIN_API_KEY is not None,
            "mistral_api_configured": cls.MISTRAL_API_KEY is not None,
            "output_dir_writable": Path(cls.DEFAULT_OUTPUT_DIR).parent.exists(),
            "mil_protocol_enabled": cls.ENABLE_MIL_PROTOCOL,
        }
        return validations
    
    @classmethod
    def get_config_summary(cls) -> str:
        """Get configuration summary for logging"""
        validations = cls.validate()
        summary = [
            "=== Configuration Summary ===",
            f"Multilogin API: {'✓ Configured' if validations['multilogin_api_configured'] else '✗ Not configured'}",
            f"Mistral API: {'✓ Configured' if validations['mistral_api_configured'] else '✗ Not configured'}",
            f"Output Directory: {cls.DEFAULT_OUTPUT_DIR}",
            f"Default Warmup: {cls.DEFAULT_WARMUP_MINUTES} minutes",
            f"Headless Mode: {cls.DEFAULT_HEADLESS}",
            f"MIL Protocol: {'✓ Enabled' if cls.ENABLE_MIL_PROTOCOL else '✗ Disabled'}",
            f"Log Level: {cls.LOG_LEVEL}",
        ]
        return "\n".join(summary)

# Singleton instance
config = Config()
