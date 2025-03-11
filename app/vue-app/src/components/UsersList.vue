<template>
  <v-container>
    <v-card>
      <v-card-title class="d-flex justify-space-between">
        <span>Users List</span>
        <v-btn color="primary" @click="openCreateDialog">New user</v-btn>
      </v-card-title>

      <v-data-table
        :headers="headers"
        :items="users"
        :loading="loading"
        class="elevation-1"
      >
        <template v-slot:item.username="{ item }">
          <router-link :to="`/users/${item._id}`" class="text-primary">
            {{ item.username }}
          </router-link>
        </template>

        <template v-slot:item.roles="{ item }">
          {{ item.roles?.join(', ')}}
        </template>

        <template v-slot:item.active="{ item }">
          <v-chip :color="item.active ? 'green' : 'red'" dark>
            {{ item.active ? 'Active' : 'Inactive' }}
          </v-chip>
        </template>

        <template v-slot:item.created_ts="{ item }">
          {{ item.created_ts }}
        </template>

        <template v-slot:item.actions="{ item }">
          <v-btn icon size="small" variant="text" @click="openEditDialog(item)">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
          <v-btn icon size="small" variant="text" color="red" @click="confirmDelete(item)">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </template>
      </v-data-table>
    </v-card>

    <!-- Editing -->
    <v-dialog v-model="editDialog" max-width="500px">
      <v-card>
        <v-card-title>Edit user</v-card-title>
        <v-card-text>
          <v-text-field label="User name" v-model="selectedUser.username" readonly></v-text-field>
          <v-select label="Roles" v-model="selectedUser.roles" :items="rolesOptions" multiple></v-select>
          <v-switch label="Active" v-model="selectedUser.active"></v-switch>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="editDialog = false">Cancel</v-btn>
          <v-btn color="primary" @click="updateUser">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Deleting -->
    <v-dialog v-model="deleteDialog" max-width="400px">
      <v-card>
        <v-card-title>Confirm</v-card-title>
        <v-card-text>
          Are you sure you want to delete user <strong>{{ selectedUser.username }}</strong>?
        </v-card-text>
        <v-card-actions>
          <v-btn @click="deleteDialog = false">Cancel</v-btn>
          <v-btn color="red" @click="deleteUser">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'


const users = ref([])
const loading = ref(false)
const router = useRouter()


const editDialog = ref(false)
const deleteDialog = ref(false)
const selectedUser = ref({})
const rolesOptions = ref(['admin', 'manager', 'user'])


const headers = ref([
  { title: 'Username', key: 'username' },
  { title: 'Roles', key: 'roles' },
  { title: 'Timezone', key: 'preferences' },
  { title: 'Is Active?', key: 'active' },
  { title: 'Created at', key: 'created_ts' },
  { title: 'Actions', key: 'actions', sortable: false },
])


const fetchUsers = async () => {
  loading.value = true
  try {
    const response = await axios.get('http://localhost:5000/users')
    users.value = response.data
  } catch (error) {
    console.error('Error fetching users:', error)
  } finally {
    loading.value = false
  }
}

const openEditDialog = (user) => {
  selectedUser.value = { ...user }
  editDialog.value = true
}

const updateUser = () => {
  alert('Feature not implemented yet.')
}

// Abrir modal de exclusão
const confirmDelete = (user) => {
  selectedUser.value = user
  deleteDialog.value = true
}

const deleteUser = async () => {
  try {
    await axios.delete(`http://localhost:5000/users/${selectedUser.value._id}`)
    fetchUsers()
    deleteDialog.value = false
    router.push("/users");
  } catch (error) {
    console.error('Error deleting user:', error)
  }
}

const openCreateDialog = () => {
  alert('Feature not implemented yet.')
}

// Fetch users on mounting the component
onMounted(fetchUsers)
</script>

