package com.example.cas.UserController;


import com.example.cas.Dto.LoginDTO;
import com.example.cas.Dto.UserDTO;
import com.example.cas.Entity.User;
import com.example.cas.Service.UserService;
import com.example.cas.response.LoginResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@CrossOrigin
@RequestMapping("api/v1/user")

public class UserController {

    @Autowired
    private UserService userService;

    @PostMapping(path = "/register")
    public String register(@RequestBody UserDTO userDTO) {
        String id = userService.addUser(userDTO);
        return id;
    }

    @PostMapping(path = "/login")
    public ResponseEntity<?> loginUser(@RequestBody LoginDTO loginDTO) {
        LoginResponse loginResponse = userService.loginUser(loginDTO);
        return ResponseEntity.ok(loginResponse);
    }
}
