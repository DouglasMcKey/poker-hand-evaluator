import {Component, OnInit} from '@angular/core';
import {SharedModule} from "./shared/shared-module";

@Component({
    selector: 'app-root',
    imports: [SharedModule],
    templateUrl: './app.html',
    styleUrl: './app.css'
})
export class App implements OnInit {
    // The master deck to  manage the available cards.
    masterDeck: any[] = [];
    selectedHand: any[] = [null, null, null, null, null]

    ngOnInit() {
        this.generateDeck();
    }

    generateDeck() {
        /**
         * Build a regular deck of cards and push them to the master deck.
         * These will be used to create the select options for the user.
         */
        const cardValues = [
            [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10],
            [11, "Jack"], [12, "Queen"], [13, "King"], [14, "Ace"]
        ]

        // The offset helps to distinguish between suites and should aid in
        // determining potential hand rankings later on.
        const suites = [
            { name: "Hearts", offset: 100 },
            { name: "Diamonds", offset: 200 },
            { name: "Clubs", offset: 300 },
            { name: "Spades", offset: 400 }
        ]

        let idCounter = 1;
        suites.forEach(suite => {
            cardValues.forEach(card => {
                this.masterDeck.push({
                    id: idCounter++,
                    face_value: card[1],
                    value: suite.offset + (card[0] as number),
                    display: `${card[1]} of ${suite.name}`
                })
            })
        })
    }
}
