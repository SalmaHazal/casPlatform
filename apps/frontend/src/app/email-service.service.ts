import { Injectable } from '@angular/core';
import emailjs from 'emailjs-com';

@Injectable({
  providedIn: 'root',
})
export class EmailServiceService {

  sendEmail(formData: any) {
    const templateParams = {
      user_name: formData.userName,
      user_email: formData.userEmail,
      user_message: formData.userMessage,
    };

    emailjs
      .send('service_mk4awon', 'contact_form', templateParams, 'yMcPtZ-59pBrFHjk8')
      .then(
        (response) => {
          console.log('SUCCESS!', response.status, response.text);
        },
        (error) => {
          console.log('FAILED...', error);
        }
      );
  }
}
