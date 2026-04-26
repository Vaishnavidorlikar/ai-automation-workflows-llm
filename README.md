# 🚀 AI Automation Workflows with JARVIS-like Assistant

A comprehensive Python project for building AI-powered automation workflows using Large Language Models (LLMs), computer vision, deep learning, and advanced data science. This project features a **JARVIS-like AI assistant** with voice interaction, hand gesture recognition, and complete machine learning capabilities.

## 🚀 Features

### 🤖 JARVIS-like AI Assistant
- **Voice Interaction**: Speech recognition and text-to-speech capabilities
- **Natural Language Processing**: Advanced conversational AI with AIML
- **Multi-modal Interface**: Voice commands + gesture recognition
- **Intelligent Responses**: Context-aware conversation system

### 👋 Hand Gesture Recognition
- **Real-time Detection**: Live camera-based gesture recognition
- **Computer Vision**: MediaPipe integration for accurate hand tracking
- **Multiple Gestures**: Thumbs up, peace, rock, paper, scissors, OK, point, etc.
- **Deep Learning**: Trainable gesture classification models

### 🧠 Deep Learning Models (TensorFlow/Keras)
- **CNN Models**: Image classification and computer vision
- **RNN/LSTM**: Text processing and sequence analysis
- **Autoencoders**: Dimensionality reduction and feature learning
- **GANs**: Generative models for data synthesis
- **Transfer Learning**: Pre-trained model fine-tuning

### 📊 Data Analysis & Visualization
- **NumPy/Pandas**: Advanced data manipulation and analysis
- **Statistical Analysis**: Comprehensive descriptive and inferential statistics
- **Matplotlib/Seaborn**: Professional data visualization
- **Interactive Plots**: Plotly and Bokeh for web-based visualizations
- **Automated Insights**: AI-powered data pattern detection

### ⚙️ Machine Learning (Scikit-learn)
- **Classification**: Random Forest, SVM, Logistic Regression, KNN, Naive Bayes
- **Regression**: Linear, Ridge, Lasso, Random Forest, SVR
- **Clustering**: K-Means, DBSCAN, Hierarchical clustering
- **Feature Engineering**: Selection, extraction, and preprocessing
- **Model Evaluation**: Cross-validation, hyperparameter tuning, performance metrics

### 💬 Conversational AI (AIML)
- **Pattern Matching**: Rule-based conversation system
- **Dynamic Responses**: Context-aware answer generation
- **Knowledge Base**: Extensible pattern-response database
- **Learning Capability**: Interaction-based improvement

### 🔄 Automated Workflows
- **Reporting Workflow**: Automated daily, weekly, and custom report generation
- **Customer Support Workflow**: Complete ticket processing system with escalation
- **Data Pipeline**: End-to-end automated data processing
- **Multi-agent Coordination**: Coordinated AI agent workflows

### 🛠️ Core Utilities
- **LLM Client**: Multi-provider support (OpenAI, Anthropic, Mock for testing)
- **Prompt Templates**: 20+ reusable templates for consistent LLM interactions
- **FastAPI REST API**: Complete API endpoints for all functionality
- **Configuration Management**: YAML-based configuration with environment variables

## 📁 Project Structure

```
ai-automation-workflows-llm/
│
├── src/
│   ├── agents/
│   │   ├── email_agent.py      # Email processing and response generation
│   │   ├── report_agent.py     # Report generation and data analysis  
│   │   └── summarizer.py       # Text summarization capabilities
│   ├── jarvis/
│   │   └── jarvis_assistant.py  # JARVIS-like AI assistant with voice interaction
│   ├── gesture_recognition/
│   │   └── gesture_detector.py  # Hand gesture recognition using computer vision
│   ├── deep_learning/
│   │   └── model_manager.py     # TensorFlow/Keras deep learning models
│   ├── data_analysis/
│   │   └── data_analyzer.py     # NumPy/Pandas data analysis and visualization
│   ├── aiml/
│   │   └── aiml_processor.py    # AIML conversational AI processor
│   ├── ml_models/
│   │   └── sklearn_manager.py   # Scikit-learn machine learning models
│   ├── workflows/
│   │   ├── automate_reporting.py    # Automated reporting workflows
│   │   └── customer_support_flow.py # Customer support automation
│   └── utils/
│       ├── llm_client.py       # Multi-provider LLM abstraction
│       └── prompt_templates.py # Reusable prompt templates
│
├── data/
│   ├── sample_inputs/          # Sample data directory
│   ├── gestures/               # Gesture recognition data
│   ├── voice/                  # Voice data storage
│   └── models/                 # Trained model storage
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
├── models/                     # Trained model storage
├── integrated_demo.py          # Complete AI/ML demonstration
├── requirements.txt            # Python dependencies
├── README.md                   # Comprehensive documentation
└── main.py                     # Main application entry point
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Camera (for gesture recognition)
- Microphone (for voice commands)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vaishnavidorlikar/ai-automation-workflows-llm.git
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
   mkdir -p data/reports data/tickets logs models/gestures data/voice
   ```

6. **Optional: Install additional system dependencies**
   ```bash
   # For voice recognition (macOS)
   brew install portaudio
   
   # For voice recognition (Ubuntu)
   sudo apt-get install portaudio19-dev python3-pyaudio
   
   # For camera access (Linux)
   sudo apt-get install v4l-utils
   ```

## 🚀 Quick Start

### 🎯 Integrated AI/ML Demo (Recommended)

Run the comprehensive demo that showcases all features:

```bash
python integrated_demo.py
```

This interactive demo includes:
- 🗣️ JARVIS voice assistant
- 👋 Hand gesture recognition  
- 🧠 Deep learning models
- 📊 Data analysis & visualization
- 💬 Conversational AI
- ⚙️ Machine learning models
- 🔄 Integrated workflows
- 📈 Performance comparisons

### Using the Main Application

```bash
python main.py --demo all          # Run all demos
python main.py --demo jarvis       # JARVIS assistant demo
python main.py --demo gesture      # Gesture recognition demo
python main.py --api               # Start API server
python main.py --test              # Run tests
```

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

### 🗣️ JARVIS Voice Assistant

```python
from src.jarvis import JARVISAssistant

# Initialize JARVIS
jarvis = JARVISAssistant()

# Start continuous listening
jarvis.start_continuous_listening()

# Process voice commands
response = jarvis.process_command("Analyze the sales data")
print(f"JARVIS: {response}")

# Enable gesture monitoring
jarvis.start_gesture_monitoring()

# Get status
status = jarvis.get_status()
print(f"Status: {status}")
```

### 👋 Hand Gesture Recognition

```python
from src.gesture_recognition import GestureDetector

# Initialize gesture detector
detector = GestureDetector()

# Real-time gesture detection
detector.start_camera_detection("Gesture Recognition")

# Single gesture detection
import cv2
frame = cv2.imread('hand_image.jpg')
gesture = detector.detect_gesture(frame)
print(f"Detected gesture: {gesture}")

# Train custom gesture model
detector.train_gesture_model('data/gestures/', 'models/gesture_model.h5')
```

### 🧠 Deep Learning Models

```python
from src.deep_learning import ModelManager

# Initialize model manager
manager = ModelManager()

# Create CNN for image classification
cnn_model = manager.create_image_classifier((64, 64, 3), 10, 'image_classifier')

# Create LSTM for text processing
lstm_model = manager.create_text_classifier(1000, 100, 5, 'text_classifier')

# Train model
X_train, y_train = load_training_data()
history = manager.train_model(cnn_model, X_train, y_train, epochs=20)

# Create GAN
generator = manager.create_gan_generator(latent_dim=100)
discriminator = manager.create_gan_discriminator()
```

### 📊 Data Analysis & Visualization

```python
from src.data_analysis import DataAnalyzer

# Initialize data analyzer
analyzer = DataAnalyzer()

# Load data
df = analyzer.load_data('data/sales_data.csv', 'sales_data')

# Generate sample data
sample_df = analyzer.generate_sample_data('classification', 1000, 15)

# Analyze data
analysis = analyzer.analyze_data('sales_data')
print(f"Summary: {analysis['summary']}")

# Create visualizations
plot_path = analyzer.create_visualization('sales_data', 'heatmap')

# Build ML models
ml_results = analyzer.build_ml_model('sales_data', 'target')
print(f"Best model accuracy: {ml_results['Random Forest']['accuracy']:.3f}")

# Perform PCA
pca_results = analyzer.perform_pca('sales_data', n_components=2)
```

### ⚙️ Machine Learning (Scikit-learn)

```python
from src.ml_models import SklearnManager
from sklearn.datasets import make_classification

# Initialize ML manager
ml_manager = SklearnManager()

# Generate sample data
X, y = make_classification(n_samples=1000, n_features=20, n_classes=3)

# Prepare data
prepared_data = ml_manager.prepare_data(pd.DataFrame(X), pd.Series(y))

# Train multiple models
results = ml_manager.train_classification_models(
    prepared_data['X_train'], prepared_data['y_train']
)

# Evaluate models
eval_results = ml_manager.evaluate_classification_models(
    prepared_data['X_test'], prepared_data['y_test']
)

# Hyperparameter tuning
tuning_results = ml_manager.hyperparameter_tuning(
    prepared_data['X_train'], prepared_data['y_train']
)

# Feature selection
selection_results = ml_manager.feature_selection(
    pd.DataFrame(X), pd.Series(y), method='selectkbest', k=10
)

# Clustering
clustering_results = ml_manager.perform_clustering(pd.DataFrame(X))
```

### 💬 Conversational AI (AIML)

```python
from src.aiml import AIMLProcessor

# Initialize AIML processor
aiml = AIMLProcessor()

# Add custom patterns
aiml.add_pattern("WHAT IS YOUR NAME", "I'm JARVIS, your AI assistant!")
aiml.add_pattern("HOW DO YOU WORK", "I use advanced AI to help you!")

# Process user input
response = aiml.respond("Hello JARVIS, how are you?")
print(f"AIML Response: {response}")

# Learn from interactions
aiml.learn_from_interaction("What's the weather?", "good")

# Export patterns
aiml.save_patterns('custom_patterns.aiml')
aiml.export_patterns_json('patterns.json')
```

### 🔄 Integrated Workflow Example

```python
# Complete AI workflow combining all technologies
from src.jarvis import JARVISAssistant
from src.data_analysis import DataAnalyzer
from src.ml_models import SklearnManager

# Initialize components
jarvis = JARVISAssistant()
analyzer = DataAnalyzer()
ml_manager = SklearnManager()

# Voice-activated data analysis
command = "Analyze customer data and create predictions"
response = jarvis.process_command(command)

# Load and analyze data
df = analyzer.load_data('customer_data.csv')
analysis = analyzer.analyze_data('customer_data')

# Build prediction model
ml_results = analyzer.build_ml_model('customer_data', 'churn')

# Generate insights
insights = {
    'data_summary': analysis['summary'],
    'model_performance': ml_results,
    'recommendations': ['Focus on high-risk customers', 'Improve retention strategies']
}

# Voice response with results
jarvis.speak(f"I analyzed {df.shape[0]} customers and built a prediction model with {ml_results['Random Forest']['accuracy']:.1%} accuracy.")
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
