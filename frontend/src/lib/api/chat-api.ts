import apiClient from './client';

export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  reply: string;
}

export const chatWithAI = async (message: string): Promise<ChatResponse> => {
  const response = await apiClient.post('/api/v1/chat', { message });
  return response as unknown as ChatResponse;
};