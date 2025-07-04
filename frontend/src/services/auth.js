import api from './api';

export async function loginUser(credentials) {
    try {
        const response = await api.post('token/', credentials);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : error;
    }
    
}

export function logoutUser(){
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
}