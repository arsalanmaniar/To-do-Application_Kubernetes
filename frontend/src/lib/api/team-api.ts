import apiClient from './client';

export interface Team {
  id: string;
  name: string;
  description?: string;
  owner_id: string;
  created_at: string;
  updated_at: string;
}

export interface CreateTeamRequest {
  name: string;
  description?: string;
  owner_id: string;
}

export interface UpdateTeamRequest {
  name?: string;
  description?: string;
}

export interface TeamListResponse {
  teams: Team[];
  total: number;
  limit: number;
  offset: number;
}

export const teamApi = {
  async getTeams(
    limit: number = 50,
    offset: number = 0
  ): Promise<TeamListResponse> {
    const response = await apiClient.get('/api/v1/teams', {
      params: { limit, offset }
    });
    // Due to the response interceptor in client.ts, the response is already the data payload
    // So response is the actual TeamListResponse object
    if (response && typeof response === 'object' && 'teams' in response) {
      const responseAny = response as any;
      return {
        teams: responseAny.teams || [],
        total: responseAny.total || 0,
        limit: responseAny.limit || limit,
        offset: responseAny.offset || offset
      };
    } else {
      // If response structure is unexpected, return a default structure
      return {
        teams: [],
        total: 0,
        limit: limit,
        offset: offset
      };
    }
  },

  async createTeam(data: CreateTeamRequest): Promise<Team> {
    const response = await apiClient.post('/api/v1/teams', data);
    return response as unknown as Team;
  },

  async getTeamById(id: string): Promise<Team> {
    const response = await apiClient.get(`/api/v1/teams/${id}`);
    return response as unknown as Team;
  },

  async updateTeam(id: string, data: UpdateTeamRequest): Promise<Team> {
    const response = await apiClient.put(`/api/v1/teams/${id}`, data);
    return response as unknown as Team;
  },

  async patchTeam(id: string, data: UpdateTeamRequest): Promise<Team> {
    const response = await apiClient.patch(`/api/v1/teams/${id}`, data);
    return response as unknown as Team;
  },

  async deleteTeam(id: string): Promise<void> {
    await apiClient.delete(`/api/v1/teams/${id}`);
  },
};