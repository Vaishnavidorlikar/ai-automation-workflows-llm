"""
Main entry point for AI Automation Workflows application.
"""

import sys
import os
import yaml
import logging
from pathlib import Path
from datetime import datetime
import argparse

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / 'src'))

from utils.llm_client import LLMClient
from agents.email_agent import EmailAgent
from agents.report_agent import ReportAgent
from agents.summarizer import SummarizerAgent
from workflows.automate_reporting import AutomatedReportingWorkflow
from workflows.customer_support_flow import CustomerSupportWorkflow


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
        print(f"Config file not found: {config_path}")
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing config file: {e}")
        return {}


def initialize_components(config: dict):
    """Initialize all components with given configuration."""
    llm_config = config.get('llm', {})
    default_provider = llm_config.get('default_provider', 'mock')
    
    # Get provider-specific config
    provider_config = llm_config.get(default_provider, {})
    
    # Initialize LLM client
    print(f"Initializing LLM client with {default_provider} provider...")
    llm_client = LLMClient(default_provider, provider_config)
    
    # Test connection
    if llm_client.test_connection():
        print("✅ LLM client connection successful")
    else:
        print("❌ LLM client connection failed")
        return None
    
    # Initialize agents
    print("Initializing agents...")
    email_agent = EmailAgent(llm_client)
    report_agent = ReportAgent(llm_client)
    summarizer = SummarizerAgent(llm_client)
    
    # Initialize workflows
    print("Initializing workflows...")
    reporting_workflow = AutomatedReportingWorkflow(llm_client, config)
    support_workflow = CustomerSupportWorkflow(llm_client, config)
    
    return {
        'llm_client': llm_client,
        'email_agent': email_agent,
        'report_agent': report_agent,
        'summarizer': summarizer,
        'reporting_workflow': reporting_workflow,
        'support_workflow': support_workflow
    }


def demo_email_processing(components: dict):
    """Demonstrate email processing capabilities."""
    print("\n" + "="*50)
    print("📧 EMAIL PROCESSING DEMO")
    print("="*50)
    
    email_agent = components['email_agent']
    
    test_email = {
        'content': '''
        Hi Support Team,
        
        I'm having trouble accessing my account. I've been trying to log in for the past hour 
        but keep getting an "Invalid credentials" error. I'm sure my password is correct 
        because I just used it yesterday. I need to access my account urgently as I have 
        an important deadline today. Can you please help me resolve this issue quickly?
        
        Thank you,
        Sarah Johnson
        ''',
        'sender': 'sarah.johnson@example.com',
        'subject': 'Urgent: Account Login Issue'
    }
    
    print(f"Processing email from {test_email['sender']}")
    print(f"Subject: {test_email['subject']}")
    print(f"Content preview: {test_email['content'][:100]}...")
    
    result = email_agent.process_email(
        test_email['content'],
        test_email['sender'],
        test_email['subject']
    )
    
    print(f"\n📊 Results:")
    print(f"  Category: {result.get('category', 'N/A')}")
    print(f"  Processed: {'✅' if result.get('processed') else '❌'}")
    print(f"  Summary: {result.get('summary', 'N/A')}")
    print(f"  Response: {result.get('response', 'N/A')[:200]}...")


def demo_report_generation(components: dict):
    """Demonstrate report generation capabilities."""
    print("\n" + "="*50)
    print("📊 REPORT GENERATION DEMO")
    print("="*50)
    
    report_agent = components['report_agent']
    
    test_data = {
        'sales_performance': {
            'monthly_revenue': [45000, 52000, 48000, 61000, 58000],
            'new_customers': [120, 145, 130, 165, 155],
            'customer_retention': [0.85, 0.87, 0.86, 0.89, 0.88]
        },
        'support_metrics': {
            'total_tickets': 1250,
            'resolved_tickets': 1180,
            'avg_resolution_time': 3.2,
            'customer_satisfaction': 4.3
        },
        'product_usage': {
            'active_users': 2500,
            'daily_logins': 1800,
            'feature_adoption': {
                'dashboard': 0.95,
                'reports': 0.78,
                'automation': 0.42
            }
        }
    }
    
    print("Generating monthly performance report...")
    
    result = report_agent.generate_report(
        test_data,
        'monthly',
        'Monthly Performance Report'
    )
    
    print(f"\n📊 Results:")
    print(f"  Title: {result.get('title', 'N/A')}")
    print(f"  Status: {result.get('status', 'N/A')}")
    print(f"  Executive Summary: {result.get('executive_summary', 'N/A')[:200]}...")
    print(f"  Recommendations: {len(result.get('recommendations', []))} items")
    
    # Show trend analysis
    print("\n📈 Trend Analysis:")
    historical_data = [
        {'timestamp': '2024-01-01', 'revenue': 45000, 'customers': 120},
        {'timestamp': '2024-02-01', 'revenue': 52000, 'customers': 145},
        {'timestamp': '2024-03-01', 'revenue': 48000, 'customers': 130},
        {'timestamp': '2024-04-01', 'revenue': 61000, 'customers': 165},
        {'timestamp': '2024-05-01', 'revenue': 58000, 'customers': 155}
    ]
    
    trend_result = report_agent.generate_trend_analysis(historical_data, 'revenue')
    print(f"  Revenue Trend: {trend_result.get('trend_direction', 'N/A')}")
    print(f"  Change Rate: {trend_result.get('change_rate', 0):.1f}%")


def demo_summarization(components: dict):
    """Demonstrate text summarization capabilities."""
    print("\n" + "="*50)
    print("📝 TEXT SUMMARIZATION DEMO")
    print("="*50)
    
    summarizer = components['summarizer']
    
    test_text = '''
    Artificial Intelligence (AI) has become an integral part of modern business operations, 
    transforming industries across the globe. Companies are increasingly adopting AI technologies 
    to automate repetitive tasks, analyze vast amounts of data, and provide personalized 
    customer experiences. Machine learning algorithms are being used to predict customer behavior, 
    optimize supply chains, and detect fraudulent activities. Natural Language Processing (NLP) 
    enables businesses to analyze customer feedback, automate customer support, and generate 
    content at scale. Computer vision is revolutionizing quality control, security monitoring, 
    and inventory management. Despite these advancements, organizations face challenges including 
    data privacy concerns, the need for skilled AI professionals, and the ethical implications 
    of automated decision-making. Successful AI implementation requires careful planning, 
    robust data infrastructure, and a clear understanding of business objectives.
    '''
    
    print(f"Original text length: {len(test_text)} characters")
    
    # Generate different types of summaries
    summary_types = ['brief', 'executive', 'detailed']
    
    for summary_type in summary_types:
        print(f"\n📋 {summary_type.title()} Summary:")
        result = summarizer.summarize_text(test_text, summary_type)
        
        print(f"  Length: {result.get('summary_length', 0)} words")
        print(f"  Compression: {result.get('compression_ratio', 0):.2f}x")
        print(f"  Summary: {result.get('summary', 'N/A')}")
        print(f"  Key Points: {len(result.get('key_points', []))} items")


def demo_customer_support(components: dict):
    """Demonstrate customer support workflow."""
    print("\n" + "="*50)
    print("🎧 CUSTOMER SUPPORT WORKFLOW DEMO")
    print("="*50)
    
    support_workflow = components['support_workflow']
    
    test_ticket = {
        'customer_email': 'john.doe@company.com',
        'subject': 'Critical System Issue - Production Down',
        'message': '''
        Our production system has been down for the past 2 hours. We're getting error code 500 
        when trying to access the main dashboard. This is affecting our entire team and we 
        have critical deadlines to meet. We need immediate assistance as this is causing 
        significant business impact. Please escalate this to your senior technical team.
        ''',
        'priority': 'critical'
    }
    
    print(f"Processing ticket from {test_ticket['customer_email']}")
    print(f"Priority: {test_ticket['priority']}")
    print(f"Subject: {test_ticket['subject']}")
    
    result = support_workflow.process_incoming_ticket(test_ticket)
    
    print(f"\n🎫 Ticket Results:")
    print(f"  Ticket ID: {result.get('ticket_id', 'N/A')}")
    print(f"  Status: {result.get('status', 'N/A')}")
    print(f"  Escalation Needed: {'✅' if result.get('escalation_needed') else '❌'}")
    print(f"  Auto Response: {result.get('auto_response', 'N/A')[:200]}...")
    print(f"  Similar Tickets: {len(result.get('similar_tickets', []))} found")


def demo_automated_reporting(components: dict):
    """Demonstrate automated reporting workflow."""
    print("\n" + "="*50)
    print("📈 AUTOMATED REPORTING WORKFLOW DEMO")
    print("="*50)
    
    reporting_workflow = components['reporting_workflow']
    
    data_sources = ['sales_database', 'crm_system', 'support_tickets']
    recipients = ['manager@company.com', 'team@company.com']
    
    print(f"Running daily report for {len(data_sources)} data sources...")
    
    result = reporting_workflow.run_daily_report(data_sources, recipients)
    
    print(f"\n📊 Workflow Results:")
    print(f"  Status: {result.get('status', 'N/A')}")
    print(f"  Report ID: {result.get('report_id', 'N/A')}")
    print(f"  Recipients: {len(result.get('recipients', []))}")
    print(f"  Summary: {result.get('summary', 'N/A')[:200]}...")


def run_demo(components: dict, demo_type: str = 'all'):
    """Run selected demo or all demos."""
    demos = {
        'email': demo_email_processing,
        'report': demo_report_generation,
        'summarize': demo_summarization,
        'support': demo_customer_support,
        'workflow': demo_automated_reporting
    }
    
    if demo_type == 'all':
        print("🚀 Running all demos...")
        for demo_name, demo_func in demos.items():
            demo_func(components)
    elif demo_type in demos:
        demos[demo_type](components)
    else:
        print(f"Unknown demo: {demo_type}")
        print(f"Available demos: {', '.join(demos.keys())}")


def start_api_server(config: dict):
    """Start the FastAPI server."""
    print("\n🌐 Starting API Server...")
    print("API will be available at: http://localhost:8000")
    print("Interactive docs at: http://localhost:8000/docs")
    
    # Import and run the FastAPI app
    sys.path.append(str(Path(__file__).parent / 'api'))
    from app import app
    import uvicorn
    
    api_config = config.get('api', {})
    host = api_config.get('host', '0.0.0.0')
    port = api_config.get('port', 8000)
    debug = api_config.get('debug', False)
    
    uvicorn.run(app, host=host, port=port, debug=debug)


def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(description='AI Automation Workflows')
    parser.add_argument('--config', default='config/config.yaml', help='Configuration file path')
    parser.add_argument('--demo', choices=['all', 'email', 'report', 'summarize', 'support', 'workflow'], 
                       default='all', help='Demo to run')
    parser.add_argument('--api', action='store_true', help='Start API server')
    parser.add_argument('--test', action='store_true', help='Run tests')
    
    args = parser.parse_args()
    
    print("🤖 AI Automation Workflows")
    print("=" * 50)
    
    # Load configuration
    print("Loading configuration...")
    config = load_config(args.config)
    if not config:
        print("❌ Failed to load configuration")
        return
    
    # Setup logging
    setup_logging(config)
    logger = logging.getLogger(__name__)
    logger.info("Application starting")
    
    # Initialize components
    components = initialize_components(config)
    if not components:
        print("❌ Failed to initialize components")
        return
    
    print("✅ All components initialized successfully")
    
    try:
        if args.test:
            # Run tests
            print("\n🧪 Running tests...")
            import subprocess
            result = subprocess.run([sys.executable, 'tests/test_agents.py'], 
                                  capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
        
        elif args.api:
            # Start API server
            start_api_server(config)
        
        else:
            # Run demos
            run_demo(components, args.demo)
            
            print("\n" + "="*50)
            print("✅ Demo completed successfully!")
            print("\nNext steps:")
            print("  • Run with --api to start the REST API server")
            print("  • Visit http://localhost:8000/docs for API documentation")
            print("  • Check notebooks/experimentation.ipynb for more examples")
            print("  • Review config/config.yaml for customization options")
    
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        print(f"❌ Error: {str(e)}")
    
    logger.info("Application finished")


if __name__ == '__main__':
    main()
