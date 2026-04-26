# AI Automation Workflows with LLM

A comprehensive Python project for building AI-powered automation workflows using Large Language Models (LLMs). This project provides agents, workflows, and utilities for email processing, report generation, customer support, and content summarization.

## 🚀 Features

### 🤖 AI Agents
- **Email Agent**: Automated email processing, categorization, and response generation
- **Report Agent**: Dynamic report generation from data with insights and recommendations
- **Summarizer Agent**: Intelligent text summarization for various content types

### 🔄 Automated Workflows
- **Reporting Workflow**: Automated daily, weekly, and custom report generation
- **Customer Support Workflow**: Complete ticket processing system with escalation

### 🛠️ Utilities
- **LLM Client**: Multi-provider support (OpenAI, Anthropic, Mock for testing)
- **Prompt Templates**: Comprehensive template library for consistent LLM interactions
- **FastAPI REST API**: Complete API endpoints for all functionality

## 📁 Project Structure

```
ai-automation-workflows-llm/
│
├── src/
│   ├── agents/
│   │   ├── email_agent.py      # Email processing and response generation
│   │   ├── report_agent.py     # Report generation and data analysis
│   │   └── summarizer.py       # Text summarization capabilities
│   │
│   ├── workflows/
│   │   ├── automate_reporting.py    # Automated reporting workflows
│   │   └── customer_support_flow.py # Customer support automation
│   │
│   └── utils/
│       ├── llm_client.py       # LLM provider abstraction
│       └── prompt_templates.py # Reusable prompt templates
│
├── data/
│   └── sample_inputs/          # Sample data for testing
│
├── notebooks/
│   └── experimentation.ipynb   # Jupyter notebook for testing
│
├── api/
│   └── app.py                  # FastAPI REST application
│
├── tests/
│   └── test_agents.py          # Comprehensive test suite
│
├── config/
│   └── config.yaml             # Configuration file
│
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── main.py                     # Main application entry point
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-automation-workflows-llm
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # For OpenAI
   export OPENAI_API_KEY="your-openai-api-key"
   
   # For Anthropic
   export ANTHROPIC_API_KEY="your-anthropic-api-key"
   ```

5. **Create necessary directories**
   ```bash
   mkdir -p data/reports data/tickets logs
   ```

## 🚀 Quick Start

### Using the Main Application

```bash
python main.py
```

This will start the application with default settings and demonstrate the core functionality.

### Using the API

```bash
# Start the FastAPI server
cd api
python app.py

# Or use uvicorn for production
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000` with interactive documentation at `http://localhost:8000/docs`.

### Using Jupyter Notebook

```bash
jupyter notebook notebooks/experimentation.ipynb
```

## 📖 Usage Examples

### Email Processing

```python
from src.agents import EmailAgent
from src.utils import LLMClient

# Initialize LLM client and email agent
llm_client = LLMClient('openai', {'openai_api_key': 'your-key'})
email_agent = EmailAgent(llm_client)

# Process an email
result = email_agent.process_email(
    content="I'm having trouble with my account login",
    sender="customer@example.com",
    subject="Login Issue"
)

print(f"Category: {result['category']}")
print(f"Response: {result['response']}")
```

### Report Generation

```python
from src.agents import ReportAgent

report_agent = ReportAgent(llm_client)

data = {
    'sales': [1000, 1500, 2000],
    'customers': [50, 75, 100],
    'satisfaction': [4.1, 4.3, 4.5]
}

report = report_agent.generate_report(data, 'monthly', 'Sales Report')
print(f"Executive Summary: {report['executive_summary']}")
```

### Customer Support Workflow

```python
from src.workflows import CustomerSupportWorkflow

support_workflow = CustomerSupportWorkflow(llm_client)

ticket = {
    'customer_email': 'customer@example.com',
    'subject': 'Cannot access account',
    'message': 'I need help with my login',
    'priority': 'high'
}

result = support_workflow.process_incoming_ticket(ticket)
print(f"Ticket ID: {result['ticket_id']}")
print(f"Auto Response: {result['auto_response']}")
```

## 🔧 Configuration

The project uses `config/config.yaml` for configuration. Key settings include:

- **LLM Provider**: Choose between OpenAI, Anthropic, or Mock (for testing)
- **API Settings**: Configure host, port, and CORS settings
- **Workflow Settings**: Customize agent behavior and thresholds
- **Logging**: Set log levels and output destinations

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `ANTHROPIC_API_KEY`: Your Anthropic API key

## 🧪 Testing

Run the comprehensive test suite:

```bash
python tests/test_agents.py
```

Or use pytest:

```bash
pytest tests/ -v
```

## 📚 API Documentation

The FastAPI application provides comprehensive REST endpoints:

### Email Endpoints
- `POST /email/process` - Process a single email
- `POST /email/batch` - Process multiple emails

### Report Endpoints
- `POST /report/generate` - Generate a report
- `POST /report/trends` - Analyze trends

### Summarization Endpoints
- `POST /summarize/text` - Summarize text
- `POST /summarize/meeting` - Summarize meeting transcript
- `POST /summarize/document` - Summarize document

### Customer Support Endpoints
- `POST /support/ticket` - Create and process ticket
- `POST /support/ticket/{id}/followup` - Handle follow-up
- `POST /support/ticket/{id}/escalate` - Escalate ticket

### Workflow Endpoints
- `POST /workflow/report` - Run reporting workflow
- `POST /workflow/report/async` - Run workflow in background

Visit `http://localhost:8000/docs` for interactive API documentation.

## 🏗️ Architecture

### Component Overview

1. **LLM Client Layer**: Abstract interface for different LLM providers
2. **Agent Layer**: Specialized AI agents for specific tasks
3. **Workflow Layer**: Orchestrates agents into complete workflows
4. **API Layer**: RESTful interface for external integration
5. **Utility Layer**: Shared utilities and templates

### Design Patterns

- **Strategy Pattern**: LLM provider selection
- **Factory Pattern**: Agent and workflow creation
- **Observer Pattern**: Workflow monitoring and logging
- **Template Method**: Consistent prompt generation

## 🔒 Security Considerations

- API key management through environment variables
- Input validation and sanitization
- Rate limiting capabilities
- CORS configuration
- Error handling without information leakage

## 🚀 Deployment

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Considerations

- Use environment variables for sensitive configuration
- Implement proper logging and monitoring
- Set up reverse proxy (nginx) for HTTPS
- Configure database persistence for production data
- Implement proper backup strategies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For questions and support:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed information
3. Review the documentation and examples

## 🗺️ Roadmap

- [ ] Add more LLM providers (Google Gemini, Cohere)
- [ ] Implement advanced workflow orchestration
- [ ] Add database persistence layer
- [ ] Implement real-time monitoring dashboard
- [ ] Add more sophisticated error handling
- [ ] Create plugin system for custom agents
- [ ] Add A/B testing for prompt optimization
- [ ] Implement multi-language support

## 📊 Performance

- **Email Processing**: ~1-2 seconds per email
- **Report Generation**: ~3-5 seconds for standard reports
- **Text Summarization**: ~1-3 seconds depending on length
- **API Response Time**: <100ms for health checks

*Performance varies based on LLM provider and complexity of input.*

---

**Built with ❤️ using Python, FastAPI, and modern LLM technologies**
