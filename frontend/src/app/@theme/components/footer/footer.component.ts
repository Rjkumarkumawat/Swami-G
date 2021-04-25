import { Component } from '@angular/core';

@Component({
  selector: 'ngx-footer',
  styleUrls: ['./footer.component.scss'],
  template: `
    <span class="created-by" style="color: #05fcfc; font-family: Exo; font-size: 1.125rem; font-weight: 400;">Rajkumar Kumawat </span>
    <div class="socials">
      <a href="https://twitter.com/Rjkumar_kumawat" target="_blank" class="ion ion-social-twitter"></a>
    </div>
    <div class="socials">
      <a href="https://www.instagram.com/rjkumar0205/" target="_blank" class="ion ion-social-instagram"></a>
    </div>
    <div class="socials">
      <a href="https://github.com/Rajkumar-kumawat" target="_blank" class="ion ion-social-github"></a>
    </div>
    <div class="socials">
      <a target="_blank" href="https://github.com/Rajkumar-kumawat"><i class="fab fa-gitlab"></i></a>
    </div>
    <div class="socials">
      <a href="https://www.linkedin.com/in/rajkumar-kumawat-66072b199/" target="_blank" class="ion ion-social-linkedin"></a>
    </div>
  `,
})
export class FooterComponent {
}
