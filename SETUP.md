# EchoMind Setup Guide

## 🚀 Complete Setup Instructions

### Prerequisites Check

1. **Node.js** (v18 or higher)
   ```bash
   node --version
   ```
   If not installed: [Download Node.js](https://nodejs.org/)

2. **Python** (v3.8 or higher)
   ```bash
   python --version
   # or
   python3 --version
   ```
   If not installed: [Download Python](https://www.python.org/downloads/)

3. **pip** (Python package manager)
   ```bash
   pip --version
   # or
   pip3 --version
   ```
   Usually comes with Python installation.

### Step-by-Step Setup

#### 1. Clone or Navigate to Project
```bash
cd EchoMind
```

#### 2. Install Frontend Dependencies
```bash
npm install
```

#### 3. Install Python Backend Dependencies
```bash
cd server
pip install -r requirements.txt
cd ..
```

#### 4. Configure Environment (Optional)
Create `.env.local` in the root directory:
```env
NEXT_PUBLIC_API_URL=http://localhost:5000
```

#### 5. Start the Application

**Option A: Using Two Terminals**

Terminal 1 - Python Backend:
```bash
cd server
python run.py
```

Terminal 2 - Next.js Frontend:
```bash
npm run dev
```

**Option B: Using Helper Scripts (Windows)**
```bash
# Terminal 1
start-backend.bat

# Terminal 2
npm run dev
```

**Option B: Using Helper Scripts (Mac/Linux)**
```bash
# Make script executable
chmod +x start-backend.sh

# Terminal 1
./start-backend.sh

# Terminal 2
npm run dev
```

#### 6. Access the Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- Health Check: http://localhost:5000/api/health

### Verification

1. **Check Backend Health**
   ```bash
   curl http://localhost:5000/api/health
   ```
   Should return: `{"status":"healthy","message":"EchoMind API is running",...}`

2. **Check Frontend**
   - Open http://localhost:3000
   - You should see the EchoMind interface

3. **Test Backend Connection**
   - Open browser console (F12)
   - Check for any connection errors
   - The app will use local fallback if backend is unavailable

### Troubleshooting

#### Backend Not Starting
- Check Python version: `python --version`
- Install dependencies: `pip install -r server/requirements.txt`
- Check port 5000 is available
- Try: `python server/app.py` directly

#### Frontend Not Starting
- Check Node.js version: `node --version`
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
- Check port 3000 is available

#### Connection Issues
- Verify backend is running: `curl http://localhost:5000/api/health`
- Check CORS settings in `server/app.py`
- Ensure firewall allows local connections
- Check `.env.local` has correct API URL

#### Port Conflicts
- Backend: Change port in `server/app.py`
- Frontend: Change port: `npm run dev -- -p 3001`
- Update `.env.local` with new backend URL

### Development Workflow

1. **Start Backend** (Terminal 1)
   ```bash
   cd server
   python run.py
   ```

2. **Start Frontend** (Terminal 2)
   ```bash
   npm run dev
   ```

3. **Make Changes**
   - Backend: Changes auto-reload (Flask debug mode)
   - Frontend: Changes hot-reload (Next.js)

4. **Test Features**
   - Journal: Test text and voice input
   - Dashboard: View mood visualizations
   - Analysis: Test emotion detection

### Production Build

#### Frontend
```bash
npm run build
npm start
```

#### Backend
```bash
cd server
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Next Steps

1. Read [README.md](README.md) for detailed documentation
2. Read [QUICKSTART.md](QUICKSTART.md) for quick reference
3. Explore the codebase in `components/` directory
4. Customize colors in `tailwind.config.js`
5. Integrate with external LLM APIs if needed

### Support

- Check [README.md](README.md) troubleshooting section
- Review [server/README.md](server/README.md) for backend issues
- Open an issue on GitHub for bugs or questions

Happy coding! 🎉

