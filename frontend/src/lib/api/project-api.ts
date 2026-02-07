import apiClient from './client';

export interface Project {
  id: string;
  name: string;
  description?: string;
  owner_id: string;
  created_at: string;
  updated_at: string;
}

export interface CreateProjectRequest {
  name: string;
  description?: string;
  owner_id: string;
}

export interface UpdateProjectRequest {
  name?: string;
  description?: string;
}

export interface ProjectListResponse {
  projects: Project[];
  total: number;
  limit: number;
  offset: number;
}

export const projectApi = {
  async getProjects(
    limit: number = 50,
    offset: number = 0
  ): Promise<ProjectListResponse> {
    const response = await apiClient.get('/api/v1/projects', {
      params: { limit, offset }
    });
    // Due to the response interceptor in client.ts, the response is already the data payload
    // So response is the actual ProjectListResponse object
    if (response && typeof response === 'object' && 'projects' in response) {
      return response as ProjectListResponse;
    } else {
      // If response structure is unexpected, return a default structure
      return {
        projects: [],
        total: 0,
        limit: limit,
        offset: offset
      };
    }
  },

  async createProject(data: CreateProjectRequest): Promise<Project> {
    const response = await apiClient.post('/api/v1/projects', data);
    return response.data;
  },

  async getProjectById(id: string): Promise<Project> {
    const response = await apiClient.get(`/api/v1/projects/${id}`);
    return response.data;
  },

  async updateProject(id: string, data: UpdateProjectRequest): Promise<Project> {
    const response = await apiClient.put(`/api/v1/projects/${id}`, data);
    return response.data;
  },

  async patchProject(id: string, data: UpdateProjectRequest): Promise<Project> {
    const response = await apiClient.patch(`/api/v1/projects/${id}`, data);
    return response.data;
  },

  async deleteProject(id: string): Promise<void> {
    await apiClient.delete(`/api/v1/projects/${id}`);
  },
};