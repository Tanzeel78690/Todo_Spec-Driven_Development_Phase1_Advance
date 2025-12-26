"use client";

import { createContext, useContext, useState, ReactNode } from 'react';

interface UIContextType {
  isLoading: boolean;
  setIsLoading: (loading: boolean) => void;
  error: string | null;
  setError: (message: string | null) => void;
}

const UIContext = createContext<UIContextType | undefined>(undefined);

export const useUI = () => {
  const context = useContext(UIContext);
  if (!context) {
    throw new Error('useUI must be used within a UIProvider');
  }
  return context;
};

export function UIProvider({ children }: { children: ReactNode }) {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  return (
    <UIContext.Provider value={{ isLoading, setIsLoading, error, setError }}>
      {isLoading && (
        <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-900 bg-opacity-50 z-50">
          <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-indigo-500"></div>
        </div>
      )}
      {error && (
        <div className="fixed top-0 left-0 w-full p-4 bg-red-500 text-white text-center z-50">
          {error}
          <button onClick={() => setError(null)} className="ml-4 font-bold">
            &times;
          </button>
        </div>
      )}
      {children}
    </UIContext.Provider>
  );
}
