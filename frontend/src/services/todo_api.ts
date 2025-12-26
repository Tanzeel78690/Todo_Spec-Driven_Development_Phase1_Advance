const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

interface Todo {
  id: string;
  title: string;
  is_completed: boolean;
  owner_id: string;
}

interface TodoCreate {
  title: string;
}

interface TodoUpdate {
  title?: string;
  is_completed?: boolean;
}

const getAuthHeaders = () => {
  const token = localStorage.getItem('access_token');
  if (!token) {
    throw new Error('Authentication token not found.');
  }
  return {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`,
  };
};

export const createTodo = async (todoData: TodoCreate): Promise<Todo> => {
  const response = await fetch(`${API_URL}/todos`, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify(todoData),
  });
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to create todo.');
  }
  return response.json();
};

export const fetchTodos = async (): Promise<Todo[]> => {
  const response = await fetch(`${API_URL}/todos`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to fetch todos.');
  }
  return response.json();
};

export const fetchTodoById = async (id: string): Promise<Todo> => {
  const response = await fetch(`${API_URL}/todos/${id}`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || `Failed to fetch todo with ID ${id}.`);
  }
  return response.json();
};

export const updateTodo = async (id: string, todoData: TodoUpdate): Promise<Todo> => {
  const response = await fetch(`${API_URL}/todos/${id}`, {
    method: 'PUT',
    headers: getAuthHeaders(),
    body: JSON.stringify(todoData),
  });
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || `Failed to update todo with ID ${id}.`);
  }
  return response.json();
};

export const deleteTodo = async (id: string): Promise<void> => {
  const response = await fetch(`${API_URL}/todos/${id}`, {
    method: 'DELETE',
    headers: getAuthHeaders(),
  });
  if (response.status === 401) {
    throw new Error('Authentication token not found or invalid.');
  }
  if (response.status !== 204) {
    const errorData = await response.json();
    throw new Error(errorData.detail || `Failed to delete todo with ID ${id}.`);
  }
};

export const toggleTodoCompletion = async (id: string): Promise<Todo> => {
  const response = await fetch(`${API_URL}/todos/${id}/complete`, {
    method: 'PATCH',
    headers: getAuthHeaders(),
  });
  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || `Failed to toggle completion for todo with ID ${id}.`);
  }
  return response.json();
};
