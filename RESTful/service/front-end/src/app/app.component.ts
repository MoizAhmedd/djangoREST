import { Component, OnInit} from '@angular/core';
import {SongsService} from './songs.service'
import {throwError} from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  public songs: any;

  constructor(private _songsService: SongsService) {

  }
  ngOnInit(){
    this.getSongs();
  }
  getSongs(){
    this._songsService.list().subscribe(
      data => {
        this.songs = data;
      }
    );
  }
}
