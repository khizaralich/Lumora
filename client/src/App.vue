<template>
  <div id="app">
    <header>
      <h1>🚀 Lumora User Management</h1>
      <p>FastAPI + Vue.js Integration</p>
    </header>

    <main>
      <!-- Server Status -->
      <div class="status-section">
        <h2>Server Status</h2>
        <div class="status-indicator" :class="{ 'online': serverStatus.online, 'offline': !serverStatus.online }">
          {{ serverStatus.online ? '🟢 Online' : '🔴 Offline' }}
        </div>
        <button @click="checkServerStatus" class="btn btn-secondary">Check Status</button>
      </div>

      <!-- Create User Form -->
      <div class="form-section">
        <h2>Create New User</h2>
        <form @submit.prevent="createUser" class="user-form">
          <div class="form-group">
            <label for="email">Email:</label>
            <input 
              type="email" 
              id="email" 
              v-model="newUser.email" 
              required 
              placeholder="user@example.com"
            />
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input 
              type="password" 
              id="password" 
              v-model="newUser.password" 
              required 
              placeholder="Enter password"
            />
          </div>
          <button type="submit" class="btn btn-primary" :disabled="loading">
            {{ loading ? 'Creating...' : 'Create User' }}
          </button>
        </form>
      </div>

      <!-- Users List -->
      <div class="users-section">
        <h2>Users List</h2>
        <button @click="loadUsers" class="btn btn-secondary">Refresh Users</button>
        <div v-if="users.length === 0" class="no-users">
          No users found. Create one above!
        </div>
        <div v-else class="users-grid">
          <div v-for="user in users" :key="user.id" class="user-card">
            <div class="user-info">
              <strong>ID:</strong> {{ user.id }}<br>
              <strong>Email:</strong> {{ user.email }}<br>
              <strong>Created:</strong> {{ formatDate(user.created_at) }}
            </div>
          </div>
        </div>
      </div>

      <!-- Messages -->
      <div v-if="message" class="message" :class="messageType">
        {{ message }}
        <button @click="clearMessage" class="message-close">×</button>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      serverStatus: {
        online: false
      },
      newUser: {
        email: '',
        password: ''
      },
      users: [],
      loading: false,
      message: '',
      messageType: 'info'
    }
  },
  async mounted() {
    await this.checkServerStatus()
    await this.loadUsers()
  },
  methods: {
    async checkServerStatus() {
      try {
        const response = await axios.get('/api/')
        this.serverStatus.online = true
        this.showMessage('Server is running!', 'success')
      } catch (error) {
        this.serverStatus.online = false
        this.showMessage('Server is offline. Make sure FastAPI is running on port 8000.', 'error')
      }
    },
    async createUser() {
      if (!this.serverStatus.online) {
        this.showMessage('Cannot create user: server is offline', 'error')
        return
      }

      this.loading = true
      try {
        const response = await axios.post('/api/users', this.newUser)
        this.users.push(response.data)
        this.newUser.email = ''
        this.newUser.password = ''
        this.showMessage('User created successfully!', 'success')
      } catch (error) {
        const errorMsg = error.response?.data?.detail || 'Failed to create user'
        this.showMessage(errorMsg, 'error')
      } finally {
        this.loading = false
      }
    },
    async loadUsers() {
      if (!this.serverStatus.online) {
        this.showMessage('Cannot load users: server is offline', 'error')
        return
      }

      try {
        const response = await axios.get('/api/users')
        this.users = response.data
      } catch (error) {
        this.showMessage('Failed to load users', 'error')
      }
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleString()
    },
    showMessage(text, type = 'info') {
      this.message = text
      this.messageType = type
      setTimeout(() => {
        this.clearMessage()
      }, 5000)
    },
    clearMessage() {
      this.message = ''
    }
  }
}
</script>

<style scoped>
#app {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

header {
  text-align: center;
  margin-bottom: 40px;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 10px;
}

header h1 {
  margin: 0;
  font-size: 2.5rem;
}

header p {
  margin: 10px 0 0 0;
  opacity: 0.9;
}

main {
  display: grid;
  gap: 30px;
}

.status-section, .form-section, .users-section {
  background: white;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.status-section {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.status-indicator {
  padding: 10px 20px;
  border-radius: 25px;
  font-weight: bold;
  font-size: 1.1rem;
}

.status-indicator.online {
  background: #d4edda;
  color: #155724;
}

.status-indicator.offline {
  background: #f8d7da;
  color: #721c24;
}

.user-form {
  display: grid;
  gap: 20px;
}

.form-group {
  display: grid;
  gap: 8px;
}

.form-group label {
  font-weight: bold;
  color: #333;
}

.form-group input {
  padding: 12px;
  border: 2px solid #e1e5e9;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-primary {
  background: #667eea;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: #5a6fd8;
  transform: translateY(-2px);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-secondary {
  background: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background: #5a6268;
}

.users-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.user-card {
  background: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border-left: 4px solid #667eea;
}

.user-info {
  line-height: 1.6;
}

.no-users {
  text-align: center;
  padding: 40px;
  color: #6c757d;
  font-style: italic;
}

.message {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 15px 20px;
  border-radius: 6px;
  color: white;
  font-weight: bold;
  max-width: 400px;
  z-index: 1000;
  animation: slideIn 0.3s ease-out;
}

.message.success {
  background: #28a745;
}

.message.error {
  background: #dc3545;
}

.message.info {
  background: #17a2b8;
}

.message-close {
  background: none;
  border: none;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
  margin-left: 10px;
  opacity: 0.7;
}

.message-close:hover {
  opacity: 1;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@media (max-width: 768px) {
  #app {
    padding: 10px;
  }
  
  header h1 {
    font-size: 2rem;
  }
  
  .status-section {
    flex-direction: column;
    align-items: stretch;
  }
  
  .users-grid {
    grid-template-columns: 1fr;
  }
}
</style>
