import { apiClient } from './client';

export interface Conversation {
  id: string;
  title: string;
  owner_id: string;
  created_at: string;
  updated_at: string;
}

export interface CreateConversationRequest {
  title: string;
  owner_id: string;
}

export interface UpdateConversationRequest {
  title?: string;
}

export interface ConversationListResponse {
  conversations: Conversation[];
  total: number;
  limit: number;
  offset: number;
}

export interface Message {
  id: string;
  conversation_id: string;
  sender: 'user' | 'ai';
  content: string;
  created_at: string;
}

export interface CreateMessageRequest {
  conversation_id: string;
  sender: 'user' | 'ai';
  content: string;
}

export interface UpdateMessageRequest {
  content?: string;
}

export interface MessageListResponse {
  messages: Message[];
  total: number;
  limit: number;
  offset: number;
}

export const conversationApi = {
  async getConversations(
    limit: number = 50,
    offset: number = 0
  ): Promise<ConversationListResponse> {
    const response = await apiClient.get('/api/v1/conversations', {
      params: { limit, offset }
    });
    return response.data;
  },

  async createConversation(data: CreateConversationRequest): Promise<Conversation> {
    const response = await apiClient.post('/api/v1/conversations', data);
    return response.data;
  },

  async getConversationById(id: string): Promise<Conversation> {
    const response = await apiClient.get(`/api/v1/conversations/${id}`);
    return response.data;
  },

  async updateConversation(id: string, data: UpdateConversationRequest): Promise<Conversation> {
    const response = await apiClient.put(`/api/v1/conversations/${id}`, data);
    return response.data;
  },

  async patchConversation(id: string, data: UpdateConversationRequest): Promise<Conversation> {
    const response = await apiClient.patch(`/api/v1/conversations/${id}`, data);
    return response.data;
  },

  async deleteConversation(id: string): Promise<void> {
    await apiClient.delete(`/api/v1/conversations/${id}`);
  },

  async getConversationMessages(
    conversationId: string,
    limit: number = 50,
    offset: number = 0
  ): Promise<MessageListResponse> {
    const response = await apiClient.get(`/api/v1/conversations/${conversationId}/messages`, {
      params: { limit, offset }
    });
    return response.data;
  },
};

export const messageApi = {
  async createMessage(data: CreateMessageRequest): Promise<Message> {
    const response = await apiClient.post('/api/v1/messages', data);
    return response.data;
  },

  async getMessageById(id: string): Promise<Message> {
    const response = await apiClient.get(`/api/v1/messages/${id}`);
    return response.data;
  },

  async updateMessage(id: string, data: UpdateMessageRequest): Promise<Message> {
    const response = await apiClient.put(`/api/v1/messages/${id}`, data);
    return response.data;
  },

  async patchMessage(id: string, data: UpdateMessageRequest): Promise<Message> {
    const response = await apiClient.patch(`/api/v1/messages/${id}`, data);
    return response.data;
  },

  async deleteMessage(id: string): Promise<void> {
    await apiClient.delete(`/api/v1/messages/${id}`);
  },
};