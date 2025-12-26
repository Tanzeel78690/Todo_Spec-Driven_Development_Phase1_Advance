const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

interface SignupResponse {
  message?: string;
  detail?: string;
}

export const signupUser = async (email: string, password: string): Promise<SignupResponse> => {
  const response = await fetch(`${API_URL}/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const errorData: SignupResponse = await response.json();
    throw new Error(errorData.detail || 'Signup failed');
  }

  return response.json();
};

export const signinUser = async (email: string, password: string): Promise<{ access_token: string, token_type: string }> => {
  const response = await fetch(`${API_URL}/signin`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `username=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`,
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Signin failed');
  }

  const data = await response.json();
  localStorage.setItem('access_token', data.access_token);
  return data;
};
