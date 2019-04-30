import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private http: HttpClient) { }

  getLinearRegressionPrediction(value) {

    return this.http.post<any>(`http://127.0.0.1:5000/linear-regression-prdiction`, { data: value })

  }
  getDecisionTreePrediction(value) {
    return this.http.post<any>(`http://127.0.0.1:5000/decision-tree-prdiction`, { data: value })

  }



}
