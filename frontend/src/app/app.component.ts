import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
prediction;
  constructor(private service:AppService){}

  predict(predictionForm:NgForm){
   let data =  Object.values(predictionForm.value)
   console.log(data,data[data.length] )
   if(data[data.length-1] === 'linear'){
   this.service.getLinearRegressionPrediction(data.slice(0,data.length-1)).subscribe(data=>{
    
    let res = data.result.split(':')[1]

    this.prediction = res.slice(0,res.length-1)
  })
  }else if(data[data.length-1 ] === 'descision'){
    this.service.getDecisionTreePrediction(data.slice(0,data.length-1)).subscribe(data=>{
      let res = data.result.split(':')[1]

      this.prediction = res.slice(0,res.length-1)
    })
  }
  }
}
