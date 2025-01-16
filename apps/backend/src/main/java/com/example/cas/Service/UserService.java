package com.example.cas.Service;

import com.example.cas.Dto.LoginDTO;
import com.example.cas.Dto.UserDTO;
import com.example.cas.response.LoginResponse;

public interface UserService {
    String addUser(UserDTO userDTO);

    LoginResponse loginUser(LoginDTO loginDTO);
}
