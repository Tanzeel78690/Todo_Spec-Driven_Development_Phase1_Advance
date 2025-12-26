"use client";

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

interface Todo {
  id: string;
  title: string;
  is_completed: boolean;
  owner_id: string;
}

export default function DashboardPage() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [newTodoTitle, setNewTodoTitle] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    setError('');
    const token = localStorage.getItem('access_token');
    if (!token) {
      router.push('/signin');
      return;
    }

    try {
      const response = await fetch(`${API_URL}/todos`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data: Todo[] = await response.json();
        setTodos(data);
      } else if (response.status === 401) {
        router.push('/signin');
      } else {
        const errData = await response.json();
        setError(errData.detail || 'Failed to fetch todos');
      }
    } catch (err) {
      setError('An unexpected error occurred while fetching todos.');
    }
  };

  const handleCreateTodo = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    const token = localStorage.getItem('access_token');
    if (!token) return;

    try {
      const response = await fetch(`${API_URL}/todos`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ title: newTodoTitle }),
      });

      if (response.ok) {
        setNewTodoTitle('');
        fetchTodos(); // Refresh list
      } else if (response.status === 401) {
        router.push('/signin');
      } else {
        const errData = await response.json();
        setError(errData.detail || 'Failed to create todo');
      }
    } catch (err) {
      setError('An unexpected error occurred while creating todo.');
    }
  };

  const handleToggleComplete = async (todo: Todo) => {
    setError('');
    const token = localStorage.getItem('access_token');
    if (!token) return;

    try {
      const response = await fetch(`${API_URL}/todos/${todo.id}/complete`, {
        method: 'PATCH',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (response.ok) {
        fetchTodos(); // Refresh list
      } else if (response.status === 401) {
        router.push('/signin');
      } else {
        const errData = await response.json();
        setError(errData.detail || 'Failed to toggle todo status');
      }
    } catch (err) {
      setError('An unexpected error occurred while toggling todo status.');
    }
  };

  const handleDeleteTodo = async (todoId: string) => {
    setError('');
    const token = localStorage.getItem('access_token');
    if (!token) return;

    try {
      const response = await fetch(`${API_URL}/todos/${todoId}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (response.status === 204) { // No Content
        fetchTodos(); // Refresh list
      } else if (response.status === 401) {
        router.push('/signin');
      } else {
        const errData = await response.json();
        setError(errData.detail || 'Failed to delete todo');
      }
    } catch (err) {
      setError('An unexpected error occurred while deleting todo.');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    router.push('/signin');
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-xl mx-auto bg-white rounded-lg shadow-md p-6">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold text-gray-800">My Todos</h1>
          <button
            onClick={handleLogout}
            className="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500"
          >
            Logout
          </button>
        </div>

        {error && <p className="text-red-500 text-sm mb-4">{error}</p>}

        <form onSubmit={handleCreateTodo} className="mb-6 flex">
          <input
            type="text"
            className="flex-grow border border-gray-300 rounded-l-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            placeholder="Add a new todo"
            value={newTodoTitle}
            onChange={(e) => setNewTodoTitle(e.target.value)}
            required
          />
          <button
            type="submit"
            className="px-4 py-2 bg-indigo-600 text-white rounded-r-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          >
            Add Todo
          </button>
        </form>

        {todos.length === 0 ? (
          <p className="text-gray-500 text-center">No todos yet. Add one above!</p>
        ) : (
          <ul>
            {todos.map((todo) => (
              <li
                key={todo.id}
                className="flex items-center justify-between bg-gray-50 p-3 mb-2 rounded-md shadow-sm"
              >
                <span
                  className={`text-lg ${todo.is_completed ? 'line-through text-gray-500' : 'text-gray-900'}`}
                >
                  {todo.title}
                </span>
                <div className="flex items-center space-x-2">
                  <input
                    type="checkbox"
                    checked={todo.is_completed}
                    onChange={() => handleToggleComplete(todo)}
                    className="h-5 w-5 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500"
                  />
                  <button
                    onClick={() => handleDeleteTodo(todo.id)}
                    className="px-3 py-1 bg-red-500 text-white text-sm rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500"
                  >
                    Delete
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
