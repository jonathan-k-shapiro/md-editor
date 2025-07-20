# Markdown Document Management System

A collaborative web application that enables non-technical users to edit markdown documents through an intuitive WYSIWYG interface, with automatic git repository synchronization behind the scenes.

## 🎯 Project Overview

This system abstracts away the complexity of git operations and markdown syntax, providing a familiar document editing experience similar to Google Docs or Notion, while maintaining all content in a git repository for version control and collaboration.

### Key Features

- **WYSIWYG Editing**: Rich text editor with real-time preview
- **Git Integration**: Automatic synchronization with git repositories
- **Real-time Collaboration**: Multiple users can edit simultaneously
- **Document Organization**: Hierarchical folder structure with search
- **Version History**: Access to document history without git complexity
- **No Git Knowledge Required**: Users never interact with git directly

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React/TS      │    │   Python API    │    │   PostgreSQL    │
│   Frontend      │◄──►│   Backend       │◄──►│   Database      │
│                 │    │   (FastAPI)     │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Git Repository│
                       │   (GitHub/GitLab)│
                       └─────────────────┘
```

## 📁 Repository Structure

```
md-editor/
├── frontend/          # React/TypeScript frontend application
├── backend/           # Python/FastAPI backend API
├── docs/              # Project documentation
├── SPECIFICATION.md   # Detailed technical specification
├── docker-compose.yml # Development environment (coming soon)
└── README.md          # This file
```

## 🚀 Quick Start

### Prerequisites

Before setting up the project, ensure you have the following installed:

- **Git**: Version 2.0 or higher
- **Python**: Version 3.11 or higher
- **Node.js**: Version 18 or higher
- **npm** or **yarn**: For frontend package management
- **PostgreSQL**: Version 13 or higher (for production setup)
- **Docker** (optional): For containerized development

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd md-editor
   ```

2. **Backend Setup**
   ```bash
   cd backend
   
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies (when available)
   pip install -r requirements.txt
   
   # Set up environment variables
   cp .env.example .env
   # Edit .env with your configuration
   
   # Run database migrations (when available)
   alembic upgrade head
   
   # Start the development server
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   
   # Install dependencies (when available)
   npm install
   # or: yarn install
   
   # Set up environment variables
   cp .env.example .env.local
   # Edit .env.local with your configuration
   
   # Start the development server
   npm run dev
   # or: yarn dev
   ```

4. **Access the Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🔧 Development Commands

### Backend Commands
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload

# Run tests
pytest

# Database migrations
alembic revision --autogenerate -m "Description"
alembic upgrade head

# Code formatting
black .
isort .

# Linting
flake8
mypy .
```

### Frontend Commands
```bash
# Install dependencies
npm install

# Development server
npm run dev

# Build for production
npm run build

# Run tests
npm test

# Run tests with coverage
npm run test:coverage

# Linting
npm run lint

# Format code
npm run format

# Type checking
npm run type-check
```

## 🐳 Docker Development (Coming Soon)

For a consistent development environment across all platforms:

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild services
docker-compose up --build
```

## 📊 Development Workflow

### Branch Strategy

- **main**: Production-ready code
- **develop**: Integration branch for features
- **feature/***: Feature development branches
- **hotfix/***: Emergency fixes for production

### Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add user authentication
fix: resolve editor crash on empty document
docs: update API documentation
style: format code with prettier
refactor: extract git service logic
test: add unit tests for document service
chore: update dependencies
```

### Pull Request Process

1. Create feature branch from `develop`
2. Make changes with descriptive commits
3. Add/update tests for new functionality
4. Update documentation if needed
5. Create pull request to `develop`
6. Ensure all CI checks pass
7. Request code review
8. Address feedback and merge

## 🧪 Testing

### Backend Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_documents.py

# Run tests with verbose output
pytest -v
```

### Frontend Testing
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run end-to-end tests
npm run test:e2e
```

## 📝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Follow the coding standards
4. **Add tests**: Ensure your changes are tested
5. **Commit your changes**: `git commit -m 'feat: add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**: Describe your changes clearly

### Coding Standards

#### Backend (Python)
- Follow PEP 8 style guide
- Use type hints for all functions
- Write docstrings for classes and functions
- Maximum line length: 88 characters (Black default)
- Use meaningful variable and function names

#### Frontend (TypeScript/React)
- Follow TypeScript strict mode
- Use functional components with hooks
- Write prop types and interfaces
- Use meaningful component and variable names
- Follow React best practices

## 📚 Documentation

- [Technical Specification](SPECIFICATION.md) - Comprehensive technical details
- [API Documentation](docs/api.md) - Backend API reference *(coming soon)*
- [User Guide](docs/user-guide.md) - End-user documentation *(coming soon)*
- [Developer Guide](docs/developer-guide.md) - Advanced development topics *(coming soon)*

## 🔐 Security

- Report security vulnerabilities privately via email
- Follow security best practices in all contributions
- Keep dependencies updated
- Use environment variables for sensitive configuration

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- Create an issue for bug reports or feature requests
- Join our development discussions
- Check the documentation for common questions

## 🗺️ Roadmap

See [SPECIFICATION.md](SPECIFICATION.md) for detailed development phases:

- **Phase 1**: Core Infrastructure (4-6 weeks)
- **Phase 2**: Document Management (4-6 weeks) 
- **Phase 3**: WYSIWYG Editor (6-8 weeks)
- **Phase 4**: Collaboration Features (4-6 weeks)
- **Phase 5**: Polish & Production (4-6 weeks)

---

**Built with ❤️ for seamless markdown collaboration** 