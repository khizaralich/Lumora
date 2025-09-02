<template>
  <div id="app">
    <div class="container">
      <h1>🚀 Lumora User Management</h1>
      <p>FastAPI + Vue.js Integration</p>
    </div>

    <div class="container">
      <h2>Server Status</h2>
      <div class="message" :class="serverStatus.online ? 'success' : 'error'">
        {{ serverStatus.online ? '🟢 Online' : '🔴 Offline' }}
      </div>
      <button @click="checkServerStatus" class="btn btn-secondary">Check Status</button>
    </div>

    <div class="container">
      <h2>Create New User</h2>
      <form @submit.prevent="createUser">
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

    <div class="container">
      <h2>Users List</h2>
      <button @click="loadUsers" class="btn btn-secondary">Refresh Users</button>
      <div v-if="users.length === 0" class="message">
        No users found. Create one above!
      </div>
      <div v-else>
        <div v-for="user in users" :key="user.id" class="user-card">
          <strong>ID:</strong> {{ user.id }}<br>
          <strong>Email:</strong> {{ user.email }}<br>
          <strong>Created:</strong> {{ formatDate(user.created_at) }}
        </div>
      </div>
    </div>

    <div v-if="message" class="message" :class="messageType">
      {{ message }}
      <button @click="clearMessage" style="float: right; background: none; border: none; cursor: pointer;">×</button>
    </div>
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
