package com.example.cas.Entity;

import jakarta.persistence.*;

@Entity
@Table(name="user")
public class User {

  @Id
  @Column(name="user_id", length = 45)
  @GeneratedValue(strategy = GenerationType.AUTO)
  private int userID;

  @Column(name = "user_name", length = 255)
  private String userName;

  @Column(name="email", length = 255)
  private String email;

  @Column(name="password", length= 255)
  private String password;

  @Column(name="cell", length=50)
  private String cell;

  public User(int userID, String userName, String email, String password, String cell) {
    this.userID = userID;
    this.userName = userName;
    this.email = email;
    this.password = password;
    this.cell = cell;
  }

  public User() {
  }

  public int getUserID() {
    return userID;
  }

  public void setUserID(int userID) {
    this.userID = userID;
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

  @Override
  public String toString() {
    return "User{" +
      "userID=" + userID +
      ", userName='" + userName + '\'' +
      ", email='" + email + '\'' +
      ", password='" + password + '\'' +
      ", cell='" + cell + '\'' +
      '}';
  }
}
