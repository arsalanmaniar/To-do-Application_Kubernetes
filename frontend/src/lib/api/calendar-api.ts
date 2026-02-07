import apiClient from './client';

export interface CalendarEvent {
  id: string;
  title: string;
  description?: string;
  start_time: string; // ISO date string
  end_time: string;   // ISO date string
  all_day: boolean;
  owner_id: string;
  task_id?: string;
  created_at: string;
  updated_at: string;
}

export interface CreateCalendarEventRequest {
  title: string;
  description?: string;
  start_time: string; // ISO date string
  end_time: string;   // ISO date string
  all_day?: boolean;
  owner_id: string;
  task_id?: string;
}

export interface UpdateCalendarEventRequest {
  title?: string;
  description?: string;
  start_time?: string; // ISO date string
  end_time?: string;   // ISO date string
  all_day?: boolean;
  task_id?: string;
}

export interface CalendarEventListResponse {
  events: CalendarEvent[];
  total: number;
  limit: number;
  offset: number;
}

export const calendarApi = {
  async getCalendarEvents(
    startDate?: string, // ISO date string
    endDate?: string,   // ISO date string
    limit: number = 50,
    offset: number = 0
  ): Promise<CalendarEventListResponse> {
    const params: Record<string, any> = { limit, offset };
    if (startDate) params.start_date = startDate;
    if (endDate) params.end_date = endDate;

    const response = await apiClient.get('/api/v1/calendar', { params });
    // Due to the response interceptor in client.ts, the response is already the data payload
    // So response is the actual CalendarEventListResponse object
    if (response && typeof response === 'object' && 'events' in response) {
      return response as CalendarEventListResponse;
    } else {
      // If response structure is unexpected, return a default structure
      return {
        events: [],
        total: 0,
        limit: limit,
        offset: offset
      };
    }
  },

  async createCalendarEvent(data: CreateCalendarEventRequest): Promise<CalendarEvent> {
    const response = await apiClient.post('/api/v1/calendar', data);
    return response.data;
  },

  async getCalendarEventById(id: string): Promise<CalendarEvent> {
    const response = await apiClient.get(`/api/v1/calendar/${id}`);
    return response.data;
  },

  async updateCalendarEvent(id: string, data: UpdateCalendarEventRequest): Promise<CalendarEvent> {
    const response = await apiClient.put(`/api/v1/calendar/${id}`, data);
    return response.data;
  },

  async patchCalendarEvent(id: string, data: UpdateCalendarEventRequest): Promise<CalendarEvent> {
    const response = await apiClient.patch(`/api/v1/calendar/${id}`, data);
    return response.data;
  },

  async deleteCalendarEvent(id: string): Promise<void> {
    await apiClient.delete(`/api/v1/calendar/${id}`);
  },
};