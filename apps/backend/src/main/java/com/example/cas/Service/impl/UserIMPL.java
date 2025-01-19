package com.example.cas.Service.impl;

import com.example.cas.Dto.LoginDTO;
import com.example.cas.Dto.UserDTO;
import com.example.cas.Entity.User;
import com.example.cas.Repo.UserRepo;
import com.example.cas.Service.UserService;
import com.example.cas.response.LoginResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UserIMPL implements UserService {

    @Autowired
    private UserRepo userRepo;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Override
    public  String addUser(UserDTO userDTO) {

        User user = new User(
                userDTO.getUserID(),
                userDTO.getUserName(),
                userDTO.getEmail(),
                this.passwordEncoder.encode(userDTO.getPassword()),
                userDTO.getCell()
        );

        userRepo.save(user);

      return "successfully added user";
    }

    @Override
    public LoginResponse loginUser(LoginDTO loginDTO) {
        String msg="";
        User user1 = userRepo.findByEmail(loginDTO.getEmail());
        if (user1 != null) {
            String password = loginDTO.getPassword();
            String encodedPassword = user1.getPassword();
            Boolean isPwdRight=passwordEncoder.matches(password, encodedPassword);
            if (isPwdRight) {
                Optional<User> user = userRepo.findByEmailAndPassword(loginDTO.getEmail(), encodedPassword);
                if (user.isPresent()) {
                    return new LoginResponse("Login Success", true);
                } else {
                    return new LoginResponse("Login Failed", false);
                }
            } else {
                return new LoginResponse("Password not match", false);
            }
        } else {
            return new LoginResponse("Email not exists", false);
        }
    }
}
