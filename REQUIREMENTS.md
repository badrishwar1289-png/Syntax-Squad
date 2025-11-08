# EchoMind - Project Requirements

This document lists all requirements for running the EchoMind application, including both frontend and backend dependencies.

## 📦 System Requirements

### Minimum System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: 4GB minimum, 8GB recommended
- **Disk Space**: 500MB for dependencies
- **Internet Connection**: Required for initial installation

### Software Requirements

#### Frontend
- **Node.js**: v18.0.0 or higher
- **npm**: v9.0.0 or higher (comes with Node.js)
- **yarn**: v1.22.0 or higher (optional, alternative to npm)

#### Backend
- **Python**: v3.8.0 or higher (v3.9+ recommended)
- **pip**: v21.0.0 or higher (comes with Python)
- **virtualenv**: Optional but recommended for isolated environments

## 📋 Frontend Dependencies

### Production Dependencies
Located in `package.json`:

```json
{
  "next": "^14.0.0",
  "react": "^18.2.0",
  "react-dom": "^18.2.0",
  "framer-motion": "^10.16.0",
  "recharts": "^2.10.0",
  "lucide-react": "^0.294.0",
  "date-fns": "^2.30.0",
  "axios": "^1.6.0"
}
```

### Development Dependencies
```json
{
  "@types/node": "^20.10.0",
  "@types/react": "^18.2.0",
  "@types/react-dom": "^18.2.0",
  "typescript": "^5.3.0",
  "tailwindcss": "^3.3.0",
  "postcss": "^8.4.0",
  "autoprefixer": "^10.4.0",
  "eslint": "^8.54.0",
  "eslint-config-next": "^14.0.0"
}
```

### Install Frontend Dependencies
```bash
npm install
# or
yarn install
```

## 🐍 Python Backend Dependencies

### Production Dependencies
Located in `server/requirements.txt`:

```
Flask==3.0.0
flask-cors==4.0.0
python-dotenv==1.0.0
```

### Optional Production Dependencies (for production deployment)
```
gunicorn==21.2.0
```

### Install Python Dependencies
```bash
cd server
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
```

### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🔧 Development Tools

### Recommended IDE/Editors
- **VS Code** (with extensions):
  - ESLint
  - Prettier
  - Python
  - Tailwind CSS IntelliSense
  - TypeScript and JavaScript Language Features

### Browser Requirements
- **Chrome**: v90+ (recommended for voice input)
- **Firefox**: v88+
- **Safari**: v14+
- **Edge**: v90+

### Browser Features Required
- **Web Speech API**: For voice input (Chrome, Edge, Safari)
- **LocalStorage**: For data persistence
- **Fetch API**: For API requests
- **ES6+ Support**: For modern JavaScript features

## 📝 Environment Variables

### Frontend (`.env.local`)
```env
NEXT_PUBLIC_API_URL=http://localhost:5000
```

### Backend (`.env` - optional)
```env
FLASK_ENV=development
FLASK_DEBUG=1
PORT=5000
```

## 🚀 Installation Commands Summary

### Complete Setup
```bash
# 1. Clone repository
git clone <repository-url>
cd EchoMind

# 2. Install frontend dependencies
npm install

# 3. Install backend dependencies
cd server
pip install -r requirements.txt
cd ..

# 4. Create environment file (optional)
echo "NEXT_PUBLIC_API_URL=http://localhost:5000" > .env.local

# 5. Start backend (Terminal 1)
cd server
python run.py

# 6. Start frontend (Terminal 2)
npm run dev
```

## ✅ Verification Checklist

### Frontend
- [ ] Node.js installed (`node --version`)
- [ ] npm installed (`npm --version`)
- [ ] Dependencies installed (`node_modules` folder exists)
- [ ] TypeScript compiles without errors
- [ ] Next.js dev server starts successfully

### Backend
- [ ] Python installed (`python --version`)
- [ ] pip installed (`pip --version`)
- [ ] Flask installed (`pip list | grep Flask`)
- [ ] Backend server starts on port 5000
- [ ] Health check endpoint responds (`curl http://localhost:5000/api/health`)

### Integration
- [ ] Frontend connects to backend
- [ ] API endpoints respond correctly
- [ ] CORS is configured properly
- [ ] Environment variables are set

## 🔍 Dependency Versions

### Frontend Versions
| Package | Version | Purpose |
|---------|---------|---------|
| next | ^14.0.0 | React framework |
| react | ^18.2.0 | UI library |
| framer-motion | ^10.16.0 | Animations |
| recharts | ^2.10.0 | Data visualization |
| tailwindcss | ^3.3.0 | Styling |
| typescript | ^5.3.0 | Type safety |

### Backend Versions
| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0.0 | Web framework |
| flask-cors | 4.0.0 | CORS support |
| python-dotenv | 1.0.0 | Environment variables |

## 🐛 Troubleshooting Dependencies

### Frontend Issues
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install

# Check for outdated packages
npm outdated

# Update packages (careful!)
npm update
```

### Backend Issues
```bash
# Upgrade pip
pip install --upgrade pip

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Check installed packages
pip list

# Verify Flask installation
python -c "import flask; print(flask.__version__)"
```

### Version Conflicts
- Use `package-lock.json` (frontend) to lock versions
- Use `requirements.txt` with exact versions (backend)
- Consider using virtual environments for Python

## 📚 Additional Resources

- [Node.js Documentation](https://nodejs.org/docs/)
- [Python Documentation](https://docs.python.org/3/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## 🔄 Updating Dependencies

### Frontend
```bash
# Check for updates
npm outdated

# Update specific package
npm update <package-name>

# Update all packages (use with caution)
npm update
```

### Backend
```bash
# Update pip
pip install --upgrade pip

# Update specific package
pip install --upgrade <package-name>

# Update all packages
pip list --outdated
pip install --upgrade -r requirements.txt
```

## 📦 Production Dependencies

### Frontend Production Build
```bash
npm run build
npm start
```

### Backend Production Deployment
```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🔒 Security Notes

- Keep dependencies updated for security patches
- Use `npm audit` to check for vulnerabilities
- Use `pip check` to verify Python package integrity
- Review dependency licenses before production use
- Use environment variables for sensitive configuration

---

**Last Updated**: 2024
**Maintained By**: EchoMind Development Team

