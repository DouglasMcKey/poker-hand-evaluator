import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
    providedIn: "root"
})

export class PokerService {
    private apiUrl = "http://127.0.0.1:8000/evaluate-power-hand/";

    constructor(private http: HttpClient) {
    }

    evaluateHand(hand: any[]): Observable<any> {
        return this.http.post<any>(this.apiUrl, {cards: hand});
    }
}