# Lumora Client - Vue.js Frontend

A modern Vue.js frontend for the Lumora FastAPI server with user management capabilities.

## Features

- 🚀 **Real-time server status monitoring**
- 👤 **User creation form** with validation
- 📋 **Users list display** with refresh capability
- 🎨 **Modern, responsive UI** with smooth animations
- 📱 **Mobile-friendly design**
- ⚡ **Fast API integration** with error handling

## Prerequisites

- Node.js (v16 or higher)
- npm or yarn package manager
- FastAPI server running on port 8000

## Setup

1. **Install dependencies:**
```bash
npm install
```

2. **Start the development server:**
```bash
npm run dev
```

3. **Open your browser:**
Navigate to http://localhost:3000

## Development

- **Hot reload**: Changes automatically refresh in the browser
- **API proxy**: Frontend proxies `/api/*` requests to `http://localhost:8000/*`
- **Error handling**: Comprehensive error messages and user feedback

## Build for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

## API Integration

The frontend communicates with the FastAPI server through:

- **Server Status**: `GET /api/` (root endpoint)
- **Create User**: `POST /api/users`
- **Get Users**: `GET /api/users`

## Project Structure

```
client/
├── src/
│   ├── App.vue          # Main application component
│   ├── main.js          # Vue app entry point
│   └── style.css        # Global styles
├── index.html           # HTML template
├── vite.config.js       # Vite configuration
├── package.json         # Dependencies and scripts
└── README.md           # This file
```

## Technologies Used

- **Vue 3** - Progressive JavaScript framework
- **Vite** - Fast build tool and dev server
- **Axios** - HTTP client for API requests
- **CSS Grid & Flexbox** - Modern layout system
