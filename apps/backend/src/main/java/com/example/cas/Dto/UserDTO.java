package com.example.cas.Dto;

public class UserDTO {

  private int userId;
  private String userName;
  private String email;
  private String password;
  private String cell;

  public UserDTO() {
  }

  public UserDTO(int userId, String userName, String email, String password, String cell) {
    this.userId = userId;
    this.userName = userName;
    this.email = email;
    this.password = password;
    this.cell = cell;
  }

  public int getUserID() {
    return userId;
  }

  public void setUserID(int userId) {
    this.userId = userId;
  }

  public String getUserName() {
    return userName;
  }

  public void setUserName(String userName) {
    this.userName = userName;
  }

  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }

  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }

  public String getCell() {
    return cell;
  }

  public void setCell(String cell) {
    this.cell = cell;
  }

}
