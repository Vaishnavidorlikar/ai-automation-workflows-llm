"""
Main entry point for AI Automation Workflows application.
"""

import sys
import os
import yaml
import logging
import argparse
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / 'src'))

from src.integration.ai_orchestrator import AIOrchestrator


def setup_logging(config: dict):
    """Set up logging configuration."""
    log_config = config.get('logging', {})
    log_level = getattr(logging, log_config.get('level', 'INFO').upper())
    log_format = log_config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create logs directory if it doesn't exist
    log_file = log_config.get('file')
    if log_file:
        log_dir = Path(log_file).parent
        log_dir.mkdir(parents=True, exist_ok=True)

    # Configure logging
    logging.basicConfig(
        level=log_level,
        format=log_format,
        filename=log_file,
        filemode='a'
    )

    # Also log to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(console_handler)


def load_config(config_path: str = 'config/config.yaml') -> dict:
    """Load configuration from YAML file."""
    logger = logging.getLogger(__name__)
    
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        # Replace environment variables
        def replace_env_vars(obj):
            if isinstance(obj, dict):
                return {k: replace_env_vars(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [replace_env_vars(item) for item in obj]
            elif isinstance(obj, str) and obj.startswith('${') and obj.endswith('}'):
                env_var = obj[2:-1]
                return os.getenv(env_var, obj)
            else:
                return obj
        
        config = replace_env_vars(config)
        return config
        
    except FileNotFoundError:
        logger.error(f"Config file not found: {config_path}")
        return {}
    except yaml.YAMLError as e:
        logger.error(f"Error parsing config file: {e}")

def initialize_orchestrator(config: dict) -> AIOrchestrator:
    """Initialize the AI Orchestrator with given configuration."""
    logger = logging.getLogger(__name__)
    logger.info("Initializing AI Orchestrator...")

    orchestrator = AIOrchestrator(config)

    if orchestrator.initialize_all():
        logger.info("SUCCESS: AI Orchestrator initialized successfully")
        return orchestrator
    else:
        logger.error("ERROR: Failed to initialize orchestrator")
        return None


def run_demo(orchestrator: AIOrchestrator, demo_type: str = 'all'):
    """Run demonstration of orchestrator capabilities."""
    logger = logging.getLogger(__name__)
    
    if not orchestrator:
        logger.error("ERROR: Orchestrator not initialized")
        return

    logger.info(f"Running {demo_type} demo...")

    if demo_type in ['all', 'api']:
        logger.info("API endpoints available at: http://localhost:8000")
        logger.info("See README.md for API usage examples")

    if demo_type in ['all', 'workflows']:
        # Test workflow execution
        test_result = orchestrator.test_workflow_execution()
        logger.info(f"Workflow test result: {test_result}")

    if demo_type in ['all', 'monitoring']:
        # Test monitoring capabilities
        metrics = orchestrator.get_system_metrics()
        logger.info(f"System metrics: {metrics}")


def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(description='AI Workflow Orchestration Platform')
    parser.add_argument('--config', default='config/config.yaml',
                       help='Path to configuration file')
    parser.add_argument('--demo', choices=['all', 'api', 'workflows', 'monitoring', 'none'],
                       default='none', help='Run specific demo')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       default='INFO', help='Logging level')

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)
    if not config:
        logger = logging.getLogger(__name__)
        logger.error("ERROR: Failed to load configuration")
        return 1

    # Override log level if specified
    if args.log_level != 'INFO':
        config['logging'] = config.get('logging', {})
        config['logging']['level'] = args.log_level

    # Setup logging
    setup_logging(config)

    # Initialize orchestrator
    orchestrator = initialize_orchestrator(config)
    if not orchestrator:
        return 1

    # Run demo if requested
    if args.demo != 'none':
        run_demo(orchestrator, args.demo)

    logger = logging.getLogger(__name__)
    logger.info("AI Workflow Orchestration Platform ready!")
    logger.info("Use --demo api to start the API server")
    logger.info("Use --demo all to run full demonstration")

    return 0


if __name__ == '__main__':
    sys.exit(main())
